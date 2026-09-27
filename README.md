# H-Gematria/ASCII

**The two name-value programs in the browser.** Served at https://nth-member.github.io/gematria/.

- `gematria_names.py` sums the anglicized Hebrew gematria of the letters (A=1 … I=9, J=10 … R=90,
  S=100 … Z=800). It ignores case, spaces and punctuation.
- `ascii_name_sum.py` sums the 7-bit ASCII code of every character, spaces, punctuation and case
  included. A character outside ASCII is an error for that line.

## The site

`docs/` is static: no build step on the server, no dependencies. `index.html` has two parts; on the
page, gematria is called H-Gematria:

- **FULL NAME (GIVEN):** both values as you type, letter by letter, and their delta (gematria − ASCII).
- **RUN FULL NAMES (GIVEN) ON A LIST:** reads the lines the way the programs read their names file, and
  **Run** saves one CSV, `h-gematria_ascii_results_<stamp>.csv`, with a row per name: `gematria_names.py`'s columns, `ascii_name_sum.py`'s columns,
  and the delta (gematria − ASCII). Each program's columns were checked byte for byte against the program,
  including quoting, tabs, `ß`, zero-width and non-breaking spaces, and the wording of the error.

Before either value is computed, every character outside ASCII is ASCII-rized, so no name fails: curly quotes
and dashes become their ASCII forms, accented letters lose their accents (Ë → E), ß becomes ss, Cyrillic and Greek
are transliterated, and a character with no ASCII form (a zero-width space, a Chinese character) is dropped. The
CSV keeps the name as given in `original_name`; every other column comes from the ASCII-rized text, and for any name
it equals what the two programs give for that ASCII-rized text.

The page needs only the programs' letter values and control-character names, in `docs/data/tables.json`.

## Rebuilding

    python3 build.py

Run this after changing either program. It imports the two programs and takes their own tables, so the
page carries no hand-typed copy of either. Nothing is written beside the programs. It finds the
programs through `GEMATRIA=/path`, or else through the first line of `.programs`, a local file that is
never committed.
