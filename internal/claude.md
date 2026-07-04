# HTML Generation Rules — Phoenix Internal Site

## Structure

- All pages link to `../css/style.css` (or `css/style.css` from root)
- All pages include `<meta name="robots" content="noindex, nofollow">`
- Include a `<nav>` TOC block for any page with more than a few sections
- `lang="en"` for English files, `lang="es"` for Spanish files

## Horizontal Rules

- One `<hr>` directly after `</nav>` — always present
- Do NOT add `<hr>` tags between sections

## Notes

- Do not wrap `<strong>Note:</strong>` paragraphs in `<blockquote>`
- Use plain `<p>` instead

## Blockquotes

- Reserve `<blockquote>` for sample/script text only (dialogue, speeches, intro scripts)

## Spanish (SPA) Files — Bilingual Sample Text

- Sections labelled "sample text", "sample interaction", "sample intro text", "sample outro text" get bilingual treatment
- English lines first, then Spanish translation in `<em>` italics, all within the same `<blockquote>`
- All regular sentence case (not all caps, not title case)

## Units

- Distance: `X m / Y ft`
- Wind speed: `X kts / Y km/h / Z m/s`

## Images

- HTML files in `operations/` reference images as `../img/routes/`
- Markdown files in `md/operations/` reference images as `../../img/routes/`
- Image filenames with spaces use angle bracket syntax in MD: `![alt](<path with spaces.jpg>)`

## File Naming

- English: `name-eng.html`
- Spanish: `name-spa.html`
- HTML goes in the folder matching the MD subfolder (e.g., `md/maintenance/` → `maintenance/`)

## index.html

- Add both ENG and ESP links whenever a new page pair is created
- Group links under a `<div class="section">` with a `<div class="section-title">` label
