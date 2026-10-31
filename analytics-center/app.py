from __future__ import annotations

from pathlib import Path
from typing import BinaryIO

import pandas as pd
import plotly.express as px
import streamlit as st

from metrics import rate

REQUIRED_COLUMNS = {
    "village",
    "sex",
    "age",
    "diabetes_screened",
    "hypertension_screened",
}
MAX_UPLOAD_BYTES = 5 * 1024 * 1024
MAX_ROWS = 100_000


def _file_size(uploaded_file: BinaryIO) -> int:
    current_position = uploaded_file.tell()
    uploaded_file.seek(0, 2)
    size = uploaded_file.tell()
    uploaded_file.seek(current_position)
    return size


def validate_columns(columns: list[str] | pd.Index) -> None:
    received = {str(column).strip() for column in columns}
    missing = REQUIRED_COLUMNS.difference(received)
    extra = received.difference(REQUIRED_COLUMNS)

    if missing:
        raise ValueError(f"ขาดคอลัมน์ที่จำเป็น: {', '.join(sorted(missing))}")
    if extra:
        raise ValueError(
            "พบคอลัมน์ที่ไม่ได้รับอนุญาต: "
            f"{', '.join(sorted(extra))}. "
            "กรุณาใช้เฉพาะแม่แบบ 5 คอลัมน์ที่กำหนด"
        )


def load_data(uploaded_file=None) -> pd.DataFrame:
    if uploaded_file is not None:
        if _file_size(uploaded_file) > MAX_UPLOAD_BYTES:
            raise ValueError("ไฟล์มีขนาดเกิน 5 MB")
        uploaded_file.seek(0)
        frame = pd.read_csv(uploaded_file, nrows=MAX_ROWS + 1)
    else:
        sample_path = Path(__file__).parent / "data" / "sample_population.csv"
        frame = pd.read_csv(sample_path, nrows=MAX_ROWS + 1)

    if len(frame) > MAX_ROWS:
        raise ValueError(f"ไฟล์มีจำนวนข้อมูลเกิน {MAX_ROWS:,} แถว")

    validate_columns(frame.columns)
    frame = frame[list(REQUIRED_COLUMNS)].copy()
    frame["age"] = pd.to_numeric(frame["age"], errors="coerce")
    frame["diabetes_screened"] = pd.to_numeric(
        frame["diabetes_screened"], errors="coerce"
    ).fillna(0)
    frame["hypertension_screened"] = pd.to_numeric(
        frame["hypertension_screened"], errors="coerce"
    ).fillna(0)
    frame = frame.dropna(subset=["village", "sex", "age"])
    frame = frame[frame["age"].between(0, 120)].copy()
    frame["diabetes_screened"] = frame["diabetes_screened"].clip(0, 1)
    frame["hypertension_screened"] = frame["hypertension_screened"].clip(0, 1)
    frame["age_group"] = pd.cut(
        frame["age"],
        bins=[-1, 14, 34, 59, 69, 120],
        labels=["0–14", "15–34", "35–59", "60–69", "70+"],
    )
    return frame


def main() -> None:
    st.set_page_config(
        page_title="Future29 Analytics Center",
        page_icon="📊",
        layout="wide",
    )
    st.title("Future29 Analytics Center 📊🏥")
    st.caption("Dashboard ตัวอย่างสำหรับข้อมูลประชากรและ KPI สาธารณสุขแบบไม่ระบุตัวบุคคล")

    with st.sidebar:
        st.header("แหล่งข้อมูล")
        uploaded = st.file_uploader(
            "เลือกไฟล์ CSV",
            type=["csv"],
            help="สูงสุด 5 MB และ 100,000 แถว",
        )
        st.warning(
            "ระบบรับเฉพาะ 5 คอลัมน์ตามแม่แบบ และจะปฏิเสธไฟล์ที่มีคอลัมน์อื่น "
            "เช่น ชื่อ HN เลขบัตรประชาชน หรือวันเกิด"
        )

    try:
        data = load_data(uploaded)
    except Exception as exc:
        st.error(f"อ่านข้อมูลไม่สำเร็จ: {exc}")
        st.stop()

    villages = sorted(data["village"].astype(str).unique())
    selected = st.sidebar.multiselect("พื้นที่", villages, default=villages)
    filtered = data[data["village"].astype(str).isin(selected)].copy()

    total = len(filtered)
    older_adults = int((filtered["age"] >= 60).sum())
    dm_rate = rate(filtered["diabetes_screened"])
    ht_rate = rate(filtered["hypertension_screened"])

    c1, c2, c3, c4 = st.columns(4)
    c1.metric("ประชากรทั้งหมด", f"{total:,}")
    c2.metric("ผู้สูงอายุ 60+", f"{older_adults:,}")
    c3.metric("คัดกรองเบาหวาน", f"{dm_rate:.1f}%")
    c4.metric("คัดกรองความดัน", f"{ht_rate:.1f}%")

    left, right = st.columns(2)
    with left:
        village_summary = (
            filtered.groupby("village", as_index=False)
            .size()
            .rename(columns={"size": "population"})
        )
        fig_village = px.bar(
            village_summary,
            x="village",
            y="population",
            title="จำนวนประชากรตามพื้นที่",
            labels={"village": "พื้นที่", "population": "จำนวน"},
        )
        st.plotly_chart(fig_village, use_container_width=True)

    with right:
        age_summary = (
            filtered.groupby("age_group", observed=False, as_index=False)
            .size()
            .rename(columns={"size": "population"})
        )
        fig_age = px.bar(
            age_summary,
            x="age_group",
            y="population",
            title="โครงสร้างประชากรตามช่วงอายุ",
            labels={"age_group": "ช่วงอายุ", "population": "จำนวน"},
        )
        st.plotly_chart(fig_age, use_container_width=True)

    st.subheader("ตาราง KPI รายพื้นที่")
    kpi = (
        filtered.groupby("village", as_index=False)
        .agg(
            population=("age", "size"),
            older_adults=("age", lambda values: int((values >= 60).sum())),
            diabetes_screening=("diabetes_screened", "mean"),
            hypertension_screening=("hypertension_screened", "mean"),
        )
    )
    kpi["diabetes_screening"] = (kpi["diabetes_screening"] * 100).round(1)
    kpi["hypertension_screening"] = (kpi["hypertension_screening"] * 100).round(1)
    kpi["status"] = kpi[["diabetes_screening", "hypertension_screening"]].min(axis=1).apply(
        lambda value: "ผ่าน" if value >= 90 else "ต้องติดตาม"
    )
    st.dataframe(kpi, use_container_width=True, hide_index=True)

    csv_bytes = kpi.to_csv(index=False).encode("utf-8-sig")
    st.download_button(
        "ดาวน์โหลดสรุป KPI",
        data=csv_bytes,
        file_name="future29_kpi_summary.csv",
        mime="text/csv",
    )


if __name__ == "__main__":
    main()
