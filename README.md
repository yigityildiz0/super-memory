# Super Memory

**A simple file-based memory system for Claude Code, Codex, ChatGPT, and long AI coding sessions.**

Super Memory keeps one clear project memory file inside your project, so an AI assistant can continue from the real latest state even when:

- 🧠 the chat gets too long
- 🪫 a tool limit is reached
- 🔁 you switch from Claude Code to Codex, or from Codex to Claude Code
- 💬 you start a new ChatGPT conversation
- 👥 you hand the project to a friend, teammate, or another account
- 🧩 you return to a project days later and do not remember every detail
- 🧪 tests, errors, changed files, and decisions are buried in old chats

Super Memory is not another chat log. It is a small, readable, project-local memory file that tells the next agent what matters now.

> Created by **Yigit Yildiz** - GitHub: [@yigityildiz0](https://github.com/yigityildiz0)

## Download

If you do not know GitHub, use these links:

| What you want | Download |
| --- | --- |
| Everything in one ZIP | [Download Super Memory](https://github.com/yigityildiz0/super-memory/releases/latest/download/super-memory-full.zip) |
| Codex skill only | [Download Codex Skill](https://github.com/yigityildiz0/super-memory/releases/latest/download/super-memory-codex-skill.zip) |
| Claude Code skill only | [Download Claude Code Skill](https://github.com/yigityildiz0/super-memory/releases/latest/download/super-memory-claude-code-skill.zip) |
| Source code from GitHub | [Download repository ZIP](https://github.com/yigityildiz0/super-memory/archive/refs/heads/main.zip) |

If a release download is not available yet, click the green **Code** button on GitHub, then click **Download ZIP**.

## What Super Memory Creates

Inside each project, Super Memory uses this folder:

```text
.ai-handoff/
├── SUPER_MEMORY.md   # the current project memory
└── LOG.md            # older compact milestones
```

`SUPER_MEMORY.md` is the important file. It stores:

- the current goal
- what is already done
- what files matter
- what decisions were made
- what commands/tests were run
- what failed and should not be repeated
- what the next agent should do

It does **not** store:

- private chain-of-thought
- passwords, tokens, API keys, or secrets
- huge logs
- full chat transcripts
- personal data that does not help the project

## Who Can Use It?

Super Memory is useful for more than one tool:

- **Claude Code users** who want `/supermemory search`, `/supermemory update`, and compact project handoffs.
- **Codex users** who want a project memory skill that starts by reading the latest local state.
- **ChatGPT users** who want a clean file to paste or attach in a new conversation.
- **Teams and friends** who want to transfer a project without sending a giant chat history.
- **Solo builders** who often switch accounts, devices, models, or tools.

## Quick Start For Codex

1. Download [Codex Skill](https://github.com/yigityildiz0/super-memory/releases/latest/download/super-memory-codex-skill.zip).
2. Unzip it.
3. Copy the `super-memory` folder into:

```text
~/.codex/skills/super-memory
```

On Windows, that is usually:

```text
C:\Users\YOUR_NAME\.codex\skills\super-memory
```

4. Restart Codex if the skill list does not refresh.
5. In a project, ask:

```text
supermemory search
```

or:

```text
Use Super Memory for this project.
```

## Quick Start For Claude Code

1. Download [Claude Code Skill](https://github.com/yigityildiz0/super-memory/releases/latest/download/super-memory-claude-code-skill.zip).
2. Unzip it.
3. Copy the `supermemory` folder into your Claude Code skills folder:

```text
~/.claude/skills/supermemory
```

4. Optional: copy `commands/claude-code/supermemory.md` into your Claude Code commands folder if you want a direct slash command.
5. In your project, run:

```text
/supermemory search
```

## Quick Start Without Any Skill System

You can still use Super Memory manually:

1. Create a folder named `.ai-handoff` in your project.
2. Create a file named `SUPER_MEMORY.md`.
3. Copy the structure from [examples/SUPER_MEMORY.md](examples/SUPER_MEMORY.md).
4. Tell any AI assistant:

```text
Read .ai-handoff/SUPER_MEMORY.md first, continue from it, and update it after meaningful progress.
```

This works in ChatGPT, Claude, Codex, or any tool that can read project files.

## Commands

Use these commands as natural language or slash-style prompts:

| Command | What it does |
| --- | --- |
| `supermemory search` | Finds the project memory, reads the current state, and absorbs only new entries. |
| `supermemory update` | Adds what changed: files, decisions, checks, errors, blockers, and next steps. |
| `supermemory new` | Creates memory for a project if none exists. It avoids duplicate memory files. |
| `supermemory compress` | Shrinks old history while preserving the useful current state. |
| `supermemory status` | Shows where the memory file is and what checkpoint is latest. |
| `supermemory delete` | Deletes only the `.ai-handoff` memory folder after clear intent. |

## Folder Guide

```text
super-memory/
├── README.md                         # start here
├── LICENSE                           # MIT license: free to use, modify, and share
├── AUTHORS.md                        # project credit
├── docs/
│   ├── INSTALL.md                    # slow, beginner-friendly install guide
│   ├── FOLDER_GUIDE.md               # explains every folder and file
│   └── COMMANDS.md                   # explains every command
├── skills/
│   ├── codex/super-memory/           # Codex skill package
│   └── claude-code/supermemory/      # Claude Code skill package
├── commands/
│   └── claude-code/supermemory.md    # optional Claude Code slash command
├── examples/
│   └── SUPER_MEMORY.md               # example project memory file
├── tools/
│   └── supermemory.py                # helper script for advanced/manual use
└── .github/
    └── ISSUE_TEMPLATE/               # bug and feature request templates
```

For a full beginner explanation, read [docs/FOLDER_GUIDE.md](docs/FOLDER_GUIDE.md).

## Why It Helps With Context Windows

AI tools are powerful, but context is limited. A model may forget old details, lose track after a long session, or start over when you open a new chat.

Super Memory gives the model a short source of truth:

- "Here is the goal."
- "Here is what changed."
- "Here are the risky files."
- "Here are the tests."
- "Here is what to do next."

That is enough for the next session to continue with less repeated explanation.

## Recommended Workflow

Use this at the start of a project session:

```text
supermemory search
```

Use this after meaningful progress:

```text
supermemory update
```

Use this when the file gets too long:

```text
supermemory compress
```

Use this before switching tools:

```text
Update Super Memory so I can continue in Claude Code/Codex/ChatGPT.
```

## License

Super Memory uses the **MIT License**.

That means people can use it, copy it, modify it, publish it, and use it in personal or commercial work. The license only asks that the copyright and license notice stay included.

## Not Affiliated

Super Memory is an independent open project. It is not affiliated with OpenAI, Anthropic, GitHub, Claude, Codex, ChatGPT, or Supermemory.ai.

## Feedback

If this helps your workflow, starring the repository helps more people discover it. ⭐

If you want another AI tool supported, a clearer installer, or a better memory format, open an issue.

---

# Türkçe Açıklama

**Super Memory**, uzun yapay zeka kodlama sohbetlerinde projenin nerede kaldığını kaybetmemek için hazırlanmış basit bir proje hafızası sistemidir.

Bir projede Claude Code kullanırken limit dolabilir, sonra Codex'e geçmek isteyebilirsin. Ya da Codex'te çalışırken yeni bir ChatGPT sohbetinde devam etmek isteyebilirsin. Normalde yeni yapay zeka eski sohbeti bilmez. Super Memory bunun için proje klasörünün içine küçük bir hafıza dosyası koyar.

O dosya şunu anlatır:

- proje hedefi ne
- hangi dosyalar değişti
- hangi kararlar alındı
- hangi testler çalıştı
- hangi hatalar görüldü
- sıradaki adım ne

Yani yeni sohbet, yeni hesap, farklı araç veya arkadaşın projeyi açtığında her şeyi baştan anlatmak zorunda kalmazsın.

## Türkçe Kullanım

Codex kullanıyorsan `skills/codex/super-memory` klasörünü Codex skill klasörüne koy.

Claude Code kullanıyorsan `skills/claude-code/supermemory` klasörünü Claude skill klasörüne koy.

Skill sistemi kullanmıyorsan bile projene `.ai-handoff/SUPER_MEMORY.md` dosyası koyup herhangi bir yapay zekaya şunu diyebilirsin:

```text
Önce .ai-handoff/SUPER_MEMORY.md dosyasını oku, kaldığım yerden devam et ve önemli ilerlemelerde bu dosyayı güncelle.
```

Bu kadar.

