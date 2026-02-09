"""
Builds the three standalone palette versions from index.html.

index.html is the master: one design, three themes, live switcher.
Each build below is the SAME markup with one palette locked in and the
switcher removed — so each file can be shared, reviewed or imported into
Figma (html.to.design) on its own.

Run:  python build.py
"""
import re
import os

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "index.html")

THEMES = [
    ("theme-01-sahyadri.html",   "sahyadri",
     "Sahyadri",         "Deep forest green + the logo's lime yellow"),
    ("theme-02-monsoon.html",    "monsoon",
     "Monsoon",          "River teal-green + warm golden yellow"),
    ("theme-03-terracotta.html", "terracotta",
     "Terracotta Trail", "Farm olive green + ochre"),
]

master = open(SRC, encoding="utf-8").read()

for filename, slug, name, blurb in THEMES:
    out = master

    # 1 · lock the palette on <html>
    out = out.replace('<html lang="en" data-theme="sahyadri">',
                      f'<html lang="en" data-theme="{slug}">', 1)

    # 2 · title / description carry the theme name
    out = out.replace("<title>Join With Me — Nature. For Everyone.</title>",
                      f"<title>Join With Me — Nature. For Everyone. ({name})</title>", 1)
    out = out.replace('content="Guided, beginner-friendly nature walks',
                      f'content="[{name} palette — {blurb}] Guided, beginner-friendly nature walks', 1)

    # 3 · drop the review-only theme switcher
    out = re.sub(r'<!-- Theme switcher[\s\S]*?</div>\n\n<div class="lb"',
                 '<div class="lb"', out, count=1)

    open(os.path.join(HERE, filename), "w", encoding="utf-8").write(out)
    print(f"built {filename:26s}  {name} — {blurb}")

print("\nMaster (all three themes + switcher): index.html")
