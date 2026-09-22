# tugaysahn / TS-utas

**Yazar:** Tugay Şahin  
**Telif:** © 2024–2026 Tugay Şahin. Tüm hakları saklıdır.

Bu program **Tugay Şahin** tarafından yapılmıştır.  
Kaynak kodlara izinsiz erişim, kopyalama, değiştirme veya başka bir yapay zekâya düzenlettirme **Fikir ve Sanat Eserleri Kanunu (FSEK)** kapsamında hukuka aykırıdır ve yasal işleme konu edilebilir.

## Belgeler

| Dosya | Açıklama |
|--------|----------|
| [`COPYRIGHT.md`](./COPYRIGHT.md) | Telif ve yasal uyarı |
| [`LICENSE`](./LICENSE) | Tüm hakları saklı lisans |
| [`AGENTS.md`](./AGENTS.md) | Yapay zekâ araçları için zorunlu kurallar |
| [`AUTHOR.json`](./AUTHOR.json) | Makine okunur yazar bilgisi |
| [`TS-utas-MEB-Dilekce.md`](./TS-utas-MEB-Dilekce.md) | MEB dilekçe şablonu |
| [`headers/`](./headers/) | Kaynak dosya başı telif şablonları |
| [`ts_utas_attribution.py`](./ts_utas_attribution.py) | Program içi yazar damgası |
| [`tools/inject_copyright_headers.py`](./tools/inject_copyright_headers.py) | Tüm kaynaklara başlık ekleme aracı |

## Kaynak kodlara telif başlığı ekleme

Kaynak dosyalarınız bu depoya geldiğinde:

```bash
python3 tools/inject_copyright_headers.py .
```

Her `.py`, `.js`, `.ts`, `.java`, `.html` vb. dosyanın başına **Tugay Şahin** imzası ve yasal uyarı yazılır.
