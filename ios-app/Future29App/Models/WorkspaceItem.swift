import SwiftUI

struct WorkspaceItem: Identifiable, Hashable {
    let id: String
    let title: String
    let subtitle: String
    let symbol: String
    let destination: WorkspaceDestination

    static let samples: [WorkspaceItem] = [
        WorkspaceItem(
            id: "population",
            title: "ข้อมูลประชากร",
            subtitle: "รวม ตรวจสอบ และแปลงไฟล์ Master",
            symbol: "person.3.fill",
            destination: .population
        ),
        WorkspaceItem(
            id: "excel",
            title: "Excel สาธารณสุข",
            subtitle: "สูตร แม่แบบ และสคริปต์ OpenPyXL",
            symbol: "tablecells.fill",
            destination: .excel
        ),
        WorkspaceItem(
            id: "calendar",
            title: "ปฏิทิน Future",
            subtitle: "สร้าง ตรวจ รวม และจัดการไฟล์ ICS",
            symbol: "calendar.badge.clock",
            destination: .calendar
        ),
        WorkspaceItem(
            id: "hospital",
            title: "งานอัตโนมัติ รพ.",
            subtitle: "KPI รายงาน และ Workflow งานประจำ",
            symbol: "cross.case.fill",
            destination: .hospital
        )
    ]
}

enum WorkspaceDestination: String, Hashable {
    case population
    case excel
    case calendar
    case hospital
}
