# Architecture (Draft)

## Purpose
This draft defines the target structure to keep the project maintainable as it grows.

## Proposed Layers
- Core domain logic (`src/core`)
- Feature modules (`src/modules`)
- Integration services (`src/services`)
- Shared helpers (`src/utils`)

## Testing Strategy
- Unit tests for pure logic.
- Integration tests for boundaries and dependencies.
- End-to-end tests for critical user flows.

## Next Architecture Decisions
Use ADRs under `docs/adr/` to record:
1. Tech stack selection
2. Data storage choice
3. API style (REST/GraphQL/etc.)
4. Authentication/authorization model
