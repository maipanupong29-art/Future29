import SwiftUI

struct DashboardView: View {
    private let items = WorkspaceItem.samples
    private let columns = [GridItem(.adaptive(minimum: 155), spacing: 16)]

    var body: some View {
        NavigationStack {
            ScrollView {
                LazyVGrid(columns: columns, spacing: 16) {
                    ForEach(items) { item in
                        NavigationLink(value: item.destination) {
                            WorkspaceCard(item: item)
                        }
                        .buttonStyle(.plain)
                        .accessibilityHint("เปิดรายละเอียดหมวด \(item.title)")
                    }
                }
                .padding()
            }
            .navigationTitle("Future29")
            .navigationDestination(for: WorkspaceDestination.self) { destination in
                WorkspaceDetailView(destination: destination)
            }
        }
    }
}

private struct WorkspaceCard: View {
    let item: WorkspaceItem

    var body: some View {
        VStack(alignment: .leading, spacing: 12) {
            Image(systemName: item.symbol)
                .font(.title)
                .symbolRenderingMode(.hierarchical)
                .accessibilityHidden(true)

            Text(item.title)
                .font(.headline)

            Text(item.subtitle)
                .font(.subheadline)
                .foregroundStyle(.secondary)
                .lineLimit(3)

            Spacer(minLength: 0)
        }
        .frame(maxWidth: .infinity, minHeight: 160, alignment: .topLeading)
        .padding()
        .background(.thinMaterial, in: RoundedRectangle(cornerRadius: 20, style: .continuous))
        .contentShape(RoundedRectangle(cornerRadius: 20, style: .continuous))
    }
}

#Preview {
    DashboardView()
}
