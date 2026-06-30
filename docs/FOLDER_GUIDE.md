# Folder Guide

This file explains what every important folder means.

## Root Files

| File | Meaning |
| --- | --- |
| `README.md` | Main project explanation. Start here. |
| `LICENSE` | MIT license. People can use, copy, modify, and share the project. |
| `AUTHORS.md` | Project credit and author identity. |
| `.gitignore` | Tells Git which local files should not be uploaded. |
| `.gitattributes` | Keeps text files consistent across operating systems. |

## `skills/`

This folder contains ready-to-install AI skills.

### `skills/codex/super-memory/`

Use this if you use Codex.

Important files:

- `SKILL.md`: the instruction file Codex reads.
- `agents/openai.yaml`: display name and default prompt for Codex UI.
- `scripts/supermemory.py`: helper script for creating, reading, updating, and compressing memory.

### `skills/claude-code/supermemory/`

Use this if you use Claude Code.

Important files:

- `SKILL.md`: the instruction file Claude Code reads.
- `scripts/supermemory.py`: the same helper script, packaged with the Claude Code skill.

## `commands/`

This folder contains optional slash-command helpers.

### `commands/claude-code/supermemory.md`

Use this if you want to type commands like:

```text
/supermemory search
/supermemory update
/supermemory compress
```

The command still uses the same project memory file:

```text
.ai-handoff/SUPER_MEMORY.md
```

## `examples/`

This folder contains examples you can copy.

### `examples/SUPER_MEMORY.md`

A sample memory file. Use it when you want manual setup without installing a skill.

## `tools/`

This folder contains a standalone helper script.

### `tools/supermemory.py`

Advanced/manual users can run this directly:

```bash
python tools/supermemory.py search --root . --agent Codex
python tools/supermemory.py update --root . --agent "Claude Code" --message "Implemented login fix; tests pass."
```

The same script is also bundled inside each skill folder so users do not need to copy `tools/` separately.

## `.github/`

This folder helps people report problems or request improvements on GitHub.

It does not affect Super Memory itself.

