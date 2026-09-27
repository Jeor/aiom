# AIO Metadata Collection Builder Guide

An illustrated, community-oriented guide to preparing catalogs, building collections, using featured layouts, exporting to Nuvio or Fusion, and troubleshooting common problems.

**[Read the dark guide online](https://jeor.github.io/aiom/)**

**[Read the guide in Markdown](Collection-Builder-Guide.md)** · **[Open the dark HTML edition](index.html)** · **[Download the offline edition](Collection-Builder-Guide.html)**

The HTML edition has a dark theme, section navigation, keyboard focus indicators, responsive tables and a print stylesheet. The offline edition embeds all screenshots and styling in one file. GitHub displays Markdown directly; HTML can be viewed through GitHub Pages or downloaded and opened locally.

## What is covered

- Catalog Management, Quick Add, Build Your Catalog and Collections: what each does.
- Enabled versus Home visibility, media types, saved manifests and staged sources.
- A featured TVGenie example and a manual Movie Night collection.
- Folder artwork, Nuvio presentation, Fusion rows and app-specific differences.
- Apply versus Save, re-importing changes and avoiding duplicate Fusion widgets.
- Safe sharing and symptom-based troubleshooting.

## Publish on GitHub

1. Upload the **contents** of this folder to the repository/folder you choose. Keep `images/` alongside the Markdown and HTML files.
2. GitHub will render this README and the Markdown guide automatically.
3. To host the dark website, use the repository's **Settings → Pages** controls to publish the branch/folder containing `index.html`. A simple setup is a dedicated repository with these files at its root. Menu wording and availability depend on GitHub settings.
4. For a guide stored under a larger repository, use that repository's existing documentation or Pages workflow instead of replacing it.
5. Review the publication visibility before publishing. Only the curated guide files belong in the repository—not configuration exports, credentials, test logs or personal addon links.

## Local preview and updates

Open `index.html` locally, or serve this directory with a static web server. No package installation is required.

Edit `Collection-Builder-Guide.md` for content and `guide.css` for appearance. Rebuild the HTML and share bundle with:

```sh
python3 build.py
```

The build script checks local image references and internal guide links. It also creates a curated `github-ready/` folder and a ZIP; those generated packaging copies do not need to be committed.

## Scope and verification

Reviewed against the AIO Metadata v3.2.0 builder interface on September 27, 2026. Screenshots show a demonstration draft and public featured layouts. Importing inside Nuvio or Fusion was not tested; the guide describes the builder's own export instructions. Labels and behavior may change with future releases.

See [attribution](ATTRIBUTION.md) and [contribution guidance](CONTRIBUTING.md). This is an independent guide, not an official AIO Metadata, Nuvio or Fusion publication. No license is assigned here to third-party UI, artwork or featured designs.
