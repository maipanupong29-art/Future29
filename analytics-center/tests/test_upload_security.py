from io import BytesIO

import pandas as pd
import pytest

import app


VALID_HEADER = (
    "village,sex,age,diabetes_screened,hypertension_screened\n"
)


def csv_file(text: str) -> BytesIO:
    return BytesIO(text.encode("utf-8"))


def test_rejects_extra_columns():
    file_obj = csv_file(
        VALID_HEADER.replace("\n", ",hn\n")
        + "คลองใช้,หญิง,67,1,1,12345\n"
    )

    with pytest.raises(ValueError, match="คอลัมน์ที่ไม่ได้รับอนุญาต"):
        app.load_data(file_obj)


def test_rejects_oversized_file(monkeypatch):
    file_obj = csv_file(VALID_HEADER + "คลองใช้,หญิง,67,1,1\n")
    monkeypatch.setattr(app, "MAX_UPLOAD_BYTES", 10)

    with pytest.raises(ValueError, match="ขนาดเกิน"):
        app.load_data(file_obj)


def test_rejects_too_many_rows(monkeypatch):
    file_obj = csv_file(
        VALID_HEADER
        + "คลองใช้,หญิง,67,1,1\n"
        + "คลองใช้,ชาย,45,1,1\n"
    )
    monkeypatch.setattr(app, "MAX_ROWS", 1)

    with pytest.raises(ValueError, match="จำนวนข้อมูลเกิน"):
        app.load_data(file_obj)


def test_accepts_only_required_columns():
    file_obj = csv_file(VALID_HEADER + "คลองใช้,หญิง,67,1,1\n")
    frame = app.load_data(file_obj)

    assert len(frame) == 1
    assert set(app.REQUIRED_COLUMNS).issubset(frame.columns)
    assert "age_group" in frame.columns


def test_invalid_age_is_removed():
    file_obj = csv_file(
        VALID_HEADER
        + "คลองใช้,หญิง,999,1,1\n"
        + "คลองใช้,ชาย,45,1,1\n"
    )
    frame = app.load_data(file_obj)

    assert frame["age"].tolist() == [45]
