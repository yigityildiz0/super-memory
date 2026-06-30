# Super Memory

Last updated: 2026-06-30T12:00:00Z
Updated by: Codex
Project root: /example/project
Mode: compact

## Current Packet
- Goal: Build a project feature and keep state portable across AI tools.
- State: Project memory created; next agent should inspect the listed files before editing.
- Active files: `src/app.ts` = main logic; `tests/app.test.ts` = verification.
- Decisions: Use one project-local memory file so Codex, Claude Code, and ChatGPT can continue from the same state.
- Verification: `npm test` -> passing before next change.
- Blockers: none
- Next: inspect active files; implement the next change; run tests; update Super Memory.

## Agent Cursors
- Codex last-read: cp-20260630T120000000000Z
- Claude Code last-read: none
- ChatGPT last-read: none
- Other last-read: none

## Timeline
- cp-20260630T120000000000Z | Codex | Created initial Super Memory file; next agent should continue from Current Packet.

