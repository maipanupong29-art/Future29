# Future Calendar System

เครื่องมือสร้าง ตรวจสอบ รวม แยก และลบรายการซ้ำในไฟล์ `.ics`

## เนื้อหาที่ควรเก็บ

- `src/` โปรแกรมสร้างและตรวจไฟล์ปฏิทิน
- `palettes/` ชุดสีและรหัสสีที่อนุมัติ
- `schemas/` มาตรฐานชื่อเหตุการณ์และ CODE
- `examples/` ตัวอย่าง `.ics` ที่ใช้ข้อมูลสมมติ
- `tests/` ชุดทดสอบ recurrence, timezone และ duplicate detection

มาตรฐานหลัก: **Future Calendar Design System v1.0**

## Source of Truth

- ปฏิทินใช้งานจริง: Google Calendar หลัก
- ตารางควบคุมและทะเบียนไฟล์: Google Drive — `ปฏิทินชีวิต 2569`
- Time zone มาตรฐาน: `Asia/Bangkok`
- ปฏิทิน iPhone ให้ซิงก์จาก Google Calendar เพื่อลดการสร้างข้อมูลซ้ำหลายต้นทาง

## รูปแบบตัวอักษร

- ตารางควบคุมใน Google Sheets ใช้ **Angsana New 12 pt** เป็นรูปแบบหลัก
- Google Calendar และแอป Calendar ของ iPhone ใช้ฟอนต์ตามระบบ จึงไม่สามารถบังคับ Angsana New ต่อเหตุการณ์ได้
- หน้าจอแอป SwiftUI ที่พัฒนาเองสามารถกำหนด typography แยกได้ แต่ต้องรักษา Dynamic Type และ VoiceOver

## กฎความปลอดภัยของข้อมูล

- ห้าม commit ไฟล์ `.ics` จริงที่มีข้อมูลส่วนบุคคล สุขภาพ หรือรายละเอียดนัดหมายลง public repository
- ใช้ข้อมูลสมมติใน `examples/` เท่านั้น
- ก่อนนำเข้าไฟล์ชุดใหญ่ให้ตรวจ UID ซ้ำ, RRULE, timezone และเหตุการณ์ซ้ำทุกครั้ง
- ระบบภายนอกที่สร้างเหตุการณ์เอง เช่น time-blocking automation ควรแยกจาก MASTER และไม่แก้ทับโดยไม่มีเหตุผล
