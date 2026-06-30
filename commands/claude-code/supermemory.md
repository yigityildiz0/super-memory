Use Super Memory for this project.

Arguments: `$ARGUMENTS`

Interpret the first argument as the action:

- `search`: read `.ai-handoff/SUPER_MEMORY.md`, absorb `Current Packet`, then read only timeline entries newer than the Claude Code cursor.
- `update`: refresh the current packet and append a compact checkpoint describing the work just completed.
- `new`: create `.ai-handoff/SUPER_MEMORY.md` if missing; if one exists, do not create a duplicate.
- `compress`: shrink old timeline detail while preserving current goal, files, decisions, verification, blockers, and next actions.
- `delete`: delete only `.ai-handoff/` after explicit confirmation of the project root.
- `status`: report the memory path, latest checkpoint, cursors, and next step.

If no action is provided, run `search`.

Use the installed `supermemory` skill rules. If the helper exists, prefer:

```bash
python ~/.claude/skills/supermemory/scripts/supermemory.py <action> --root . --agent "Claude Code"
```

For `update`, include the remaining arguments as a dense message:

```bash
python ~/.claude/skills/supermemory/scripts/supermemory.py update --root . --agent "Claude Code" --message "<compact update>"
```

Never store private chain-of-thought, secrets, full transcripts, or huge logs.

