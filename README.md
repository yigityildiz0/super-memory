# Super Memory

**A simple file-based project memory system for Claude Code, Codex, ChatGPT, and long AI coding sessions.**

Super Memory helps an AI assistant continue from the real latest state of a project, even when the original chat is too long, deleted, limited, or moved to another AI tool.

Languages:

- [English](#english)
- [Türkçe](#türkçe)

> Created by **Yigit Yildiz** - GitHub: [@yigityildiz0](https://github.com/yigityildiz0)

---

# English

## What Is Super Memory?

Super Memory is a small project-memory system.

It creates one clear memory file inside your project. That file explains what the project is, what changed, what failed, what was decided, and what should happen next.

The goal is simple:

> A new AI assistant should be able to open your project, read one memory file, and continue without you explaining everything again.

Super Memory is useful when you work with:

- Claude Code
- Codex
- ChatGPT
- another AI coding assistant
- a second account
- a teammate or friend
- a new chat after the old chat became too long

It is not a database. It is not a complicated app. It is not a full transcript. It is a clean handoff note for the project.

## Why You Might Need It

AI coding sessions often break because the useful context is trapped in a chat.

Common problems:

- 🧠 The chat gets too long.
- 🪫 A Claude Code, Codex, or ChatGPT limit is reached.
- 🔁 You switch from Claude Code to Codex, or from Codex to Claude Code.
- 💬 You start a new ChatGPT conversation.
- 🗑️ A chat is deleted or lost.
- 👥 You want to send the project to a friend or teammate.
- 🔐 You continue from another account.
- 🧩 You return to a project days later and forget what happened.
- 🧪 Test results, bugs, failed attempts, and decisions are buried in old messages.

Super Memory solves this by keeping the useful project state in the project itself.

## Download

If you do not know GitHub, use the links below.

Click the link you need, download the ZIP file, then extract/unzip it like a normal folder.

| What you want | Download |
| --- | --- |
| Everything in one ZIP | [Download Super Memory](https://github.com/yigityildiz0/super-memory/releases/latest/download/super-memory-full.zip) |
| Codex skill only | [Download Codex Skill](https://github.com/yigityildiz0/super-memory/releases/latest/download/super-memory-codex-skill.zip) |
| Claude Code skill only | [Download Claude Code Skill](https://github.com/yigityildiz0/super-memory/releases/latest/download/super-memory-claude-code-skill.zip) |
| Source code from GitHub | [Download repository ZIP](https://github.com/yigityildiz0/super-memory/archive/refs/heads/main.zip) |

If a release download is not available, open the GitHub page, click the green **Code** button, then click **Download ZIP**.

## Which Download Should I Choose?

| If you use... | Choose this |
| --- | --- |
| Only Codex | `super-memory-codex-skill.zip` |
| Only Claude Code | `super-memory-claude-code-skill.zip` |
| Both Codex and Claude Code | `super-memory-full.zip` |
| ChatGPT without local skills | `super-memory-full.zip`, then use `examples/SUPER_MEMORY.md` manually |
| You are not sure | `super-memory-full.zip` |

If you are a complete beginner, download **Everything in one ZIP**. It contains all files and examples.

## What Super Memory Creates

Inside your project, Super Memory uses this folder:

```text
.ai-handoff/
├── SUPER_MEMORY.md   # the current project memory
└── LOG.md            # older compact milestones
```

`SUPER_MEMORY.md` is the important file.

It stores:

- current project goal
- what is already done
- what files matter
- what decisions were made
- what commands or tests were run
- what failed and should not be repeated
- current blockers
- next steps
- short notes for the next AI assistant

It does **not** store:

- private chain-of-thought
- full chat transcripts
- passwords
- API keys
- tokens
- secret files
- huge logs
- unrelated personal information

## Who Can Use It?

Super Memory is useful for many workflows.

### Claude Code Users

Use it when you want Claude Code to remember project state across sessions.

Example:

```text
/supermemory search
```

### Codex Users

Use it when you want Codex to read the latest project state before planning or editing files.

Example:

```text
supermemory search
```

### ChatGPT Users

Use it when you start a new ChatGPT conversation and want to continue an old project.

You can attach or paste `.ai-handoff/SUPER_MEMORY.md` and say:

```text
Read this Super Memory file first, then continue from the latest state.
```

### Teams, Friends, And Second Accounts

Use it when somebody else needs to understand your project without reading a giant chat history.

Send them the project folder and tell them to read:

```text
.ai-handoff/SUPER_MEMORY.md
```

## Quick Start For Codex

1. Download [Codex Skill](https://github.com/yigityildiz0/super-memory/releases/latest/download/super-memory-codex-skill.zip).
2. Extract/unzip the downloaded file.
3. You will see a folder named `super-memory`.
4. Copy that `super-memory` folder into:

```text
~/.codex/skills/super-memory
```

On Windows, the folder is usually:

```text
C:\Users\YOUR_NAME\.codex\skills\super-memory
```

5. Restart Codex if the skill list does not refresh.
6. Open a project.
7. Ask Codex:

```text
supermemory search
```

or:

```text
Use Super Memory for this project.
```

## Quick Start For Claude Code

1. Download [Claude Code Skill](https://github.com/yigityildiz0/super-memory/releases/latest/download/super-memory-claude-code-skill.zip).
2. Extract/unzip the downloaded file.
3. You will see a folder named `supermemory`.
4. Copy that `supermemory` folder into your Claude Code skills folder:

```text
~/.claude/skills/supermemory
```

5. Optional: copy this file into your Claude Code commands folder if you want a direct slash command:

```text
commands/claude-code/supermemory.md
```

6. Open a project.
7. Run:

```text
/supermemory search
```

## Quick Start Without Any Skill System

You can use Super Memory even without installing a skill.

1. Open your project folder.
2. Create a folder named `.ai-handoff`.
3. Inside it, create a file named `SUPER_MEMORY.md`.
4. Copy the structure from [examples/SUPER_MEMORY.md](examples/SUPER_MEMORY.md).
5. Tell any AI assistant:

```text
Read .ai-handoff/SUPER_MEMORY.md first, continue from it, and update it after meaningful progress.
```

This works in ChatGPT, Claude, Codex, and any assistant that can read project files.

## Commands

Use these commands as plain language or slash-style prompts.

| Command | What it does |
| --- | --- |
| `supermemory search` | Finds the project memory, reads the current state, and absorbs only new entries. |
| `supermemory update` | Adds what changed: files, decisions, checks, errors, blockers, and next steps. |
| `supermemory new` | Creates memory for a project if none exists. It avoids duplicate memory files. |
| `supermemory compress` | Shrinks old history while preserving the useful current state. |
| `supermemory status` | Shows where the memory file is and what checkpoint is latest. |
| `supermemory delete` | Deletes only the `.ai-handoff` memory folder after clear intent. |

## Folder Guide

When you download the full project, you will see this structure:

```text
super-memory/
├── README.md                         # start here
├── LICENSE                           # MIT license: free to use, modify, and share
├── AUTHORS.md                        # project credit
├── docs/
│   ├── INSTALL.md                    # beginner-friendly install guide
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

For a slower explanation of every folder, read [docs/FOLDER_GUIDE.md](docs/FOLDER_GUIDE.md).

## Why It Helps With Context Windows

AI tools are powerful, but they do not have unlimited context.

After a long session, an assistant may lose track of:

- the original goal
- changed files
- failed attempts
- test results
- user preferences
- next steps

Super Memory gives the next session a short source of truth:

- "Here is the goal."
- "Here is what changed."
- "Here are the risky files."
- "Here are the tests."
- "Here is what to do next."

That is usually enough to continue without repeating the whole conversation.

## Recommended Workflow

At the start of a project session:

```text
supermemory search
```

After meaningful progress:

```text
supermemory update
```

When the memory file becomes too long:

```text
supermemory compress
```

Before switching tools:

```text
Update Super Memory so I can continue in Claude Code/Codex/ChatGPT.
```

Before sending the project to another person:

```text
Update Super Memory so another person can understand the current state.
```

## Privacy And Safety

Super Memory is meant to store project facts, not private secrets.

Do not put these into `SUPER_MEMORY.md`:

- passwords
- API keys
- tokens
- private credentials
- personal messages
- full logs with sensitive data

Keep it practical and safe.

## License

Super Memory uses the **MIT License**.

That means people can use it, copy it, modify it, publish it, and use it in personal or commercial work.

The license only asks that the copyright and license notice stay included.

## Not Affiliated

Super Memory is an independent open project.

It is not affiliated with OpenAI, Anthropic, GitHub, Claude, Codex, ChatGPT, or Supermemory.ai.

## Feedback

If Super Memory helps your workflow, starring the repository helps more people discover it. ⭐

If you want another AI tool supported, a clearer installer, or a better memory format, open an issue.

---

# Türkçe

## Super Memory Nedir?

Super Memory küçük bir proje hafızası sistemidir.

Projenin içine tek ve net bir hafıza dosyası koyar. Bu dosya projenin ne olduğunu, neyin değiştiğini, neyin hata verdiğini, hangi kararların alındığını ve sırada ne yapılması gerektiğini anlatır.

Amaç basit:

> Yeni bir yapay zeka asistanı projeyi açsın, tek bir hafıza dosyasını okusun ve sen her şeyi tekrar anlatmadan kaldığı yerden devam edebilsin.

Super Memory şunlarla çalışırken işe yarar:

- Claude Code
- Codex
- ChatGPT
- başka bir yapay zeka kodlama asistanı
- ikinci bir hesap
- takım arkadaşı veya arkadaş
- eski sohbet çok uzadığı için açılan yeni sohbet

Bu bir veritabanı değildir. Karmaşık bir uygulama değildir. Tam sohbet dökümü değildir. Proje için temiz bir devir notudur.

## Neden Gerekebilir?

Yapay zeka ile kod yazarken işe yarayan bilgiler çoğu zaman sohbetin içinde sıkışıp kalır.

Sık görülen sorunlar:

- 🧠 Sohbet çok uzar.
- 🪫 Claude Code, Codex veya ChatGPT limiti dolar.
- 🔁 Claude Code'dan Codex'e veya Codex'ten Claude Code'a geçersin.
- 💬 Yeni bir ChatGPT sohbeti açarsın.
- 🗑️ Sohbet silinir veya kaybolur.
- 👥 Projeyi bir arkadaşına veya takım arkadaşına göndermek istersin.
- 🔐 Başka bir hesaptan devam edersin.
- 🧩 Projeye günler sonra dönersin ve ne olduğunu hatırlamazsın.
- 🧪 Test sonuçları, hatalar, başarısız denemeler ve kararlar eski mesajların içinde kalır.

Super Memory bunu, işe yarayan proje durumunu projenin kendi içine kaydederek çözer.

## İndirme

GitHub bilmiyorsan aşağıdaki linkleri kullan.

İhtiyacın olan linke tıkla, ZIP dosyasını indir, sonra normal bir klasör gibi çıkar/aç.

| Ne istiyorsun? | İndir |
| --- | --- |
| Her şey tek ZIP içinde | [Super Memory İndir](https://github.com/yigityildiz0/super-memory/releases/latest/download/super-memory-full.zip) |
| Sadece Codex skill | [Codex Skill İndir](https://github.com/yigityildiz0/super-memory/releases/latest/download/super-memory-codex-skill.zip) |
| Sadece Claude Code skill | [Claude Code Skill İndir](https://github.com/yigityildiz0/super-memory/releases/latest/download/super-memory-claude-code-skill.zip) |
| GitHub kaynak kodu | [Repository ZIP İndir](https://github.com/yigityildiz0/super-memory/archive/refs/heads/main.zip) |

Release indirmesi çalışmazsa GitHub sayfasını aç, yeşil **Code** düğmesine tıkla, sonra **Download ZIP** seçeneğine tıkla.

## Hangi İndirmeyi Seçmeliyim?

| Eğer bunu kullanıyorsan... | Bunu seç |
| --- | --- |
| Sadece Codex | `super-memory-codex-skill.zip` |
| Sadece Claude Code | `super-memory-claude-code-skill.zip` |
| Hem Codex hem Claude Code | `super-memory-full.zip` |
| Local skill kullanmadan ChatGPT | `super-memory-full.zip`, sonra `examples/SUPER_MEMORY.md` dosyasını manuel kullan |
| Emin değilsen | `super-memory-full.zip` |

Tamamen yeniysen **Her şey tek ZIP içinde** seçeneğini indir. İçinde bütün dosyalar ve örnekler vardır.

## Super Memory Ne Oluşturur?

Super Memory projenin içinde şu klasörü kullanır:

```text
.ai-handoff/
├── SUPER_MEMORY.md   # mevcut proje hafızası
└── LOG.md            # eski kısa kilometre taşları
```

`SUPER_MEMORY.md` önemli dosyadır.

Şunları kaydeder:

- mevcut proje hedefi
- şu ana kadar ne yapıldı
- hangi dosyalar önemli
- hangi kararlar alındı
- hangi komutlar veya testler çalıştırıldı
- hangi şeyler hata verdi ve tekrar denenmemeli
- mevcut engeller
- sıradaki adımlar
- sonraki yapay zeka asistanı için kısa notlar

Şunları kaydetmez:

- gizli düşünce zinciri
- tam sohbet dökümleri
- şifreler
- API anahtarları
- tokenlar
- gizli dosyalar
- devasa loglar
- projeye yardımcı olmayan kişisel bilgiler

## Kimler Kullanabilir?

Super Memory birçok farklı iş akışı için kullanılabilir.

### Claude Code Kullanıcıları

Claude Code'un proje durumunu oturumlar arasında hatırlamasını istiyorsan kullan.

Örnek:

```text
/supermemory search
```

### Codex Kullanıcıları

Codex'in planlama veya dosya düzenleme yapmadan önce son proje durumunu okumasını istiyorsan kullan.

Örnek:

```text
supermemory search
```

### ChatGPT Kullanıcıları

Yeni bir ChatGPT sohbeti açıp eski bir projeden devam etmek istiyorsan kullan.

`.ai-handoff/SUPER_MEMORY.md` dosyasını ekleyebilir veya içeriğini yapıştırıp şöyle diyebilirsin:

```text
Önce bu Super Memory dosyasını oku, sonra son durumdan devam et.
```

### Takımlar, Arkadaşlar Ve İkinci Hesaplar

Başka biri devasa sohbet geçmişini okumadan projeni anlamak zorundaysa kullan.

O kişiye proje klasörünü gönder ve şu dosyayı okumasını söyle:

```text
.ai-handoff/SUPER_MEMORY.md
```

## Codex İçin Hızlı Başlangıç

1. [Codex Skill](https://github.com/yigityildiz0/super-memory/releases/latest/download/super-memory-codex-skill.zip) dosyasını indir.
2. İndirilen dosyayı çıkar/aç.
3. `super-memory` adlı bir klasör göreceksin.
4. Bu `super-memory` klasörünü şuraya kopyala:

```text
~/.codex/skills/super-memory
```

Windows'ta klasör genelde şudur:

```text
C:\Users\YOUR_NAME\.codex\skills\super-memory
```

5. Skill listesi yenilenmezse Codex'i yeniden başlat.
6. Bir proje aç.
7. Codex'e şunu yaz:

```text
supermemory search
```

veya:

```text
Use Super Memory for this project.
```

## Claude Code İçin Hızlı Başlangıç

1. [Claude Code Skill](https://github.com/yigityildiz0/super-memory/releases/latest/download/super-memory-claude-code-skill.zip) dosyasını indir.
2. İndirilen dosyayı çıkar/aç.
3. `supermemory` adlı bir klasör göreceksin.
4. Bu `supermemory` klasörünü Claude Code skills klasörüne kopyala:

```text
~/.claude/skills/supermemory
```

5. İsteğe bağlı: doğrudan slash komutu istiyorsan şu dosyayı Claude Code commands klasörüne kopyala:

```text
commands/claude-code/supermemory.md
```

6. Bir proje aç.
7. Şunu çalıştır:

```text
/supermemory search
```

## Skill Sistemi Olmadan Hızlı Başlangıç

Super Memory'yi skill kurmadan da kullanabilirsin.

1. Proje klasörünü aç.
2. `.ai-handoff` adlı bir klasör oluştur.
3. Bu klasörün içinde `SUPER_MEMORY.md` adlı bir dosya oluştur.
4. [examples/SUPER_MEMORY.md](examples/SUPER_MEMORY.md) dosyasındaki yapıyı kopyala.
5. Herhangi bir yapay zeka asistanına şunu söyle:

```text
Önce .ai-handoff/SUPER_MEMORY.md dosyasını oku, buradan devam et ve anlamlı ilerlemelerden sonra dosyayı güncelle.
```

Bu yöntem ChatGPT, Claude, Codex ve proje dosyası okuyabilen herhangi bir asistanla çalışır.

## Komutlar

Bu komutları düz yazı olarak veya slash komutu gibi kullanabilirsin.

| Komut | Ne yapar? |
| --- | --- |
| `supermemory search` | Proje hafızasını bulur, mevcut durumu okur ve sadece yeni girişleri alır. |
| `supermemory update` | Değişen dosyaları, kararları, kontrolleri, hataları, engelleri ve sıradaki adımları ekler. |
| `supermemory new` | Projede hafıza yoksa oluşturur. Aynı projede çift hafıza dosyası oluşmasını önler. |
| `supermemory compress` | Eski geçmişi kısaltır ama işe yarayan mevcut durumu korur. |
| `supermemory status` | Hafıza dosyasının nerede olduğunu ve en son checkpoint bilgisini gösterir. |
| `supermemory delete` | Açık niyet varsa sadece `.ai-handoff` hafıza klasörünü siler. |

## Klasör Rehberi

Tam projeyi indirdiğinde şu yapıyı görürsün:

```text
super-memory/
├── README.md                         # buradan başla
├── LICENSE                           # MIT lisansı: kullanmak, değiştirmek ve paylaşmak serbest
├── AUTHORS.md                        # proje sahibi bilgisi
├── docs/
│   ├── INSTALL.md                    # yeni başlayanlar için kurulum rehberi
│   ├── FOLDER_GUIDE.md               # her klasör ve dosyayı açıklar
│   └── COMMANDS.md                   # her komutu açıklar
├── skills/
│   ├── codex/super-memory/           # Codex skill paketi
│   └── claude-code/supermemory/      # Claude Code skill paketi
├── commands/
│   └── claude-code/supermemory.md    # isteğe bağlı Claude Code slash komutu
├── examples/
│   └── SUPER_MEMORY.md               # örnek proje hafızası dosyası
├── tools/
│   └── supermemory.py                # ileri/manuel kullanım için yardımcı script
└── .github/
    └── ISSUE_TEMPLATE/               # hata ve özellik isteği şablonları
```

Her klasörün daha yavaş ve ayrıntılı açıklaması için [docs/FOLDER_GUIDE.md](docs/FOLDER_GUIDE.md) dosyasını oku.

## Context Window Sorununa Nasıl Yardımcı Olur?

Yapay zeka araçları güçlüdür ama sınırsız context'e sahip değildir.

Uzun bir oturumdan sonra asistan şunları kaybedebilir:

- asıl hedef
- değişen dosyalar
- başarısız denemeler
- test sonuçları
- kullanıcı tercihleri
- sıradaki adımlar

Super Memory sonraki oturuma kısa bir gerçek kaynak verir:

- "Hedef bu."
- "Bunlar değişti."
- "Riskli dosyalar bunlar."
- "Testler bunlar."
- "Sırada bu var."

Bu genelde bütün konuşmayı tekrar anlatmadan devam etmek için yeterlidir.

## Önerilen İş Akışı

Proje oturumunun başında:

```text
supermemory search
```

Anlamlı ilerlemeden sonra:

```text
supermemory update
```

Hafıza dosyası çok uzadığında:

```text
supermemory compress
```

Başka araca geçmeden önce:

```text
Update Super Memory so I can continue in Claude Code/Codex/ChatGPT.
```

Projeyi başka birine göndermeden önce:

```text
Update Super Memory so another person can understand the current state.
```

## Gizlilik Ve Güvenlik

Super Memory proje gerçeklerini saklamak içindir, özel sırları saklamak için değildir.

`SUPER_MEMORY.md` içine şunları koyma:

- şifreler
- API anahtarları
- tokenlar
- özel giriş bilgileri
- kişisel mesajlar
- hassas veri içeren tam loglar

Dosyayı pratik ve güvenli tut.

## Lisans

Super Memory **MIT Lisansı** kullanır.

Bu, insanların projeyi kullanabileceği, kopyalayabileceği, değiştirebileceği, yayınlayabileceği ve kişisel ya da ticari işlerde kullanabileceği anlamına gelir.

Lisans sadece telif ve lisans bilgisinin dosyada kalmasını ister.

## Bağlantılı Değildir

Super Memory bağımsız ve açık bir projedir.

OpenAI, Anthropic, GitHub, Claude, Codex, ChatGPT veya Supermemory.ai ile bağlantılı değildir.

## Geri Bildirim

Super Memory iş akışına yardımcı olursa repoya yıldız vermen daha fazla kişinin keşfetmesine yardımcı olur. ⭐

Başka bir yapay zeka aracı desteği, daha açık bir kurulum veya daha iyi bir hafıza biçimi istiyorsan issue açabilirsin.

