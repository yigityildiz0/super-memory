# super-memory

[English](super-memory.en.md) · [Türkçe](super-memory.tr.md) · [Library](../../README.tr.md)

**Uzun oturum ve farklı ajanlar arasında kısa, proje-yerel devir notları ve kanıtı korur.**

## Örnek istek

> Güncel proje devir notunu oku, durumunu dosyalarla doğrula ve sıradaki işi sürdür.

## Tetikleme ve yönlendirme

İstek, hostun skill açıklamasıyla eşleştirilir. Host destekliyorsa kanonik adla açık seçim de yapılabilir. Sohbete /ad yazmak tek başına kayıtlı bir komut yaratmaz.

<details>
<summary>Kaynak açıklamasının tam metni</summary>

Always-on project memory skill for Codex, Claude Code, ChatGPT, and other AI coding sessions. Use automatically at the start of project or coding work, before planning, to locate or create `.ai-handoff/SUPER_MEMORY.md`, read the current packet, compare agent cursors, and keep the file updated after meaningful progress. Also use for `supermemory search`, `supermemory update`, `supermemory new`, `supermemory compress`, `supermemory delete`, `supermemory status`, Super Memory, resume, continue, handoff, context window full, limit reached, switch to Claude Code, switch to Codex, new chat continuation, deleted chat recovery, teammate handoff, devam et, kaldığım yerden devam et, limit bitti, context doldu, and project memory requests.

</details>

## Çalışma mantığı

Proje hafızasını bulur; güncel paket ve yeni kontrol noktalarını okur; dosyalarla doğrular; kısa devir notunu ve ajan imlecini günceller.

Kök giriş dosyası görevi karşılar; yalnız gereken modül ve referanslar yüklenir. Betik içermesi çalıştırıldığı anlamına gelmez. Mevcut araç, veri ve kapsam doğrulandıktan sonra görev yürütülür.

## Girdi, çıktı ve doğrulama

- Girdi: örnek istekteki hedef, ilgili dosya/URL/veri ve sonucu değiştiren kısıtlar.
- Çıktı: isteğe uygun yanıt, plan, taslak veya yetkili dosya değişikliği; dayanak ve belirsizlik açık.
- Doğrulama: yapılan kontrol ile önerilen kontrol ayrı belirtilir; erişilmeyen kaynak veya çalıştırılmayan araç kullanılmış sayılmaz.

## Ortam ve sınırlar

Paket model ağırlığı, izin, hesap veya API kredisi sağlamaz. Bu sürüm mevcut host araçları, açık erişim ve yerel işlemi kullanır; ücretli servis otomatik alternatif değildir. Klinik/yatırım çıktıları profesyonel kararın veya emir işleminin yerine geçmez.

## Modüller ve kaynak

[SKILL.md](../../skills/common/super-memory/SKILL.md) · [Installation](../INSTALL.md) · [License scope](../LICENSE-SCOPE.md)

Bağımsız kök akışı; referanslar giriş dosyasında listelenir.
