#!/usr/bin/env python3
"""
Concatena todos os arquivos .md de sections/ em um unico arquivo
topaz_knowledge_base.md, adicionando cabecalho com metadados.

Uso: python build_kb.py
"""

import os
import glob
from datetime import datetime

SECTIONS_DIR = os.path.join(os.path.dirname(__file__), "sections")
OUTPUT_FILE = os.path.join(os.path.dirname(__file__), "topaz_knowledge_base.md")

HEADER = """<!--
  BASE DE CONHECIMENTO TOPAZ -- SUPORTE A VENDAS
  Gerado automaticamente por build_kb.py
  Data: {date}
  Versao: 1.0
  Secoes: {section_count}
  Fontes: site topazevolution.com, topaz_one.md (video), topaz_core_banking.md (video)
-->

"""

SEPARATOR = "\n\n---\n\n"


def build():
    md_files = sorted(glob.glob(os.path.join(SECTIONS_DIR, "*.md")))

    if not md_files:
        print("Nenhum arquivo .md encontrado em sections/")
        return

    sections = []
    for path in md_files:
        with open(path, encoding="utf-8") as f:
            content = f.read().strip()
        sections.append(content)
        print(f"  + {os.path.basename(path)} ({len(content):,} chars)")

    header = HEADER.format(
        date=datetime.now().strftime("%Y-%m-%d %H:%M"),
        section_count=len(sections),
    )

    full_doc = header + SEPARATOR.join(sections) + "\n"

    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        f.write(full_doc)

    lines = full_doc.count("\n")
    words = len(full_doc.split())
    print(f"\n  Arquivo gerado: {OUTPUT_FILE}")
    print(f"  {len(sections)} secoes | {lines} linhas | ~{words:,} palavras | {len(full_doc):,} caracteres")


if __name__ == "__main__":
    build()
