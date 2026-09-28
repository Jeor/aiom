# AIO Metadata: Collection Builder Guide


## Start here

**New to collections?** Follow the [five-step quick start](#quick-start), then use the featured example or the manual walkthrough. **Already building?** Jump to [Catalogs and the builder](#catalogs-and-the-builder), [saving and exporting](#8-save-export-and-use-your-layout), or [troubleshooting](#10-quick-troubleshooting). For faster repeat browsing, see [Caching & Warming](Caching-Warming-Guide.md).

## Choose your starting point

| What you want | Best place to start | What you will build |
|---|---|---|
| A ready-made layout to customize | [Use a featured layout](#3-easiest-start-use-a-featured-layout) | Import one section, then adjust its folders and sources. |
| A small collection of your own | [Build your own collection](#5-build-your-own-collection) | Movie Night with two folders, each connected to a movie catalog. |
| Titles displayed directly in Fusion | [Create a normal catalog row](#7-fusion-example-a-normal-catalog-row) | A Trending Tonight row without a folder to open first. |
| A folder based on a provider collection or public list | [Find a provider source](#d-find-a-source-directly-from-a-provider) | Attach a TMDB/TheTVDB collection or an MDBList list from the picker. |

If this is your first layout, finish one small example and open it in your app before importing a large pack.

## Quick start

1. **Prepare a source.** In **Catalogs**, make sure the movie or show catalog you want is enabled. Save your AIO configuration.
2. **Open Collections.** Choose **Nuvio** or **Fusion** at the top.
3. **Create a layout.** Preview a **Featured** layout and import the parts you want, or create a collection with a folder and a catalog source.
4. **Check and save.** Confirm that every folder has its intended sources, resolve any save issues, then save.
5. **Use it in your app.** Export for your chosen app and import the file or supported link there. Saving in AIO alone does not update the app.

**Success check:** you can see your collection in the app, open a folder, and see titles from the catalog you selected.

## Catalogs and the builder

**Catalogs decides what content is available. Collections decides how that content is organized.** A folder called “Comedy” does not automatically filter its contents to comedy: it needs a comedy catalog as its source.

![The Catalog Management screen and Collections entry point](images/00-catalog-management.png)

### Which button should I use?

| In Catalogs | Use it when you want to… | How it relates to the builder |
|---|---|---|
| Quick Add | Add a supported list URL or custom manifest. | Makes the source available in your catalog configuration. |
| Build Your Catalog | Create a filtered discover catalog, such as recent comedy movies. | Defines the titles supplied by a folder or row. It does not create the folder layout. |
| Provider icons | Open source-specific integration settings. | Configure the provider or lists behind your sources. |
| Collections | Arrange sources into collections, folder tiles and Fusion rows. | Opens the builder covered in this guide. |
| Share Setup / Import Setup | Share or import the broader catalog setup. | Separate from the builder's layout-specific Import JSON and Export & share controls. |
| Reload Catalogs | Refresh the catalog view. | Useful when checking available catalogs; it does not import a layout into your viewing app. |

### Enabled is different from Home

| Control | What to keep in mind |
|---|---|
| Enabled (eye icon) | Controls whether the catalog is enabled. Keep a source enabled when you want to use it in your layout. |
| Home (house icon) | Controls whether the catalog is shown as a normal home catalog. It is separate from enabling the source. |
| Row checkbox | Selects catalogs for bulk actions. Checking it is not the same as enabling the catalog. |
| Drag handle / move arrows | Reorders the catalog list. The collection builder also has its own folder and source ordering. |
| Random order | Changes catalog ordering where supported; it does not shuffle your folder layout. |
| Delete Catalog | Removes a catalog from the configuration. A layout that references it may then need a replacement source. |

**Common setup:** keep a catalog **Enabled**, but turn **Home** off if you want to reach it through a collection rather than also showing it as a separate home row. The final display depends on how your client uses home catalogs and imported widgets.

### Read the Catalog Management list

Each row represents a catalog source, such as a movie list or a series discover catalog. Its name identifies the source; its media type tells you whether it supplies movies, series or anime. The same provider can supply several different catalogs.

Use search and filters to find rows, the row checkboxes to select them, and the available bulk actions to change the selected catalogs. **Filtering the screen does not disable the catalogs you cannot see.** Check the selection count before applying a bulk action.

The **Collections** filter offers **All**, **In a collection** and **Not in one**. Use it to find sources already referenced by your layout or sources you have not organized yet. This is separate from the Home switch: a source can belong to a collection and also appear as a normal home catalog.

### What are catalog tags?

A tag is a name you assign to one or more catalogs to group them, such as `Movie Night`, `Documentaries` or `To organize`. A catalog can have several tags, and catalogs from different providers can share one tag. The tag color is a visual aid.

**A tag describes the catalog group, not the titles inside it.** Naming a tag `Comedy` does not filter a mixed movie list to comedies. Use a suitable list or discover-catalog filters to choose the actual content. Catalog tags are also separate from provider content tags, such as AniList tags used in a discover search.

| Where you use a tag | What happens |
|---|---|
| Tags bar in Catalog Management | Filters the rows you see while editing. |
| Select by tag | Selects catalog rows for actions; selection is separate from visibility and enabling. |
| Tag action on selected catalogs | Applies or removes a tag on those catalogs. |
| Tag filters in the builder's catalog picker | Helps find tagged sources available to the builder. |
| Add sources by tag in a folder | Adds the matching available sources to that folder, skipping sources already attached. |
| Profile choices when installing | Builds an installation link for the selected tagged catalog groups. This is separate from exporting a collection layout. |

### Create and apply a tag

1. In **Catalog Management**, tick the checkboxes beside the catalogs you want to group. For example, select the movie versions of TMDB Popular and TMDB Top Rated.
2. Open the **Tag** action for the selection.
3. Under **Create a new tag**, enter `Movie Night`, choose a color if desired, and click **Add**. The new tag is applied to the selected catalogs immediately in the current configuration.
4. To reuse an existing tag, click it in the tag dialog instead of creating another. Tag names that differ only by capitalization are treated as the same tag.
5. Close the dialog, check the tags on the catalog rows, and save your AIO configuration to keep the changes on the server.

The tag dialog shows **Applied to all**, **Applied to some**, or **Not applied** for a selection. Clicking a partially applied tag adds it to the remaining selected catalogs. Clicking a tag already applied to all removes it from that selection.

### Filter, select and manage tags

Click a tag in the tags bar to filter the catalog list. Selecting several tags matches **any** selected tag: `Movie Night` plus `Documentaries` shows catalogs with either label. Other active filters, such as search or media type, still narrow the results. **Clear** in the tags bar clears the tag filter; it does not remove tags from catalogs.

The number beside a tag counts catalogs carrying that tag, not the movies or episodes inside them. It is not necessarily the number currently visible after other filters.

Open **Manage tags** to rename, recolor or delete a tag. Renaming updates its assignments throughout the current configuration. Deleting a tag removes the label and its assignments, not the catalogs themselves. Removing a tag from selected catalogs is narrower: other catalogs can keep it. Save the configuration after these changes. If you use a tag-specific installation link, review that profile and its link after renaming or deleting the tag.

### Use tags to build a collection faster

For the Movie Night example, first apply the `Movie Night` tag to the sources you want. Save the configuration, open the builder, and select a folder.

- To choose individual sources, open **Add catalog**, use the tag filter under **Your catalogs**, and select the sources you want.
- To attach the whole available group to one folder, use the folder's add-sources-by-tag option. Sources already in that folder are skipped.
- For separate tiles such as Popular Movies and Top Rated Movies, create separate folders and attach the corresponding source to each. Adding two sources by tag to one folder does not create two folder tiles.

**Adding by tag copies the current selection of sources into the folder. It is not a live rule.** Tagging another catalog later does not automatically add it to that folder. Repeat the add-by-tag action when you want to bring in newly tagged sources, then save and re-import the layout into your app.

Only tags covering sources available to the builder appear in its tag choices. If a tag is missing, confirm the catalogs are enabled, save your configuration and check the builder's source indicator.

### Tagged profiles and optional content ratings

The installation area's **Profile** choices let you select tagged catalog groups or **All catalogs**. Use the generated installation link for that choice. Clicking a tag in Catalog Management only filters the editor; it does not switch an existing app installation to that profile.

A tag can also have a **Content rating** in Manage tags, with a **Show unrated titles** option. This is an explicit profile setting; a tag named `Kids` or `Family` alone applies no rating limit. The rating setting is intended for installing that tagged profile and can tighten, but not loosen, the rating restriction saved in **Filters**.

When combining profiles with different limits, read the installation summary rather than assuming one uniform limit covers everything. Test the resulting catalogs and search, and decide whether unrated titles should be shown. Adding sources to a collection by tag is not the same action as installing a rating-limited profile.

### Common tag questions

| Question | Answer |
|---|---|
| Does a tag create a folder? | No. Create the folder in Collections, then attach sources. |
| Does clicking a tag enable its catalogs? | No. Filtering, selection and Enabled are different controls. |
| Why does a tagged catalog still appear on Home? | Tags do not change the Home switch. Adjust Home separately. |
| Why did selecting two tags show more catalogs? | Tag filters match either tag, rather than requiring both. |
| Why did a new tagged source not appear in my folder? | Adding sources by tag is a one-time action. Add it to the folder, save and re-import. |
| Does deleting a tag delete its catalogs? | No. It removes the label and assignments. |

### Example: make a source, then put it in a folder

Suppose you want a **Recent Comedies** tile inside **Movie Night**:

1. In **Catalogs**, use **Build Your Catalog** to create a movie discover catalog named `Recent Comedies`. Choose a supported provider and the genre/date filters you want. Available filters vary by provider.
2. Preview and build that catalog, then save the configuration. Provider access or API keys may be required.
3. Open **Collections**, select **Movie Night**, and add a folder named `Recent Comedies`.
4. Click **Add catalog**, find your new catalog under **Your catalogs**, select it, and add it.
5. Save the layout and re-import its export into your app.

Alternatively, use **Quick Add** to bring in an existing public list instead of creating a filtered catalog yourself.

![Quick Add accepts supported list and manifest URLs](images/12-quick-add.png)

### Where does the builder get its catalog list?

The header tells you whether catalogs were read from your **saved manifest** or derived from your **local config**. A saved manifest can provide genre options and requirements that the local draft does not have.

Featured imports can also carry definitions for missing catalogs. These are staged for addition when you apply/save; they are not all added just because you previewed the featured pack. The import summary shows the proposed additions and available capacity.

**Catalog missing from Add catalog?** Save the catalog configuration, confirm the source is enabled and its movie/series type is correct, then reopen the builder and check its source indicator. If needed, use **Change source** to inspect the manifest address. Use your own addon configuration. Creating a tile with the same name will not create the missing source.

## 1. What are you building?

The builder arranges catalogs into a layout. The catalogs supply the movies and shows; the layout controls how people browse them.

| Term | What it means | Example |
|---|---|---|
| Catalog / source | A list that supplies titles. | TMDB Popular — Movie |
| Folder | A tile that opens one or more catalog sources. | Popular Movies |
| Collection | A named group of folders. | Movie Night |
| Row | A direct catalog row for Fusion, rather than a collection of folder tiles. | Trending Tonight |
| JSON | The file format used to move the layout into an app or another builder. You do not need to write it yourself. | Downloaded collection or widget file |
| Manifest | The addon description that tells the builder which catalogs and options are available. | Your saved AIO addon configuration |

A small first collection could be:

- **Movie Night** — the collection.
- **Popular Movies** — a folder using the TMDB Popular movie catalog.
- **Top Rated Movies** — a second folder using the TMDB Top Rated movie catalog.

A folder's cover is artwork for that folder, not the posters for every movie inside it.

## 2. Open the builder and choose your app

1. Open your AIO Metadata configuration and log into your saved setup.
2. Open **Catalogs**.
3. Click **Collections** to open **Collections & Widgets**.
4. Choose **Nuvio** or **Fusion** at the top, depending on where you will use the layout.

Use **Build** to edit a layout, **Featured** to browse ready-made examples, and **Export & share** when you are ready to use or share it.

| Feature | Nuvio | Fusion |
|---|---|---|
| Collections with folder tiles | Supported | Supported |
| Classic catalog rows | Omitted from export | Supported |
| Nuvio presentation and artwork settings | Used by Nuvio | Ignored by Fusion |
| Nested folders | Their catalogs are flattened into the parent folder on export | Their catalogs are flattened into the parent folder on export |

**Nested folders are labeled “Jellyfin only.”** The builder says Jellyfin clients can open them as folders within folders. This guide concentrates on the Nuvio and Fusion export workflow.

## 3. Easiest start: use a featured layout

Featured layouts provide ready-made folders, sources and artwork. You can preview them before importing anything.

![Featured collection gallery](images/01-featured.png)

Examples available when this guide was written:

| Featured layout | What to expect |
|---|---|
| Starter Kit | Awards, decades, directors, genres and streaming services. |
| Ninja Streams | Trending titles, services, genres, decades, runtime, studios and networks. Includes classic rows. |
| Callandt95 | Trending/watchlist rows, services, movie genres and film franchises. |
| Snoak | Popular titles, discovery, service top tens, genres and decades. |
| TVGenie | Daily picks, movie/show categories, decades and networks. |
| Unified Media Experience | A larger selection of services, genres, people, studios, awards and lists. |

Some featured layouts use adapted sources. Read their description: an original Trakt list may have been replaced with an MDBList counterpart or another available source. Provider access and required keys still matter.

### See what a complete layout looks like

![TVGenie Movie Categories: a ready-made layout in the featured preview](images/02-featured-preview.png)

Read this example from the outside in: **Movie Categories** is the collection; **Daily Picks**, **Latest Movies** and **Trending Movies** are folder tiles. The images identify the folders. The catalog sources attached to each folder determine the titles that open inside it.

This is the builder's preview of a complete featured design, before import. Use it as a visual reference; the final app can arrange the same layout differently.

### Example: import only TVGenie's Movie Categories

1. Find **TVGenie** in **Featured**, then click **Preview**.
2. Click the entry names to inspect the different parts of the layout.
3. To keep only one part, click **None**, then tick **Import Movie Categories**.
4. Check that the button says **Import 1 of 3**, then click it.
5. Review the import summary and choose how to combine it with your current draft.

![Only Movie Categories selected for import](images/03-selective-import.png)

The selection checkbox controls **what gets imported**. Selecting an entry to preview it is a separate action.

| Import choice | What it does |
|---|---|
| Merge | Combines matching IDs and skips catalogs you already have. |
| Add as new | Keeps both copies rather than merging them. |
| Overwrite | Discards the existing builder design in favor of the imported one. Check carefully before choosing this. |

The summary may say catalogs are **rebuildable**. That means the file includes definitions for catalogs missing from your setup. The builder adds the needed ones when you apply/save. If you remove parts of the design first, only the remaining referenced catalogs need to be added.

**Start with one section.** Large featured packs can add many catalogs; you do not need to import the whole pack.

## 4. Understand the editor

![The collection editor with a featured movie layout](images/04-collection-settings.png)

- **Left:** your collections and folders. Select an item to edit it. Use drag handles to change their order.
- **Middle:** settings for the selected collection, folder or row.
- **Right:** a live preview of the layout.
- **Design / Preview:** switch between editing and inspecting the selected entry.
- **Status and issue indicator:** show whether you have a draft and whether anything needs attention before saving.

The preview is approximate. It shows your artwork, shapes, titles and order, but spacing and card sizes can differ in the actual app. It is not a playback test.

The screenshots show **“1 issue to fix”** because the demonstration draft has no provider keys. In your setup, expand the issue indicator to read the actual reason.

## 5. Build your own collection

### A. Create the collection and first folder

1. Open **Build** and click **Collection**. In an empty builder you may also see **New collection**.
2. Set **Title** to `Movie Night`.
3. Click **Add folder**.
4. Set **Folder title** to `Popular Movies`.
5. Choose a tile shape: **Poster**, **Wide** or **Square**.

![Creating Movie Night with a Popular Movies folder](images/07-build-folder.png)

A new collection is not yet in your list until you click **Add collection**. **Discard** abandons that new entry.

### B. Give the folder a source

1. Click **Add catalog** in the folder's **Sources** section.
2. In **Your catalogs**, find **TMDB Popular** with type **movie**.
3. Tick it, then click **Add 1**.
4. Check that it appears under **Sources**.
5. Click **Add collection** when the new collection is ready.

![Selecting the TMDB Popular movie catalog](images/06-choose-catalog.png)

The picker lets you search, filter by media type and select several catalogs at once.

You can also use the provider tabs shown above. See [Find a source directly from a provider](#d-find-a-source-directly-from-a-provider) for the steps.

Choose the correct media type: **TMDB Popular — movie** and **TMDB Popular — series** are different catalogs.

### C. Add a second folder

Select **Movie Night**, click **Add folder**, and repeat the process:

| Folder title | Catalog source | Suggested tile shape |
|---|---|---|
| Popular Movies | TMDB Popular — movie | Wide |
| Top Rated Movies | TMDB Top Rated — movie | Wide |

This is an example layout, not a required naming scheme. You can use your own lists instead.

**An empty folder can still export, but it opens empty.** Add at least one source if you want it to show titles.

### D. Find a source directly from a provider

The **Add catalogs** picker pictured above has four tabs: **Your catalogs**, **MDBList**, **TheTVDB** and **TMDB**. Your catalogs reuses sources already in your configuration; the provider tabs let you find additional sources without leaving the builder.

1. Select the folder that should receive the source, then click **Add catalog**.
2. Choose **TMDB** or **TheTVDB** to find collections, or **MDBList** to search for lists.
3. Enter a specific name. For example, try `The Lord of the Rings` when looking for a film collection. This is a search example, not a guarantee of a particular result.
4. Inspect the results and select the collection or list you actually want. Check its media type and any available description; similarly named lists can have different contents.
5. Add the selection, then confirm that it appears in the folder's **Sources**.
6. Review any catalog additions or required provider access shown by the builder. Save the layout, export it, and import it into your app.

| Source tab | Choose it for | Check before adding |
|---|---|---|
| Your catalogs | Reusing an enabled catalog you already configured. | Correct movie/series type and filters. |
| TMDB | Finding a TMDB collection. | The intended franchise or collection, rather than assuming every title search is a collection. |
| TheTVDB | Finding a collection available through TheTVDB's picker. | The result's contents and supported media type. |
| MDBList | Searching for a list that matches your theme. | List identity, contents and any required provider access. |

**No useful results?** Try the full name rather than an abbreviation, check provider access, and confirm you chose the right tab. If you already have a supported list URL, [Quick Add](#example-make-a-source-then-put-it-in-a-folder) is another route.

### E. Check the finished Movie Night example

Before exporting, select **Movie Night** and confirm this structure in the editor:

| Collection | Folder tile | Attached source | Expected result when opened |
|---|---|---|---|
| Movie Night | Popular Movies | TMDB Popular — movie | Popular movie titles. |
| Movie Night | Top Rated Movies | TMDB Top Rated — movie | Top-rated movie titles. |

You should have one collection containing two folders, with one source under each. The preview should show two folder tiles; opening those folders in the app should show their respective titles. Folder artwork is optional for this first check.

Use the complete featured preview above to understand the visual structure. The Movie Night table is the expected result of the manual exercise, not a screenshot from a tested client import.

## 6. Customize folders and collections

### Folder settings

![Folder name, tile shape and cover controls](images/10-folder-options.png)

| Setting | What it changes |
|---|---|
| Folder title | The name of the tile. |
| Tile shape | Poster is tall, Wide is landscape, Square is square. Fusion calls this Layout. |
| Cover image URL | The artwork displayed on the folder tile. Use an image address your viewing device can reach. |
| Hide title on the folder | Hides the text label on that folder. Useful when the artwork already contains the name. |
| Sources / Add catalog | The catalogs opened by the folder. More than one can be attached. |
| Folders inside | Adds nested folders for Jellyfin; Nuvio/Fusion exports flatten their catalogs into the parent. |

![Folder sources and the Jellyfin-only nesting option](images/11-folder-sources.png)

The catalog source supplies the contents; these controls arrange how it is attached to the folder. Use the source arrows or drag handles to change source order. Its actions menu includes **Rename catalog** and **Remove from folder**.

### Which artwork goes where?

Think about the part of the layout you are decorating before choosing an image.

| Artwork field | Belongs to | Intended use |
|---|---|---|
| Cover image URL | Folder | The tile you select to open that folder. For example, a Popular Movies cover identifies that folder. |
| Backdrop image URL | Collection, under Nuvio presentation | Background artwork for the whole collection. |
| Hero backdrop URL | Folder, under Nuvio artwork | Artwork for the folder's hero presentation in a supporting app. |
| Title logo URL | Folder, under Nuvio artwork | A graphic title/logo for the folder's presentation. |
| Focus GIF URL / Play focus GIF | Folder, under Nuvio artwork | Optional animated artwork when supported by the app. |
| Hero video URL | Folder, under Nuvio artwork | Optional video for the hero presentation when supported. |

**Example:** Movie Night can have a collection backdrop, while Popular Movies and Top Rated Movies each have their own covers. Those covers do not replace the posters of the movies inside the folders.

The featured preview shows labeled folder covers such as Daily Picks and Latest Movies. Use the [folder settings screenshot](#folder-settings) to locate the cover control. Start with covers; add optional Nuvio artwork after the basic layout works. Fusion ignores Nuvio-specific presentation settings.

### Nuvio presentation

These collection controls are grouped under **Nuvio presentation**. Fusion ignores them.

| Setting | Purpose |
|---|---|
| Backdrop image URL | A background image for the collection. |
| Folder view mode | Choose Tabbed grid, Rows, or Follow layout. |
| Pin to top | Requests that the collection be pinned at the top in Nuvio. |
| Focus glow | Turns the focus glow on or off. |
| Show “All” tab | Controls whether the collection includes an All tab. |

**Show Nuvio artwork** opens optional folder artwork fields: **Cover emoji**, **Focus GIF URL**, **Hero backdrop URL**, **Hero video URL**, **Title logo URL**, and **Play focus GIF**. Leave them blank if you only want a simple tile. Their actual appearance depends on the app.

The collection-level **Hide title** control is labeled **Fusion only**. It is separate from hiding a folder's title.

## 7. Fusion example: a normal catalog row

Use a **Row** when you want a catalog displayed directly, instead of a tile that opens a folder.

1. Select **Fusion**, then click **Row**.
2. Name it `Trending Tonight`.
3. Click **Pick catalog** and choose your trending movie catalog.
4. Adjust **Items shown**, aspect ratio and card size.
5. Optionally enable numbered rankings or change badges.
6. Click **Add row**.

![A new Fusion row and its approximate preview](images/08-fusion-row.png)

| Row setting | Meaning |
|---|---|
| Items shown | The item count requested for the row. |
| Cache TTL (seconds) | The row's cache duration setting. For example, 1800 seconds is 30 minutes. |
| Aspect ratio | Poster, Wide or Square cards. |
| Card size | The card-size preference for the row. |
| Numbered ranking | Adds 1, 2, 3… to the cards. |
| Hide title | Hides the row heading. |
| Provider badges / Rating badges | Controls those badges in the row. |

The screenshot is an unfinished row before its catalog is selected. **Fusion drops rows without a catalog. Nuvio omits classic rows entirely.**

## 8. Save, export and use your layout

There are two separate jobs: save the design in AIO, then import it into the viewing app.

| Action | What it does | What to do next |
|---|---|---|
| Add collection / Add row | Adds the new entry to the builder design. | Review the entry, then save the configuration. |
| Apply only | Applies the design to the current configuration without saving it to the server. | Save the configuration when you are ready to keep it on the server. |
| Save | Stores the configuration on the server. | Export for the app you use. |
| Download | Downloads the selected export as a JSON file. | Import that file into the target app. |
| Import in Nuvio or Fusion | Loads the exported layout in that app. | Open a folder or row to check the contents. |

**Typical sequence:** Add collection → Save → Export & share → Download → Import in your app.

1. Expand any **issues to fix** and resolve them.
2. Click **Save** to store the configuration on the server. **Apply only** keeps the design in the current configuration without saving it to the server.
3. Select the correct target: **Nuvio** or **Fusion**.
4. Open **Export & share**.
5. For your own app, leave **Make a copy for someone else** off. Use **Download** to get the JSON file, or use the import link if your app supports it.
6. In the target app, open its collection/widget import feature and import the file or supported link.
7. Check the layout and open a folder to verify that its sources load.

**Saving in AIO does not push the change into Nuvio or Fusion. You must import again to see later layout edits.** The saved-config import link is unavailable until you have saved a configuration.

### Updating an existing layout

- **Nuvio:** editing an imported collection preserves its ID, so re-importing updates the matching collection. Building a new collection creates a new ID and adds another collection.
- **Fusion:** importing adds widgets rather than matching existing ones. The builder advises removing the widgets you changed in Fusion, then importing only those replacements. They return at the end, so you may need to reorder them.

### Image caching

**Serve images through this server** makes exported artwork URLs use AIO's image cache. The original addresses in the editor remain unchanged. This may help with slow image hosts, but the viewing device must be able to reach your AIO server.

## 9. Share a layout without sharing your account link

![Export dialog with Make a copy for someone else enabled](images/09-share-safely.png)

1. Open **Export & share**.
2. Turn on **Make a copy for someone else**.
3. Download that copy and review it for any private list names or custom image URLs you added.
4. Share the sanitized file, not your personal addon or import link.
5. The recipient opens **Import JSON** in their own AIO builder, then loads the file, pastes its contents or loads its link.
6. They review the import summary, save their own setup, and export a personal copy for their app.

The sharing switch removes the personal addon link. It does not mean that every custom name or external URL you typed is suitable for public sharing. A share copy is intended to be imported into the recipient's builder first so their own addon link can be filled in.

## 10. Quick troubleshooting

Start with the symptom below. When testing, change one thing at a time and check the same folder again.

### My folder is empty

1. In the builder, select the folder and check **Sources**. An empty tile can export successfully.
2. Confirm the catalog is enabled in **Catalogs** and has the correct media type.
3. Check the list/provider itself and any required access or filters. If the source has no titles, adding artwork will not fix it.
4. Save and re-import if you changed the source or layout.

### I saved, but nothing changed in my app

1. Check whether you clicked **Save** or only **Apply only**.
2. Export for the correct app and import it there again.
3. In Nuvio, edit the existing collection to preserve its ID. In Fusion, follow the replacement workflow to avoid duplicates.

### I cannot save or cannot see a genre option

Expand the issue indicator. Resolve the specific problem it names, such as missing provider keys or capacity. If the builder is using a local draft, save the main configuration so it can read the real manifest. Do not paste somebody else's private manifest link to work around this.

### My artwork is blank

Check the cover URL first: it should point to an image the viewing device can reach. A successful browser preview on one device does not prove another device can reach a private server. If using **Serve images through this server**, check that the app can reach AIO too.

### Other problems

| Problem | What to check |
|---|---|
| New collection is missing from the builder list | Click Add collection after creating it. |
| Source is wrong or unavailable | Check the folder's Sources and the builder's source indicator. Use your own saved configuration. |
| Fusion has duplicate widgets | Follow [Updating an existing layout](#updating-an-existing-layout) and import only the changed replacements. |
| Nuvio is missing a classic row | Classic rows are Fusion-only. Use a collection with folders for Nuvio. |
| Preview looks different from the app | The builder preview is approximate. Check the exported layout in the target app. |
| Images load slowly on repeat visits | See [Caching & Warming](Caching-Warming-Guide.md) for image routing, caching and warming checks. |

**A good first setup:** one collection, two folders, one source per folder. Once that works in your app, add more sections or adapt a featured layout.
