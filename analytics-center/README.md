# Future29 Analytics Center 📊🏥

ศูนย์กลางวิเคราะห์ข้อมูลสำหรับงานประชากร งาน KPI และงานสาธารณสุข โดยใช้ข้อมูลจำลองหรือข้อมูลที่ผ่านการทำให้ไม่ระบุตัวบุคคลแล้วเท่านั้น

## ความสามารถเริ่มต้น

- Dashboard ภาพรวมประชากร
- สรุปจำนวนตามหมู่บ้าน เพศ และช่วงอายุ
- แสดง KPI พร้อมสถานะเทียบเป้าหมาย
- กรองข้อมูลตามพื้นที่
- รองรับไฟล์ CSV ที่ไม่มีข้อมูลระบุตัวบุคคล
- ส่งออกตารางสรุปจากหน้า Dashboard

## โครงสร้าง

```text
analytics-center/
├── app.py
├── requirements.txt
├── data/
│   └── sample_population.csv
├── tests/
│   └── test_metrics.py
└── README.md
```

## วิธีรัน

```bash
cd analytics-center
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
streamlit run app.py
```

บน Windows ให้ใช้ `.venv\\Scripts\\activate` แทนคำสั่ง activate ด้านบน

## รูปแบบข้อมูลขั้นต่ำ

| คอลัมน์ | ความหมาย |
|---|---|
| village | ชื่อหมู่บ้านหรือพื้นที่ |
| sex | เพศ เช่น ชาย/หญิง |
| age | อายุเต็มปี |
| diabetes_screened | 1 = คัดกรองแล้ว, 0 = ยังไม่คัดกรอง |
| hypertension_screened | 1 = คัดกรองแล้ว, 0 = ยังไม่คัดกรอง |

## กฎความปลอดภัย

ห้ามอัปโหลดชื่อ นามสกุล HN เลขบัตรประชาชน วันเกิดจริง ที่อยู่ละเอียด เบอร์โทรศัพท์ หรือข้อมูลอื่นที่ระบุตัวบุคคลได้ขึ้น GitHub
