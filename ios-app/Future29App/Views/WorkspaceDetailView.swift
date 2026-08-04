import SwiftUI

struct WorkspaceDetailView: View {
    let destination: WorkspaceDestination

    var body: some View {
        List {
            Section {
                Label(configuration.summary, systemImage: configuration.symbol)
                    .font(.headline)
                    .padding(.vertical, 8)
            }

            Section("สิ่งที่จะพัฒนาต่อ") {
                ForEach(configuration.nextSteps, id: \.self) { step in
                    Label(step, systemImage: "checkmark.circle")
                }
            }

            Section("ความปลอดภัยของข้อมูล") {
                Label(
                    "ใช้เฉพาะข้อมูลจำลองหรือข้อมูลที่ไม่สามารถระบุตัวบุคคลได้",
                    systemImage: "lock.shield.fill"
                )
            }
        }
        .navigationTitle(configuration.title)
        .navigationBarTitleDisplayMode(.inline)
    }

    private var configuration: DetailConfiguration {
        switch destination {
        case .population:
            DetailConfiguration(
                title: "ข้อมูลประชากร",
                symbol: "person.3.fill",
                summary: "เครื่องมือรวม ตรวจสอบ ทำความสะอาด และแปลงไฟล์ประชากร",
                nextSteps: ["เลือกไฟล์แม่แบบ", "ตรวจเงื่อนไขข้อมูล", "ส่งออกรายงานสรุป"]
            )
        case .excel:
            DetailConfiguration(
                title: "Excel สาธารณสุข",
                symbol: "tablecells.fill",
                summary: "ศูนย์รวมสูตร แม่แบบ และเครื่องมือจัดรูปแบบ Excel",
                nextSteps: ["เปิดรายการเครื่องมือ", "ตั้งค่าเงื่อนไข", "ตรวจผลก่อนบันทึก"]
            )
        case .calendar:
            DetailConfiguration(
                title: "ปฏิทิน Future",
                symbol: "calendar.badge.clock",
                summary: "สร้าง ตรวจ รวม แยก และค้นหารายการซ้ำในไฟล์ ICS",
                nextSteps: ["เลือกหมวดปฏิทิน", "ตรวจชื่อและอิโมจิ", "ส่งออกไฟล์ ICS"]
            )
        case .hospital:
            DetailConfiguration(
                title: "งานอัตโนมัติ รพ.",
                symbol: "cross.case.fill",
                summary: "ติดตาม KPI รายงาน และ Workflow งานประจำในที่เดียว",
                nextSteps: ["เลือก Workflow", "ตรวจสถานะงาน", "สรุปสิ่งที่ต้องดำเนินการ"]
            )
        }
    }
}

private struct DetailConfiguration {
    let title: String
    let symbol: String
    let summary: String
    let nextSteps: [String]
}

#Preview {
    NavigationStack {
        WorkspaceDetailView(destination: .calendar)
    }
}
