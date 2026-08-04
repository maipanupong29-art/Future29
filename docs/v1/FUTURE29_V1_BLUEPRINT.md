# Future29 v1.0 — Product Blueprint

## วิสัยทัศน์
Future29 คือ Digital Public Health Workspace ส่วนบุคคลสำหรับรวมงานข้อมูลประชากร งาน Excel งานปฏิทิน งาน KPI และงานอัตโนมัติของโรงพยาบาลไว้ในระบบเดียว โดยออกแบบให้ปลอดภัย ตรวจสอบได้ และต่อยอดได้โดยไม่ต้องรื้อโครงสร้างใหม่

## หลักการออกแบบ
- ข้อมูลจริงต้องไม่ขึ้น GitHub
- ใช้ข้อมูลจำลองหรือข้อมูลที่ทำให้ไม่ระบุตัวบุคคลแล้วเท่านั้น
- แยก UI, business logic, storage และ integration ออกจากกัน
- ทุกฟีเจอร์สำคัญต้องมี test และ CI
- รองรับ Dynamic Type, VoiceOver, Dark Mode และภาษาไทย
- ใช้ SwiftUI แบบ feature-first และ dependency injection

## 20 โมดูลหลัก
1. Home Dashboard
2. Population Import
3. Population Validation
4. Population Master
5. Population Reports
6. Excel Tools
7. Excel Templates
8. Analytics Overview
9. KPI Dashboard
10. Trend Analysis
11. Calendar Manager
12. ICS Builder
13. Duplicate Calendar Audit
14. Hospital Workflows
15. Task & Deadline Center
16. Reports & Export
17. File Library
18. Notifications
19. Security & Privacy
20. Settings & Administration

## เป้าหมายรุ่น 1.0
- มากกว่า 100 หน้าจอรวมสถานะ loading, empty, error, detail และ editor
- แอป iOS 17+ ด้วย SwiftUI
- Analytics Center ด้วย Python/Streamlit
- ระบบ CI สำหรับ iOS และ Python
- เอกสารสถาปัตยกรรม ความปลอดภัย การทดสอบ และการใช้งาน
- ยังไม่เชื่อมข้อมูลผู้ป่วยจริงใน v1.0 จนกว่าจะผ่านการประเมิน PDPA และ security review

## สถาปัตยกรรม
```text
Future29App
├── AppCore
│   ├── Routing
│   ├── DesignSystem
│   ├── Security
│   └── SharedServices
├── Features
│   ├── Home
│   ├── Population
│   ├── ExcelTools
│   ├── Analytics
│   ├── Calendar
│   ├── Hospital
│   ├── Reports
│   └── Settings
├── Data
│   ├── Models
│   ├── Repositories
│   ├── LocalStorage
│   └── ImportExport
└── Tests
    ├── Unit
    ├── Integration
    ├── Snapshot
    └── UI
```

## Definition of Done
ฟีเจอร์ถือว่าเสร็จเมื่อ:
- Build ผ่าน
- Unit tests ผ่าน
- ไม่มี secret หรือข้อมูลส่วนบุคคลใน repository
- มี loading, empty และ error state
- รองรับ accessibility ขั้นพื้นฐาน
- มีเอกสารวิธีใช้และข้อจำกัด
- ผ่าน security checklist ก่อน merge
