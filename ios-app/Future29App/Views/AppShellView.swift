import SwiftUI

struct AppShellView: View {
    private enum AppTab: Hashable {
        case home
        case about
    }

    @State private var selectedTab: AppTab = .home

    var body: some View {
        TabView(selection: $selectedTab) {
            Tab("หน้าหลัก", systemImage: "square.grid.2x2.fill", value: .home) {
                DashboardView()
            }

            Tab("เกี่ยวกับ", systemImage: "info.circle.fill", value: .about) {
                AboutView()
            }
        }
    }
}

#Preview {
    AppShellView()
}
