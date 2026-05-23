# Future29

## Project Overview
Future29 is currently in the bootstrap phase. This repository is prepared to become the primary codebase for the product and includes a standard onboarding guide for new contributors.

## Goals for New Contributors
- Understand the repository layout and team conventions quickly.
- Set up local development in a reproducible way.
- Know where to add new features, tests, and documentation.

## Recommended Repository Structure

```text
Future29/
├── README.md
├── docs/
│   ├── architecture.md
│   ├── adr/
│   └── onboarding.md
├── src/
│   ├── core/
│   ├── modules/
│   ├── services/
│   └── utils/
├── tests/
│   ├── unit/
│   ├── integration/
│   └── e2e/
├── scripts/
├── .github/
│   └── workflows/
├── .editorconfig
├── .gitignore
└── <language-specific config files>
```

## Onboarding Checklist

### 1) Understand the Context
- Read this README end to end.
- Read `docs/architecture.md` for high-level design.
- Check open issues and current roadmap/milestones.

### 2) Local Setup (Template)
> Replace commands below to match your stack.

```bash
# Example only
# install dependencies
<package-manager> install

# run application
<package-manager> run dev

# run tests
<package-manager> test
```

### 3) Development Workflow
1. Create a feature branch from `main`.
2. Implement in `src/` with focused commits.
3. Add tests under `tests/`.
4. Run lint + tests locally before pushing.
5. Open PR with summary, risks, and test evidence.

## Coding & Collaboration Standards
- Keep modules small and single-purpose.
- Prefer explicit naming over abbreviations.
- Add or update tests for every meaningful change.
- Update docs when behavior or architecture changes.
- Use conventional commit messages (recommended):
  - `feat:` new feature
  - `fix:` bug fix
  - `docs:` documentation only
  - `refactor:` internal code improvements
  - `test:` test-related changes
  - `chore:` maintenance work

## Architecture Notes (Starter)
Until implementation begins, use this simple layering model:
- **Core**: shared domain logic and entities.
- **Modules**: feature-level business use cases.
- **Services**: external integrations (DB/API/queues).
- **Interface Layer**: HTTP handlers, CLI commands, or UI adapters.

## What to Learn Next
For new team members, recommended learning order:
1. Product scope and domain vocabulary.
2. System architecture and module boundaries.
3. Testing strategy (unit/integration/e2e).
4. Deployment and CI/CD pipeline.
5. Observability: logs, metrics, tracing.

## Contribution Template
When opening a PR, include:
- What changed
- Why it changed
- How it was tested
- Backward compatibility impact
- Follow-up tasks

## Ownership (Fill In)
- Tech lead: `<name>`
- Review owners: `<team-or-handle>`
- Slack/Chat channel: `<channel>`
