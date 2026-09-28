# AIO Metadata: Collection Builder Guide


## Start here

**New to collections?** Follow the [five-step quick start](#quick-start), then use the featured example or the manual walkthrough. **Already building?** Jump to [Catalogs and the builder](#catalogs-and-the-builder), [saving and exporting](#8-save-export-and-use-your-layout), or [troubleshooting](#10-quick-troubleshooting). For faster repeat browsing, see [image caching](#11-cache-images-for-faster-repeat-browsing) and [warming modes](#12-choose-a-warming-mode).

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

**You can also add folder sources directly from a provider.** Click **Add catalog**, then use the **TMDB** or **TheTVDB** tab to find collections, or the **MDBList** tab to search for lists. Select the collection or list you want and add it to the folder. You do not have to start with a source already shown under **Your catalogs**. Available options depend on the provider and your configuration.

Choose the correct media type: **TMDB Popular — movie** and **TMDB Popular — series** are different catalogs.

### C. Add a second folder

Select **Movie Night**, click **Add folder**, and repeat the process:

| Folder title | Catalog source | Suggested tile shape |
|---|---|---|
| Popular Movies | TMDB Popular — movie | Wide |
| Top Rated Movies | TMDB Top Rated — movie | Wide |

This is an example layout, not a required naming scheme. You can use your own lists instead.

**An empty folder can still export, but it opens empty.** Add at least one source if you want it to show titles.

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

### More symptoms


| Problem | What to check |
|---|---|
| Folder opens empty | Does it have a catalog source? Is that source enabled and working in AIO? |
| New collection is missing from the list | Did you click Add collection after creating it? |
| Save is disabled | Expand the issue indicator. Check missing provider keys, required configuration and catalog limits. |
| Catalog or genre options are missing | Check the catalog source. A saved manifest provides details that a local draft may not contain. |
| Source is wrong or unavailable | Use Change source to inspect the manifest URL; use your own configuration, not somebody else's private addon link. |
| App still shows the old design | Save, then re-import the export into the app. |
| Fusion has duplicate widgets | Re-import only the changed replacements, following the update guidance above. |
| Nuvio is missing a classic row | Classic rows are Fusion-only. Use a collection with folders for Nuvio. |
| Artwork is missing | Check the image URL and whether the device can reach it; consider server image caching. |
| Preview looks different from the app | The builder preview is approximate. Test the exported layout in the target app. |

**A good first setup:** one collection, two folders, one source per folder. Once that works in your app, add more sections or adapt a featured layout.


## 11. Cache images for faster repeat browsing

**Caching stores images after they are fetched or rendered. Warming fetches content ahead of a visit.** You can use the image cache without running a full warming job: normal browsing fills it as images are requested through AIO's cache routes.

| What is cached? | What it saves | Where to look |
|---|---|---|
| Catalogs and metadata | Repeated provider lookups for lists, titles and artwork URLs. | Dashboard → Ops → Cache Management |
| Image files | Downloading or rendering the same poster, logo or background again. | Dashboard → Ops → Image Cache |
| Hot images in RAM | Disk reads for frequently requested images eligible for the memory cache. | Settings → Images & Art → Image Cache Memory Size |
| Images on the viewing device | Repeated transfers between the player and the image server. | Art proxy client-cache and provider-policy settings |

A metadata cache hit does not mean the image file is cached. An image loaded directly from an external provider also does not automatically pass through AIO's image cache.

### A. Turn on the cache and choose what it stores

1. Open **Dashboard → Settings → Images & Art**. Use the settings search if a control is hard to find.
2. Enable **Built-in Image Cache**. This setting is marked **Restart**; restart the AIO container after applying it.
3. Enable the artwork classes you use, using the table below.
4. Check **Image Cache Max Size** against available storage. Keep the cache on a persistent volume; an SSD is preferable for frequent image access.
5. Browse a few titles, then open **Ops → Image Cache**. Check that the image count and disk usage increase.

| Setting | Suggested starting point | Why / trade-off |
|---|---|---|
| Built-in Image Cache | On | Stores images served through the built-in cache. Posters are included by default. |
| Cache Backgrounds | On if you display backgrounds | Avoids repeatedly downloading large artwork. Uses more disk space. |
| Cache Landscape Posters | On if your client uses landscape tiles | Helps repeat visits to those rows. |
| Cache Logos | On if logos are shown | Saves repeated logo downloads. Creates many small files. |
| Cache Collection Images | On if you use collection artwork through the cache | Stores collection covers, backdrops, logos and focus GIFs without poster reshaping. |
| Cache Processed Images | On | Avoids repeatedly rendering rating overlays and image transforms. |
| Cache Episode Thumbnails | Optional | Useful for frequent episode browsing, but long series can add hundreds of files. |
| Bring Posters to 2:3 | Leave enabled unless you need another behavior | Normalizes poster shapes. This is a presentation setting, not a reason to increase concurrency. |

For collection exports, **Serve images through this server** routes the exported artwork through AIO's cache. The viewing device must be able to reach the server. **Poster Proxy URL** normally stays blank when using the built-in cache; it is for an external caching proxy.

### B. Choose sensible storage and image sizes

These are starting points, not requirements for every server. Check free space, other applications and actual cache use before increasing limits.

| Setting | What to change | When to change it |
|---|---|---|
| Image Cache Max Size | Keep the default `10g` for a small setup; consider `25g` or `50g` on an SSD with room. | Raise it when the cache stays near its budget or warming reports over capacity. More space helps retain images; it does not make a provider respond faster. |
| Image Cache Memory Size | Start at the default `128m`; consider `512m` or `1g` only with RAM headroom and a measured need. | This is an additional RAM allowance, not the total disk cache. A large server does not automatically need a tens-of-gigabytes allocation. |
| Prefer Smaller TMDB Posters | On | Uses a 600×900 rendition rather than the original. |
| Prefer Smaller TMDB Logos | On, then check the result on your display | Uses `w500` logos. Reduces transfer sizes, with a possible loss of detail at large display sizes. |
| Prefer Smaller TMDB Landscape Posters | On for ordinary catalog tiles | Uses `w780` artwork; check quality if your client displays it much larger. |
| Prefer Smaller TMDB Backdrops | Leave off for full-resolution backgrounds; enable for lower bandwidth | Uses `w1280`. Large and 4K displays may show softer backgrounds. |

The smaller-image options affect **TMDB** artwork, not every provider. Existing metadata can keep its old artwork URLs until refreshed. Let it expire naturally, or refresh a specific affected item; clearing every cache creates a new burst of downloads.

### C. Keep artwork fresh without unnecessary downloads

**Use Built-In Provider Policies** is a good starting point. Providers serving changing rating posters may need different expiry rules from providers serving stable artwork.

- **Image Cache Validity (Days)** supplies the general freshness period where no provider policy applies. Start with `30`; longer is not always better for changing artwork.
- **Image Cache Inactive Days** removes images that have not been requested recently. Start with `30`, then adjust to your storage budget and browsing habits.
- **Art Proxy Client Cache (Days)** affects how long a player/browser can keep art. Leave it at `1` initially; provider rules can override it.
- **Follow Each Source's Own Validity** and **Art Proxy Follows the Source's Cache-Control** are different controls. Leave their defaults unless you specifically want upstream headers to govern caching.
- **Per-Provider Cache Policies**, also accessible through **Ops → Image Cache → Advanced…**, let you customize a particular provider without changing every image's lifetime.

Do not set every lifetime to “forever” to chase speed. You may keep old ratings or artwork long after the source changes.

## 12. Choose a warming mode

Start with the content people actually browse. Warming spends provider requests, bandwidth, disk writes and sometimes CPU before anyone opens the item. It is useful when that work will be reused.

| Mode or task | What it prepares | Best use |
|---|---|---|
| Normal browsing, without a full warm | Requested catalogs, metadata and images fill their respective caches as needed. | Small or infrequently used setups; minimal speculative work. |
| Essential warming | A small set of shared essentials, such as genres, studios and popular catalog data. | A light background baseline. |
| TMDB popular warming | Popular/trending content and related metadata. | Broad discovery browsing rather than a particular user's complete list setup. |
| Comprehensive warming | Eligible configured catalogs for the selected saved configurations, up to a page limit. Discovered artwork can be sent to the image warmer. | Regularly used collections and lists that should be prepared ahead of time. |
| MAL warming | MAL catalog tasks, with optional priority genres, decades and seasonal/schedule coverage. | Setups that use MAL anime catalogs and have working provider access. |
| Image warm queue | Downloads or renders offered artwork in the background. | Supports image preparation; it is not a separate scan of every movie or show in existence. |

**Warmup Mode** offers `essential` and `comprehensive`. In comprehensive mode, the separate TMDB popular-content and MAL warmers are skipped. Do not try to enable every warmer to make the same content load faster. The small essential-cache task is separate from the TMDB popular-content pass.

### A. Start with essential and popular warming

Open **Settings → Warming: Popular**:

| Setting | Starting point |
|---|---|
| Enable Cache Warming | On for automatic essential warming. Restart if the dashboard marks the change as requiring it. |
| Warming Interval (min) | `720` — every 12 hours. |
| TMDB Popular Warming | Enable if popular TMDB content is useful to your users. |
| Popular Warming Interval (hrs) | `24`. |
| Warming Language | Match the language you normally browse, such as `en-US`. |

Popular warming needs server-side TMDB access. A personal key in a saved user configuration is not necessarily the key used by the shared popular warmer. Check the logs if the task reports that it has no TMDB key.

### B. Warm your own catalogs with comprehensive mode

Open **Settings → Warming: Full**:

1. Set **Warmup Mode** to `comprehensive`.
2. Enter your saved configuration UUID in **Warmup UUIDs**. Use your own configuration identifier, not a provider API key. The current settings accept up to five UUIDs; keep these identifiers private.
3. Set **Max Pages Per Catalog** to a modest starting value such as `3`. This is a suggested first test, not the application's default of `100`.
4. Keep **Warmup Interval (hrs)** at `24`, **Initial Delay (sec)** at `300`, and **Task Delay (ms)** at `100` initially.
5. Leave **Resume on Restart** enabled. Apply the settings and follow any restart notice shown by your version.
6. Open **Ops**, find **Comprehensive Catalog Warming**, and start one run using its **Force** control or the **Comprehensive** quick action.
7. Watch progress and image capacity before increasing the page limit or adding more configurations.

**A page limit is not a title count.** Page sizes vary by provider. Even three pages per catalog can be substantial when a configuration contains hundreds of catalogs.

Comprehensive does not mean literally every catalog: the current implementation excludes some dynamic catalogs, such as Up Next and recommendations, and catalogs with caching disabled. It also handles sources behind merged catalogs rather than simply warming the merged wrapper.

Keep **Warmup TTL Lead (sec)** at `60` initially. It helps warmed catalog entries expire shortly before the next run so the next pass can refresh them. Leave **Auto on Cache Epoch Change** off unless you intentionally want a new full run after invalidating the metadata cache namespace.

The current settings enforce a minimum of **12 hours** for the comprehensive interval, even though its description mentions shorter fractional examples. Follow the validation in your installed version.

### C. Use quiet hours correctly

**Quiet hours are a period when warming pauses or skips starting, not a window when it runs.** For example, `18:00-23:00` protects evening browsing by keeping the comprehensive warmer quiet during those hours.

Enable **Quiet Hours Enabled** and set **Quiet Hours Range** to the time you want to protect. The comprehensive warmer reads the server/container's local clock, so check its timezone. Quiet hours are not a precise “start at this time” scheduler, and already queued image work may still need to finish.

### D. Enable MAL warming only when you need it

Under **Warming: MAL**, enable **MAL Warmup Enabled** only if you use MAL catalogs and provider requests are succeeding. This warmer runs in `essential` mode.

Start with **MAL Warmup Interval (hrs)** at `24`, **MAL Initial Delay (sec)** at `300`, and **MAL Task Delay (ms)** at `100`. Use **MAL Warmup Decades**, **MAL Priority Pages**, and the priority/schedule switches to limit the content being prepared. Keep safe-for-work filtering aligned with the intended audience.

If MAL requests are failing or rate-limited, warming more frequently will not fix provider access. Resolve the errors first. Its separate **MAL Quiet Hours** controls protect time in the same way: they stop work during the selected period.

### E. Tune image warming separately

Return to **Settings → Images & Art**:

| Setting | Starting point / action | Why |
|---|---|---|
| Image Warm Queue | On | Uses one bounded queue for offered artwork. |
| Image Warm Queue Depth | Keep `50000` initially | A larger backlog is not the same as faster downloads. Work dropped from a full queue can be filled on demand. |
| Image Warm Concurrency (min) | Keep `4` initially | Lower bound for the adaptive warmer. |
| Image Warm Concurrency (max) | Keep the default `48` if browsing stays responsive; try `24` if it slows during warming | Reducing background work can improve foreground responsiveness, but the warm takes longer. These values are not universal hardware targets. |
| Image Warm Target Lag (ms) | Keep `20` | Lets the warmer back off when the event loop is busy. |
| Image Fetch Concurrency | Keep its existing/default value initially | Controls simultaneous uncached downloads. Increasing it can overload providers or your connection. |
| Image Warm Proxy Base | Normally blank | Lets rendered-image warming use the instance's loopback address. |
| Log Every Image Request | Off except for short debugging sessions | Avoids excessive logging during bulk image activity. |

Leave connection-pool, TLS-session, scan-concurrency and stream-threshold settings at their defaults unless measurements identify a problem they address. More cores and RAM do not remove provider rate limits or network bottlenecks.

## 13. Check warming progress and solve problems

Use **Dashboard → Ops** for cache sizes and warming progress. Use **System** for memory and event-loop delay, and **Logs** for the reason a request failed. Do not confuse the metadata/Redis hit rate with the image cache's effectiveness.

### Understand the image counters

| Counter / symptom | Meaning and next step |
|---|---|
| Images seen | Artwork offered to the warmer. It is not a count of successfully stored files. |
| Fetched | Images successfully fetched by the warming path. |
| Already cached | Fresh images did not need another fetch. This is useful work avoided. |
| Rendered | Artwork prepared through a rendering path, such as an overlaid poster. |
| Over capacity | In the checked implementation, the disk image cache is at least 98% of its configured budget, so new warm work is skipped to avoid churning the cache. Increase the disk budget if space permits, or warm less artwork. |
| Dropped / queue full | The outstanding image queue reached its limit. Reduce how much content you offer at once before raising the queue depth. |
| Failed / timeout | The fetch or render did not complete. Inspect the provider and error; repeatedly pressing Force can add more load. |

These counters describe different paths and may include repeated offers. Do not add them together and assume they must equal the disk image count. Catalog progress can finish before the image queue drains.

### A simple before-and-after check

1. Open a collection and record how long its images take to appear.
2. Revisit it without clearing caches. Repeat browsing should benefit from already cached content.
3. Run one chosen warm and check whether the disk budget, failed requests or queue are limiting it.
4. Change one setting, repeat the same browse, and compare responsiveness as well as warming speed.
5. If foreground browsing slows, reduce the warm's scope or concurrency, or protect those hours with quiet hours.

### Refresh a problem image without starting over

Use **Ops → Image Cache → Refresh an image…** or **Clear art by ID…** for targeted corrections. A metadata-cache clear and an image-cache clear affect different stored data. **Clear All Images** removes the benefit of the existing image cache and causes new fetches as images are used; it is not a routine speed optimization.

The **Stop**, **Stop All Warming**, **Essential Warming**, **MAL Warming** and **Comprehensive** controls are operational actions, not a replacement for choosing persistent mode and interval settings. Check the task status after using them; do not assume a manual stop changes what will run after a restart.

**Recommended first setup:** enable the relevant image cache classes, use smaller TMDB tile artwork where it looks good, choose essential warming or a limited comprehensive run, and increase coverage only after checking the result.
