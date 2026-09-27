# Gematria and ASCII

**The two name-value programs in the browser.** Served at https://nth-member.github.io/gematria/.

- `gematria_names.py` sums the anglicized Hebrew gematria of the letters (A=1 … I=9, J=10 … R=90,
  S=100 … Z=800). It ignores case, spaces and punctuation.
- `ascii_name_sum.py` sums the 7-bit ASCII code of every character, spaces, punctuation and case
  included. A character outside ASCII is an error for that line.

## The site

`docs/` is static: no build step on the server, no dependencies. `index.html` has two parts:

- **Any text:** both values as you type, letter by letter.
- **Run the programs on a list:** reads the lines the way each program reads its names file, prints what
  the program prints, and saves the CSV it writes, with the same columns and file name. It was checked
  byte for byte against the programs, including quoting, tabs, `ß`, zero-width and non-breaking spaces,
  and the wording of the error.

The page needs only the programs' letter values and control-character names, in `docs/data/tables.json`.

## Rebuilding

    python3 build.py

Run this after changing either program. It imports the two programs and takes their own tables, so the
page carries no hand-typed copy of either. Nothing is written beside the programs. It finds the
programs through `GEMATRIA=/path`, or else through the first line of `.programs`, a local file that is
never committed.
