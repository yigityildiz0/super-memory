#!/usr/bin/env python3
"""Super Memory helper.

Maintains .ai-handoff/SUPER_MEMORY.md without storing transcripts or secrets.
"""

from __future__ import annotations

import argparse
import re
import shutil
from datetime import datetime, timezone
from pathlib import Path

MEMORY_DIR = ".ai-handoff"
MEMORY_FILE = "SUPER_MEMORY.md"
LEGACY_FILES = ("SUPERMEMORY.md", "HANDOFF.md")
LOG_FILE = "LOG.md"
AGENTS = ("Codex", "Claude Code", "ChatGPT", "Other")


def now_iso() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def checkpoint_id() -> str:
    return datetime.now(timezone.utc).strftime("cp-%Y%m%dT%H%M%S%fZ")


def normalize_agent(agent: str) -> str:
    cleaned = (agent or "").strip().lower()
    aliases = {
        "codex": "Codex",
        "chatgpt codex": "Codex",
        "claude": "Claude Code",
        "claude code": "Claude Code",
        "chatgpt": "ChatGPT",
        "gpt": "ChatGPT",
    }
    return aliases.get(cleaned, agent.strip() if agent else "Other")


def resolve_root(raw_root: str | None) -> Path:
    start = Path(raw_root or ".").resolve()
    if start.is_file():
        start = start.parent

    if (start / MEMORY_DIR / MEMORY_FILE).exists():
        return start
    if any((start / MEMORY_DIR / legacy).exists() for legacy in LEGACY_FILES):
        return start
    if (start / ".git").exists():
        return start
    if (start / "package.json").exists() or (start / "pyproject.toml").exists() or (start / "Cargo.toml").exists():
        return start

    cur = start
    while True:
        if (cur / MEMORY_DIR / MEMORY_FILE).exists():
            return cur
        if any((cur / MEMORY_DIR / legacy).exists() for legacy in LEGACY_FILES):
            return cur
        if cur.parent == cur:
            break
        cur = cur.parent

    cur = start
    while True:
        if (cur / ".git").exists():
            return cur
        if (cur / "package.json").exists() or (cur / "pyproject.toml").exists() or (cur / "Cargo.toml").exists():
            return cur
        if cur.parent == cur:
            return start
        cur = cur.parent


def paths(root: Path) -> tuple[Path, Path, Path]:
    mem_dir = root / MEMORY_DIR
    return mem_dir, mem_dir / MEMORY_FILE, mem_dir / LOG_FILE


def template(root: Path, agent: str) -> str:
    cp = checkpoint_id()
    cursor_lines = "\n".join(f"- {name} last-read: {'none' if name != agent else cp}" for name in AGENTS)
    return f"""# Super Memory

Last updated: {now_iso()}
Updated by: {agent}
Project root: {root}
Mode: compact

## Current Packet
- Goal: Unset. Replace with the current objective.
- State: Super Memory initialized; no project work recorded yet.
- Active files: none
- Decisions: none
- Verification: none
- Blockers: none
- Next: Define the first concrete action.

## Agent Cursors
{cursor_lines}

## Timeline
- {cp} | {agent} | Initialized Super Memory for this project.
"""


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8") if path.exists() else ""


def write_text(path: Path, text: str) -> None:
    path.write_text(text, encoding="utf-8", newline="\n")


def migrate_legacy(root: Path, agent: str) -> None:
    mem_dir, mem_path, log_path = paths(root)
    if mem_path.exists():
        return
    for legacy_name in LEGACY_FILES:
        legacy_path = mem_dir / legacy_name
        if legacy_path.exists():
            legacy_text = read_text(legacy_path)
            cp = checkpoint_id()
            migrated = f"""# Super Memory

Last updated: {now_iso()}
Updated by: {agent}
Project root: {root}
Mode: compact

## Current Packet
- Goal: Migrated from `{legacy_name}`. Review and tighten this packet.
- State: Legacy memory imported into Super Memory.
- Active files: see imported legacy section below.
- Decisions: keep one canonical file at `.ai-handoff/{MEMORY_FILE}`.
- Verification: migration completed by helper script.
- Blockers: none
- Next: review imported facts, remove stale detail, continue work.

## Agent Cursors
""" + "\n".join(f"- {name} last-read: {'none' if name != agent else cp}" for name in AGENTS) + f"""

## Timeline
- {cp} | {agent} | Migrated legacy `{legacy_name}` into `{MEMORY_FILE}`.

## Imported Legacy Notes

```markdown
{legacy_text.strip()}
```
"""
            write_text(mem_path, migrated)
            if not log_path.exists():
                write_text(log_path, f"# Super Memory Log\n\nCreated: {now_iso()}\n")
            return


def ensure(root: Path, agent: str) -> Path:
    mem_dir, mem_path, log_path = paths(root)
    mem_dir.mkdir(parents=True, exist_ok=True)
    migrate_legacy(root, agent)
    if not mem_path.exists():
        write_text(mem_path, template(root, agent))
    if not log_path.exists():
        write_text(log_path, f"# Super Memory Log\n\nCreated: {now_iso()}\n")
    return mem_path


def checkpoint_ids(text: str) -> list[str]:
    return re.findall(r"\bcp-\d{8}T\d{6}(?:\d{3,6})?Z\b", text)


def latest_checkpoint(text: str) -> str:
    ids = []
    for line in timeline_lines(text):
        ids.extend(checkpoint_ids(line))
    return ids[-1] if ids else "none"


def get_cursor(text: str, agent: str) -> str:
    pattern = rf"^- {re.escape(agent)} last-read: (.+)$"
    match = re.search(pattern, text, flags=re.MULTILINE)
    return match.group(1).strip() if match else "none"


def set_cursor(text: str, agent: str, cp: str) -> str:
    line = f"- {agent} last-read: {cp}"
    pattern = rf"^- {re.escape(agent)} last-read: .+$"
    if re.search(pattern, text, flags=re.MULTILINE):
        return re.sub(pattern, line, text, flags=re.MULTILINE)
    marker = "## Agent Cursors\n"
    if marker in text:
        return text.replace(marker, marker + line + "\n", 1)
    return text.rstrip() + "\n\n## Agent Cursors\n" + line + "\n"


def touch(text: str, agent: str) -> str:
    text = re.sub(r"^Last updated: .+$", f"Last updated: {now_iso()}", text, flags=re.MULTILINE)
    text = re.sub(r"^Updated by: .+$", f"Updated by: {agent}", text, flags=re.MULTILINE)
    return text


def current_packet(text: str) -> str:
    match = re.search(r"## Current Packet\n(.*?)(?=\n## |\Z)", text, flags=re.S)
    return match.group(1).strip() if match else ""


def timeline_lines(text: str) -> list[str]:
    match = re.search(r"## Timeline\n(.*?)(?=\n## |\Z)", text, flags=re.S)
    if not match:
        return []
    return [line.rstrip() for line in match.group(1).splitlines() if line.strip().startswith("- cp-")]


def lines_after_cursor(lines: list[str], cursor: str) -> list[str]:
    if cursor == "none":
        return lines[-10:]
    index = -1
    for i, line in enumerate(lines):
        if cursor in line:
            index = i
    return lines[index + 1 :] if index >= 0 else lines[-10:]


def append_checkpoint(text: str, agent: str, message: str) -> tuple[str, str]:
    cp = checkpoint_id()
    compact = " ".join((message or "Updated project state.").split())
    line = f"- {cp} | {agent} | {compact}"
    if "## Timeline\n" not in text:
        text = text.rstrip() + "\n\n## Timeline\n" + line + "\n"
    else:
        def add_to_timeline(match: re.Match[str]) -> str:
            body = match.group(1).rstrip()
            return "## Timeline\n" + body + "\n" + line + "\n"

        text = re.sub(r"## Timeline\n(.*?)(?=\n## |\Z)", add_to_timeline, text, count=1, flags=re.S)
    text = set_cursor(touch(text, agent), agent, cp)
    return text, cp


def cmd_new(args: argparse.Namespace) -> None:
    root = resolve_root(args.root)
    agent = normalize_agent(args.agent)
    mem_dir, mem_path, _ = paths(root)
    if mem_path.exists() and not args.force:
        print(f"Existing memory found: {mem_path}")
        print("No second memory created. Use update/search, or pass --force to archive and recreate.")
        return
    if mem_path.exists() and args.force:
        archive = mem_dir / f"SUPER_MEMORY.archive.{datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%SZ')}.md"
        shutil.move(str(mem_path), str(archive))
        print(f"Archived old memory: {archive}")
    ensure(root, agent)
    print(f"Memory ready: {mem_path}")


def cmd_status(args: argparse.Namespace) -> None:
    root = resolve_root(args.root)
    _, mem_path, log_path = paths(root)
    if not mem_path.exists():
        print(f"Missing: {mem_path}")
        return
    text = read_text(mem_path)
    print(f"Memory: {mem_path}")
    print(f"Log: {log_path}")
    print(f"Latest checkpoint: {latest_checkpoint(text)}")
    for agent in AGENTS:
        print(f"{agent} cursor: {get_cursor(text, agent)}")


def cmd_search(args: argparse.Namespace) -> None:
    root = resolve_root(args.root)
    agent = normalize_agent(args.agent)
    mem_path = ensure(root, agent)
    text = read_text(mem_path)
    cursor = get_cursor(text, agent)
    lines = timeline_lines(text)
    unseen = lines_after_cursor(lines, cursor)
    last = latest_checkpoint(text)
    print(f"Memory: {mem_path}")
    print(f"Agent: {agent}")
    print(f"Cursor before: {cursor}")
    print("\n## Current Packet\n")
    print(current_packet(text) or "(empty)")
    print("\n## New Timeline Entries\n")
    print("\n".join(unseen) if unseen else "(none)")
    if args.mark_read and last != "none":
        text = set_cursor(touch(text, agent), agent, last)
        write_text(mem_path, text)
        print(f"\nCursor updated: {agent} -> {last}")


def cmd_update(args: argparse.Namespace) -> None:
    root = resolve_root(args.root)
    agent = normalize_agent(args.agent)
    mem_path = ensure(root, agent)
    text, cp = append_checkpoint(read_text(mem_path), agent, args.message)
    write_text(mem_path, text)
    print(f"Appended {cp} to {mem_path}")


def cmd_compress(args: argparse.Namespace) -> None:
    root = resolve_root(args.root)
    agent = normalize_agent(args.agent)
    mem_path = ensure(root, agent)
    _, _, log_path = paths(root)
    text = read_text(mem_path)
    lines = timeline_lines(text)
    keep = max(1, args.keep)
    if len(lines) <= keep:
        print(f"No compression needed. Timeline entries: {len(lines)}")
        return
    old, kept = lines[:-keep], lines[-keep:]
    archive_block = "\n\n" + f"## Compressed {now_iso()} by {agent}\n" + "\n".join(old) + "\n"
    with log_path.open("a", encoding="utf-8", newline="\n") as fh:
        fh.write(archive_block)
    text = re.sub(r"## Timeline\n.*?(?=\n## |\Z)", "## Timeline\n" + "\n".join(kept) + "\n", text, flags=re.S)
    text = touch(text, agent)
    write_text(mem_path, text)
    print(f"Compressed {len(old)} old entries into {log_path}")
    print(f"Kept {len(kept)} latest entries in {mem_path}")


def cmd_delete(args: argparse.Namespace) -> None:
    root = resolve_root(args.root)
    mem_dir, _, _ = paths(root)
    if not mem_dir.exists():
        print(f"Nothing to delete: {mem_dir}")
        return
    if not args.yes:
        print(f"Refusing to delete without --yes: {mem_dir}")
        return
    shutil.rmtree(mem_dir)
    print(f"Deleted only memory folder: {mem_dir}")


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Super Memory helper")
    sub = parser.add_subparsers(dest="command", required=True)

    def add_common(p: argparse.ArgumentParser) -> None:
        p.add_argument("--root", default=".", help="Project root or file inside the project")
        p.add_argument("--agent", default="Codex", help="Codex, Claude Code, ChatGPT, or Other")

    p_new = sub.add_parser("new", help="Create memory if missing")
    add_common(p_new)
    p_new.add_argument("--force", action="store_true", help="Archive existing memory and create a new one")
    p_new.set_defaults(func=cmd_new)

    p_status = sub.add_parser("status", help="Show memory status")
    p_status.add_argument("--root", default=".")
    p_status.set_defaults(func=cmd_status)

    p_search = sub.add_parser("search", help="Read current packet and new entries")
    add_common(p_search)
    p_search.add_argument("--mark-read", action=argparse.BooleanOptionalAction, default=True)
    p_search.set_defaults(func=cmd_search)

    p_update = sub.add_parser("update", help="Append compact checkpoint")
    add_common(p_update)
    p_update.add_argument("--message", required=True, help="Compact update message")
    p_update.set_defaults(func=cmd_update)

    p_compress = sub.add_parser("compress", help="Move old timeline entries into LOG.md")
    add_common(p_compress)
    p_compress.add_argument("--keep", type=int, default=20, help="Timeline entries to keep")
    p_compress.set_defaults(func=cmd_compress)

    p_delete = sub.add_parser("delete", help="Delete only .ai-handoff")
    p_delete.add_argument("--root", default=".")
    p_delete.add_argument("--yes", action="store_true")
    p_delete.set_defaults(func=cmd_delete)

    return parser


def main() -> None:
    parser = build_parser()
    args = parser.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
