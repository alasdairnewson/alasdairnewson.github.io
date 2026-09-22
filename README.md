# Alasdair Newson — academic website

Static site for [alasdairnewson.github.io](https://alasdairnewson.github.io).

## Structure

- `/` — About me (home)
- `/cv/` — Curriculum Vitae
- `/phd-thesis/` — PhD and HDR
- `/publications/` — Publications
- `/research/` — Research hub and topic subpages
- `/software/` — Software and codes
- `/teaching/` — Teaching

Shared styles: `css/style.css`. Shared script: `js/main.js`.

## Regenerating pages

After editing `generate_site.py`:

```bash
python3 generate_site.py
```

## Assets

See `assets/README.md` for files you need to add (portrait, PDFs, figures, code archives).

## Local preview

```bash
python3 -m http.server 8080
```

Then open http://localhost:8080
