# NEOLINGUS — German ↔ English dictionary

A single-page German–English dictionary that runs entirely in the browser, offline, with no server.
NEOLINGUS searches the full BEOLINGUS / Ding word list from TU Chemnitz: about 414,500 entries and over
a million one-to-one translations.

**Live page:** https://gmleuning.github.io/beolingusreboot/ (once GitHub Pages is switched on, see below)

## Features

- Searches German and English at the same time, both columns shown side by side
- Results ranked by how well they match: exact entry, whole word, start of a word, then inside a word
- Results can be filtered by word type (noun, verb, adjective, …)
- Grammar and subject tags (`{f}`, `{vt}`, `[ugs.]`, `[med.]` …) show what they mean when you hover over them
- Click any word in the results to look that word up
- Buttons for ä ö ü ß, for keyboards without them
- Each search has its own address (`neolingus.html#q=Haus`), so you can bookmark it and the Back button works
- Keyboard shortcuts: **/** jumps to the search box, **Esc** clears it
- Colours taken from the classic dict.tu-chemnitz.de site; the layout also works on phones

## Using it

**Online:** open the GitHub Pages address above.

**Offline:** download the repository (**Code → Download ZIP**, or clone it) and open `neolingus.html`
in any browser. No installation is needed.

The page loads the whole dictionary (~28 MB) once when it opens, so the first load takes a moment.
Searches after that are instant.

## Files

| File | Role |
|---|---|
| `neolingus.html` | The dictionary page (search, ranking, display) |
| `main.css` | Stylesheet from the original TU Chemnitz site, kept for reference |
| `index.html` | Sends visitors to `neolingus.html`, so the plain Pages address works |
| `chemnitz_beolingus_de-en.txt` | The source word list in Ding format (`German :: English`, one entry per line) |
| `neolingus-data.js` | The same word list wrapped as JavaScript, which the page loads |
| `build_neolingus.py` | Turns the `.txt` into `neolingus-data.js` |
| `chemnitz format.html` | Reference copy of a TU Chemnitz results page that the layout was modelled on |

### Why there is a `.js` copy of the word list

Browsers won't let a page opened from your own disk (`file://`) read a nearby `.txt` file, but they
will load a nearby `<script>`. `neolingus-data.js` is just the text file stored as one JavaScript
string, so the page works when opened straight from a folder. If the `.js` file is missing, the page
offers to load the `.txt` by hand instead.

## Updating the word list

1. Download the latest `de-en.txt` from https://dict.zero-g.net/ (or the TU Chemnitz Ding page) and
   save it as `chemnitz_beolingus_de-en.txt`.
2. Rebuild the data file:

       py build_neolingus.py

   (or `python3 build_neolingus.py` on macOS/Linux). It prints the number of entries and the file size.
3. Commit and push both files.

## Switching on GitHub Pages

Repository **Settings → Pages → Build and deployment**: Source *Deploy from a branch*,
branch `main`, folder `/ (root)`, **Save**. The site goes live a minute or two later.

## Credits and licence

Dictionary data: **BEOLINGUS / Ding**, © Frank Richter, TU Chemnitz, 1995–2026, released under the
GNU General Public License, version 2 or later. See https://dict.zero-g.net/. The copyright header
at the top of the word list must stay in place.

The page and build script in this repository are released under the same licence, the
**GNU General Public License, version 2 or (at your option) any later version**. The full text is in
[LICENSE](LICENSE).
