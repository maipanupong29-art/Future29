import SwiftUI

struct AboutView: View {
    var body: some View {
        NavigationStack {
            List {
                Section("แอป") {
                    LabeledContent("ชื่อ", value: "Future29")
                    LabeledContent("รุ่นต้นแบบ", value: "0.1.0")
                    LabeledContent("ระบบขั้นต่ำ", value: "iOS 17")
                }

                Section("หลักการ") {
                    Label("ออกแบบด้วย SwiftUI", systemImage: "swift")
                    Label("ไม่เก็บข้อมูลผู้ป่วยจริง", systemImage: "lock.shield.fill")
                    Label("พัฒนาเป็นหมวดและทดสอบได้", systemImage: "shippingbox.fill")
                }
            }
            .navigationTitle("เกี่ยวกับ")
        }
    }
}

#Preview {
    AboutView()
}
