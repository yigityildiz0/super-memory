# Install Super Memory

This guide is written for people who do not use GitHub often.

## Option 1: Download Everything

1. Open the Super Memory GitHub page.
2. Click the green **Code** button.
3. Click **Download ZIP**.
4. Unzip the file.
5. Open the folder.

You will see:

- `skills/codex/super-memory` for Codex
- `skills/claude-code/supermemory` for Claude Code
- `examples/SUPER_MEMORY.md` for manual use
- `docs/` for explanations

## Option 2: Codex Only

1. Download `super-memory-codex-skill.zip` from the latest release.
2. Unzip it.
3. Copy the `super-memory` folder into:

```text
~/.codex/skills/super-memory
```

Windows example:

```text
C:\Users\YOUR_NAME\.codex\skills\super-memory
```

Then restart Codex if needed.

## Option 3: Claude Code Only

1. Download `super-memory-claude-code-skill.zip` from the latest release.
2. Unzip it.
3. Copy the `supermemory` folder into:

```text
~/.claude/skills/supermemory
```

Optional slash command:

Copy this file:

```text
commands/claude-code/supermemory.md
```

into your Claude Code commands folder if you want `/supermemory`.

## Option 4: Manual Use

If you do not want to install anything:

1. Create `.ai-handoff/` inside your project.
2. Copy `examples/SUPER_MEMORY.md` into that folder.
3. Tell your AI assistant to read it before working.

Example prompt:

```text
Read .ai-handoff/SUPER_MEMORY.md first. Continue from the current state. Update it after meaningful progress.
```

