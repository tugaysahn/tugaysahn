#!/usr/bin/env python3
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
"""Kaynak dosyaların başına Tugay Şahin telif başlığını ekler."""

from __future__ import annotations

import argparse
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
HEADERS = ROOT / "headers"

MARKER = "Yazar / Author : Tugay Şahin"

HASH_EXTS = {".py", ".sh", ".bash", ".zsh", ".rb", ".r", ".yaml", ".yml", ".toml", ".ini", ".cfg"}
C_EXTS = {".js", ".jsx", ".ts", ".tsx", ".java", ".c", ".cpp", ".h", ".hpp", ".cs", ".go", ".kt", ".swift", ".css", ".php", ".rs"}
HTML_EXTS = {".html", ".htm", ".xml", ".vue", ".svelte"}


def load_header(ext: str) -> str | None:
    if ext in HASH_EXTS:
        return (HEADERS / "HEADER_HASH_STYLE.txt").read_text(encoding="utf-8")
    if ext in C_EXTS:
        return (HEADERS / "HEADER_C_STYLE.txt").read_text(encoding="utf-8")
    if ext in HTML_EXTS:
        return (HEADERS / "HEADER_HTML_STYLE.txt").read_text(encoding="utf-8")
    return None


def inject(path: Path, dry_run: bool = False) -> bool:
    header = load_header(path.suffix.lower())
    if header is None:
        return False

    text = path.read_text(encoding="utf-8")
    if MARKER in text:
        return False

    # Shebang / encoding satırını koru
    lines = text.splitlines(keepends=True)
    prefix = ""
    body_start = 0
    if lines and lines[0].startswith("#!"):
        prefix = lines[0]
        body_start = 1
        if body_start < len(lines) and "coding" in lines[body_start]:
            prefix += lines[body_start]
            body_start += 1

    new_text = prefix + header + "".join(lines[body_start:])
    if not dry_run:
        path.write_text(new_text, encoding="utf-8")
    return True


def main() -> None:
    parser = argparse.ArgumentParser(description="TS-utas telif başlığı enjekte et")
    parser.add_argument("paths", nargs="*", default=["."], help="Taranacak klasör/dosya")
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    count = 0
    for raw in args.paths:
        p = Path(raw)
        files = [p] if p.is_file() else [f for f in p.rglob("*") if f.is_file() and ".git" not in f.parts]
        for f in files:
            if inject(f, dry_run=args.dry_run):
                print(("DRY " if args.dry_run else "OK  ") + str(f))
                count += 1
    print(f"Toplam: {count} dosya")


if __name__ == "__main__":
    main()
