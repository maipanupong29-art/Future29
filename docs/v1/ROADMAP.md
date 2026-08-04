# Future29 v1.0 — Roadmap

## Phase 0: Foundation
- Product blueprint
- 20-module boundary
- 120-screen catalog
- Security baseline
- CI/CD baseline
- Design system tokens

## Phase 1: App Shell
- TabView + NavigationStack
- Router และ deep-link model
- Shared loading/empty/error components
- Theme, typography, spacing และ accessibility
- Mock repositories สำหรับ Preview และ Test

## Phase 2: Population Core
- Import CSV/XLSX ผ่านไฟล์ที่ทำให้ไม่ระบุตัวบุคคล
- Column mapping
- Validation rules
- Duplicate detection
- Master list และ export summary

## Phase 3: Analytics Core
- KPI cards
- Area comparison
- Age distribution
- Screening coverage
- Trend charts
- Export CSV/PDF summary

## Phase 4: Calendar Core
- ICS import/export
- Event editor
- Recurrence and alarm editor
- Duplicate audit
- Calendar summary

## Phase 5: Hospital Workflow
- Workflow library
- Checklist execution
- Task/deadline center
- Status history
- Summary export

## Phase 6: Security & Operations
- App lock and Face ID
- Keychain for local secrets
- Audit log
- Backup/restore design
- Privacy manifest
- Security scan and release checklist

## Phase 7: Release Candidate
- Full regression test
- Accessibility audit
- Performance audit
- Dependency pinning
- Documentation freeze
- TestFlight/internal distribution preparation

## CI/CD Gates
ทุก Pull Request ต้องผ่าน:
1. Swift build
2. Python tests
3. Lint/format
4. Secret scan
5. Dependency review
6. Unit tests
7. Smoke tests
8. Security checklist

## Release Rule
ห้ามเชื่อมข้อมูลผู้ป่วยจริงก่อนมี:
- Data classification
- PDPA review
- Threat model
- Encryption design
- Access control design
- Audit logging
- Incident response procedure
