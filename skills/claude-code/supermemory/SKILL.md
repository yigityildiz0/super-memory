---
name: supermemory
description: Always-on project memory skill for Claude Code, Codex, ChatGPT, and other AI coding sessions. Use automatically at the start of project or coding work, before planning, to locate or create `.ai-handoff/SUPER_MEMORY.md`, read the current packet, compare agent cursors, and keep the file updated after meaningful progress. Also use for `/supermemory`, `supermemory search`, `supermemory update`, `supermemory new`, `supermemory compress`, `supermemory delete`, `supermemory status`, Super Memory, resume, continue, handoff, context window full, limit reached, switch to Codex, switch to Claude Code, new chat continuation, deleted chat recovery, teammate handoff, devam et, kaldığım yerden devam et, limit bitti, context doldu, and project memory requests.
---

# Super Memory

Use this skill as a project-local memory system. It helps Claude Code, Codex, ChatGPT, and other agents continue from the same project state without relying on private chat history.

Credit: Super Memory by Yigit Yildiz, GitHub `@yigityildiz0`.

## First Move

For any real project task:

1. Identify the active project root.
2. Look for `.ai-handoff/SUPER_MEMORY.md`.
3. If it exists, read `Current Packet` first.
4. Read only timeline entries newer than this agent's cursor when possible.
5. If it is missing, create it before substantial work.
6. If older `.ai-handoff/SUPERMEMORY.md` or `.ai-handoff/HANDOFF.md` exists, migrate useful facts into `SUPER_MEMORY.md`.
7. If the root is ambiguous, ask where the project memory should live.

Do this before planning when the user asks to continue, resume, switch agents, recover from a limit, recover from a deleted chat, or work on project files.

## Storage

Use one project-local memory folder:

- `.ai-handoff/SUPER_MEMORY.md`: canonical current project memory.
- `.ai-handoff/LOG.md`: compact older milestones.

Do not create multiple competing memory files for the same project.

## Commands

Treat these as slash-style commands:

- `/supermemory search`: find/read memory, absorb current packet, then read only new entries since this agent's cursor.
- `/supermemory update`: refresh current packet and append a compact checkpoint after meaningful progress.
- `/supermemory new`: create memory only when none exists; if one exists, update it instead of creating a duplicate.
- `/supermemory compress`: preserve active state, shorten stale timeline, move old detail to `LOG.md`.
- `/supermemory delete`: delete only `.ai-handoff/` after explicit user intent and root confirmation.
- `/supermemory status`: report memory path, age, latest checkpoint, and next action.

## What To Save

Save operational facts:

- goal and scope
- project root
- user constraints that affect the work
- active files and why they matter
- completed changes
- decisions with evidence
- commands, tests, checks, and results
- blockers, failed attempts, and useful error text
- next 3-7 actions
- notes for the next agent

Never save hidden reasoning, full transcripts, secrets, API keys, credentials, huge logs, or unrelated personal data.

## Format

Keep `SUPER_MEMORY.md` compact and readable:

```markdown
# Super Memory

Last updated: <ISO datetime>
Updated by: <Codex | Claude Code | ChatGPT | Other>
Project root: <path>
Mode: compact

## Current Packet
- Goal: <1-3 bullets max>
- State: <current state>
- Active files: `<path>` = <why it matters>
- Decisions: <decision> -> <reason/evidence>
- Verification: `<command/check>` -> <result>
- Blockers: <none or current blocker>
- Next: <3-7 concrete actions>

## Agent Cursors
- Codex last-read: <checkpoint id or none>
- Claude Code last-read: <checkpoint id or none>
- ChatGPT last-read: <checkpoint id or none>
- Other last-read: <checkpoint id or none>

## Timeline
- cp-YYYYMMDDTHHMMSSffffffZ | <Agent> | <dense update>
```

## Cursor Rule

The current packet is always relevant. Timeline entries are incremental.

When Claude Code resumes:

1. Read `Current Packet`.
2. Find `Claude Code last-read`.
3. Read timeline entries after that checkpoint.
4. Prioritize entries written by other agents after the cursor.
5. Update `Claude Code last-read` after absorbing them.

If the cursor is missing, read the latest packet plus the last 10 timeline entries.

## Compression Rule

Keep memory dense from the start. Prefer this style:

- `Auth fix done; changed src/auth.ts; npm test pass; next deploy.`
- `Build fail: missing env VITE_API_URL; no code issue found.`

Avoid this style:

- `I worked on the project and made some progress.`
- pasted conversations
- repeated explanations

When compressing:

1. Preserve goal, active files, decisions, verification, blockers, and next actions.
2. Keep the latest useful timeline entries.
3. Move old entries into `LOG.md` as short milestones.
4. Remove obsolete detail unless it prevents repeating a mistake.

## Update Timing

Update memory after:

- behavior-changing edits
- new or resolved blockers
- changed plan or scope
- tests/build/lint checks
- failed attempts worth remembering
- agent switch
- likely context reset or limit
- before ending a long turn

## Helper Script

Use `scripts/supermemory.py` for deterministic file handling:

```bash
python scripts/supermemory.py search --root . --agent "Claude Code"
python scripts/supermemory.py update --root . --agent "Claude Code" --message "Implemented X; tests passed."
python scripts/supermemory.py new --root . --agent "Claude Code"
python scripts/supermemory.py compress --root . --keep 20
python scripts/supermemory.py status --root .
python scripts/supermemory.py delete --root . --yes
```

Manual edits are acceptable when they produce a clearer current packet.

