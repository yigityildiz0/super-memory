# Commands

Super Memory commands can be typed as plain language in Codex, ChatGPT, or Claude. In Claude Code, you can also use them as slash-style commands if you install the optional command wrapper.

## `supermemory search`

Use at the start of a session.

It should:

1. find `.ai-handoff/SUPER_MEMORY.md`
2. read the current packet
3. read only new timeline entries since this agent's last cursor
4. continue from the latest state

## `supermemory update`

Use after meaningful progress.

Record:

- changed files
- completed work
- test results
- errors
- blockers
- next steps

Keep it short. Do not paste the whole chat.

## `supermemory new`

Use when a project has no memory file yet.

If a memory file already exists, do not create a duplicate. Read and update the existing file instead.

## `supermemory compress`

Use when the memory file gets too long.

Preserve:

- current goal
- active files
- decisions
- test results
- blockers
- next steps

Move older details into `LOG.md` as short milestones.

## `supermemory status`

Use to check where the memory file is and what checkpoint is latest.

## `supermemory delete`

Use only when you intentionally want to remove project memory.

It should delete only:

```text
.ai-handoff/
```

It must not delete source code, project files, Git history, or global chat history.

