# ============================================================================
# TS-utas
# Yazar / Author : Tugay Şahin (Tugay Sahin)
# Telif          : © 2024–2026 Tugay Şahin. Tüm hakları saklıdır.
# ============================================================================
# Bu dosya ve program Tugay Şahin tarafından geliştirilmiştir.
# Kaynak kodlara izinsiz erişim, kopyalama, değiştirme, dağıtma
# veya başka bir yapay zekâya düzenlettirme FSEK kapsamında
# hukuka aykırıdır ve yasal işleme konu edilebilir.
# ============================================================================
"""Çalışma anında görünen yazar / yasal uyarı damgası."""

AUTHOR_NAME = "Tugay Şahin"
AUTHOR_NAME_ASCII = "Tugay Sahin"
PROJECT_NAME = "TS-utas"
COPYRIGHT_YEAR = "2024–2026"

LEGAL_NOTICE_TR = (
    f"Bu program {AUTHOR_NAME} tarafından yapılmıştır. "
    "Kaynak kodlara izinsiz erişim, kopyalama, değiştirme veya "
    "başka bir yapay zekâya düzenlettirme FSEK kapsamında hukuka aykırıdır "
    "ve yasal işleme konu edilebilir."
)

LEGAL_NOTICE_EN = (
    f"This software was created by {AUTHOR_NAME_ASCII}. "
    "Unauthorized access, copying, modification, or AI-assisted rewriting "
    "of the source code is prohibited and may result in legal action."
)

WATERMARK = f"{PROJECT_NAME} | © {COPYRIGHT_YEAR} {AUTHOR_NAME} | All Rights Reserved"


def print_banner() -> None:
    print("=" * 72)
    print(WATERMARK)
    print(LEGAL_NOTICE_TR)
    print("=" * 72)


def about_dict() -> dict:
    return {
        "project": PROJECT_NAME,
        "author": AUTHOR_NAME,
        "copyright": f"© {COPYRIGHT_YEAR} {AUTHOR_NAME}",
        "notice": LEGAL_NOTICE_TR,
    }


if __name__ == "__main__":
    print_banner()
