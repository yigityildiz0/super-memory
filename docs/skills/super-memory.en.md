# super-memory

[English](super-memory.en.md) · [Türkçe](super-memory.tr.md) · [Library](../../README.md)

**Keep compact, project-local handoffs and evidence across long sessions and different agents.**

## Try it

> Read the current project handoff, verify its state and continue the next unfinished task.

## Trigger and routing

The host matches the request against the skill description. Explicit selection by canonical name is available where supported. Typing /name in chat does not register a command.

<details>
<summary>Exact source description</summary>

Always-on project memory skill for Codex, Claude Code, ChatGPT, and other AI coding sessions. Use automatically at the start of project or coding work, before planning, to locate or create `.ai-handoff/SUPER_MEMORY.md`, read the current packet, compare agent cursors, and keep the file updated after meaningful progress. Also use for `supermemory search`, `supermemory update`, `supermemory new`, `supermemory compress`, `supermemory delete`, `supermemory status`, Super Memory, resume, continue, handoff, context window full, limit reached, switch to Claude Code, switch to Codex, new chat continuation, deleted chat recovery, teammate handoff, devam et, kaldığım yerden devam et, limit bitti, context doldu, and project memory requests.

</details>

## How it works

Locate the project memory; read the current packet and newer checkpoints; verify against files; update a compact handoff and agent cursor.

The root entry point owns routing; only relevant modules and references are loaded. A bundled script is not an executed result. Work uses actual host tools, available input and the task scope.

## Inputs, outputs and verification

- Input: the example goal, relevant files/URLs/data, and constraints that change the result.
- Output: a task-appropriate answer, plan, draft or authorized file change with evidence and uncertainty.
- Verification: performed and suggested checks are separate; inaccessible sources and unexecuted tools are not counted as used.

## Runtime and boundaries

The package supplies no model weights, permissions, account or API credit. This edition uses existing host tools, open access and local computation; a separately billed service is not an automatic fallback. Clinical/investment outputs do not replace professional judgment or execute orders.

## Modules and source

[SKILL.md](../../skills/common/super-memory/SKILL.md) · [Installation](../INSTALL.md) · [License scope](../LICENSE-SCOPE.md)

Standalone root workflow; references are linked by the entry point.
