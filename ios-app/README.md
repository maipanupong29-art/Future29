# Future29 iOS

แอปต้นแบบ SwiftUI สำหรับเข้าถึงเครื่องมือหลักใน Repository `Future29`

## ความสามารถในรุ่นเริ่มต้น

- Dashboard รวม 4 หมวดงานหลัก
- NavigationStack สำหรับเปิดรายละเอียดแต่ละหมวด
- TabView แยกหน้าหลักและข้อมูลแอป
- รองรับ Dynamic Type และ VoiceOver เบื้องต้น
- ไม่มีการเก็บข้อมูลผู้ป่วยหรือข้อมูลส่วนบุคคลจริง

## ความต้องการ

- Xcode 16 หรือใหม่กว่า
- iOS 17+
- XcodeGen สำหรับสร้างไฟล์ `.xcodeproj`

## วิธีเปิดโครงการ

```bash
cd ios-app
xcodegen generate
open Future29.xcodeproj
```

จากนั้นเลือก Simulator และกด Run

## โครงสร้าง

```text
ios-app/
├── project.yml
├── Future29App/
│   ├── Future29App.swift
│   ├── Models/
│   ├── Views/
│   └── Resources/
└── README.md
```

> แอปนี้เป็นโครงสร้างเริ่มต้นสำหรับพัฒนาต่อ ไม่เชื่อมฐานข้อมูลจริง และไม่ควรฝัง secret หรือข้อมูลสุขภาพที่ระบุตัวบุคคลได้
