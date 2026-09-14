# Salomé Doucet — Portfolio

A lightweight portfolio website for industrial designer Salomé Doucet, built with
[VitePress](https://vitepress.dev/). It's designed so you can add projects and
change text yourself by editing simple files, keeping any needed programming for day-to-day content management to a minimum.

This guide covers everything you'll normally do: **running the site on your
computer**, **adding or editing projects**, **replacing images**, **editing the
About/Contact pages**, **changing colours and fonts**, and **filling in the SEO
fields** (the little preview that appears when a page is shared on social media).

---

## 1. Running the site on your computer

You only need to do the one-time setup once.

**One-time setup**

1. Install [Node.js](https://nodejs.org/) (version 26 or newer).
2. Open a terminal in this project folder and run:
   ```bash
   npm install
   ```

**Every time you want to preview your changes**

```bash
npm run docs:dev
```

Then open the address it prints (usually <http://localhost:5173>) in your browser.
The page updates automatically as you save files. Press `Ctrl + C` in the
terminal to stop it.

> **Tip:** always preview locally before publishing, so you can catch typos or a
> photo that looks off.

---

## 2. How the project is organised

You'll mostly touch these places:

| What you want to change            | Where to go                         |
| ---------------------------------- | ----------------------------------- |
| A project (text, year, photos)     | `work/<project-name>.md`            |
| Project photos                     | `public/work/<project-name>/`       |
| The About page                     | `about.md`                          |
| The Contact page                   | `contact.md`                        |
| Portrait / contact / share images  | `public/img/`                       |
| Colours, fonts, spacing            | `.vitepress/theme/style.css`        |
| Email + social links (site-wide)   | `.vitepress/config.mts`             |

Anything inside `public/` is served from the root of the site. That's why a file
at `public/work/sadji/cover.jpg` is written as `/work/sadji/cover.jpg` inside a
page.

---

## 3. Adding or editing a project

Each project is **one Markdown file** in the `work/` folder plus **one image
folder** in `public/work/`. The homepage grid builds itself automatically from
these — you don't edit the homepage directly.

### Step 1 — Add the photos

Create a folder `public/work/<project-name>/` and put your images in it. Use
lowercase names with hyphens for the folder (e.g. `my-new-lamp`). Inside it:

- `cover.jpg` — the main image (shown on the homepage grid **and** as the large
  banner at the top of the project page).
- `01.jpg`, `02.jpg`, `03.jpg`, … — the gallery images, shown in order.

> **Keep photos web-friendly.** Very large photos make the site slow. Aim for
> roughly **1600–2200 px** on the long edge and save as JPG. (The existing photos
> were prepared with the helper script in `scripts/`, but you can also just
> resize them in any photo app before dropping them in.)

### Step 2 — Add the text

Create a file `work/<project-name>.md`. Copy this template and fill it in:

```markdown
---
title: My New Lamp
year: 2025
description: "A one-line summary used for search engines and link previews."
cover: /work/my-new-lamp/cover.jpg
gallery:
  - /work/my-new-lamp/01.jpg
  - /work/my-new-lamp/02.jpg
  - /work/my-new-lamp/03.jpg
---

Write the full project description here. You can use several paragraphs —
just leave a blank line between them.
```

The part between the two `---` lines is called the **frontmatter**. Each field:

- **title** — the project name (shown as the heading and homepage caption).
- **year** — used to order the homepage (newest first).
- **description** — short summary for SEO/link previews (see section 6). Keep it
  to one sentence and wrap it in `"straight quotes"`.
- **cover** — path to the main image.
- **gallery** — list of the other images, in the order you want them shown. Each
  line starts with two spaces, then `- `, then the path.

The text **below** the second `---` is the full description shown on the page.

That's it — save, and the project appears on the homepage automatically.

### Editing an existing project

Open its file in `work/`, change the text or the list of images, and save. To
swap a photo, replace the file in `public/work/<project-name>/` with a new one of
the same name.

### Removing a project

Delete its `work/<project-name>.md` file (and optionally its image folder).

---

## 4. Editing the About and Contact pages

Open `about.md` or `contact.md` and edit the text directly. These files mix a
little HTML with the text to get the two-column layout — the parts you edit are
clearly the sentences and links. **Keep the blank lines** between paragraphs and
leave the `<div>` / `<img>` tags in place.

- **Portrait photo (About):** replace `public/img/portrait.jpg`.
- **Contact photo:** replace `public/img/contact.jpg`.
- **Email + social links:** the Contact page links and the footer icons come from
  `.vitepress/config.mts` (see below). Update them there and they change
  everywhere.

---

## 5. Changing colours, fonts and spacing

All styling lives in **one file**: `.vitepress/theme/style.css`. At the very top
there's a block called **Design tokens** — change a value there and it updates
across the whole site. For example:

```css
--green: #0b6755;  /* the name in the header */
--sage:  #a5baad;  /* project titles and headings */
--tan:   #c9bda5;  /* menu, footer, CV headings */
--ink:   #787268;  /* normal body text */
```

You can change fonts and page width in the same block. You rarely need to touch
anything further down the file.

---

## 6. SEO / link previews

"SEO fields" control the title, summary and image that appear when a page is
shared on social media or shows up in a Google result. They come straight from
each page's frontmatter — no special steps needed:

- **title** — the page/project name.
- **description** — the one-line summary.
- **cover** — the image used for the preview thumbnail.

So filling in those three fields on a project (section 3) is all you need. The
About and Contact pages have the same fields at the top of their files.

Two site-wide settings live in `.vitepress/config.mts`:

- **`SITE`** — the website's real address (e.g. `https://salomedoucet.com`). This
  must be correct for link previews to work. Update it if the domain changes.
- **`themeConfig`** — your `email`, `instagram` and `linkedin` links, used by the
  footer and Contact page.

---

## 7. Publishing

The site is hosted on Netlify. To create the finished files yourself, run:

```bash
npm run docs:build      # builds the site into .vitepress/dist
npm run docs:preview    # preview that finished build locally
```

Once connected to Netlify, saving your changes to the project's Git repository
will publish them automatically.

---

### Quick reference

```bash
npm install           # one-time setup
npm run docs:dev      # preview while editing  → http://localhost:5173
npm run docs:build    # build the final site
npm run docs:preview  # preview the final build
```
