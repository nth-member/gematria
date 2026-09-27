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
- **RUN FULL NAMES (GIVEN) ON A LIST:** a typed list, or a file chosen with **or a file…** (`.csv`, `.txt`
  or `.tsv`, one full name per line, no header). Lines are read the way the programs read their names file:
  UTF-8, with `\r\n`, `\r` and `\n` all ending a line, blank lines and lines beginning with `#` skipped.
  **Run** saves one CSV, `h-gematria_ascii_results_<stamp>.csv`, with a row per name:

  | columns | from |
  |---|---|
  | `original_name`, `normalized_letters`, `h-gematria_breakdown`, `h-gematria_total` | `gematria_names.py` |
  | `ascii_characters`, `ascii_breakdown`, `ascii_total` | `ascii_name_sum.py` |
  | `delta` | H-Gematria − ASCII |

  Each program's columns were checked byte for byte against the program, including quoting, tabs, `ß`,
  zero-width and non-breaking spaces.

### Lists of any size

Run never holds the list or the CSV whole. A file is read a batch at a time, and rows are written as they
are made. For a file over 50 MB, where the browser allows it (desktop Chrome, Edge, Opera), Run first asks
where to save and then writes straight to that file on disk; elsewhere the CSV is built in the browser's
own storage, 16 MB at a time, and saved as a download, so its size is bounded by the device's memory. The
screen shows the first 200 names and a running count, and Run becomes **Stop** while it runs; a stopped
run keeps what it has written. A file that is not UTF-8 is refused rather than half-saved.

The CSV is about fifteen times the size of the list, most of it the two letter-by-letter breakdowns. Ten
million lines (9,875,900 names) streamed to a 3.15 GB CSV in 61 seconds with 172 MB of memory; that CSV is
byte-identical to the two programs run on the same list and merged, and Polars and VisiData both read it
whole.

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

## The nth-member sites

| site | repository | what it is |
|---|---|---|
| https://nth-member.github.io/revott/ | nth-member/revott | REVOTT atop GDELT: the field at every node of an instance |
| https://nth-member.github.io/gdelt/ | nth-member/gdelt | what GDELT was reading on a given day |
| https://nth-member.github.io/member/ | nth-member/member | the nth member: REVOTT's numerator, its introspection and its journal |
| https://nth-member.github.io/gematria/ | nth-member/gematria | H-Gematria/ASCII: the two name-value programs in the browser |
| https://nth-member.github.io/alien-corridor/ | nth-member/alien-corridor | the Alien Corridor Support System (MDQNM engine) in the browser |
