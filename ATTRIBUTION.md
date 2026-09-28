# Attribution and scope

AIOMetadata, Nuvio and Fusion names and interfaces belong to their respective projects. Screenshot artwork and featured layouts retain their creators' rights.

The featured gallery shown in this guide credits Starter Kit to Renoria, Ninja Streams to RandomNinjaAtk, Callandt95 to Callandt, Snoak to snoak, TVGenie to tvgeniekodi, and Unified Media Experience to nobnobz. The worked featured example uses TVGenie's Movie Categories.

Screenshots were captured from a signed-out demonstration draft. No personal account configuration was saved or published. Public creator handles are attribution, not the guide author's personal account details.

This guide is independent and documents the observed v3.2.0 interface. It is not a verification of every client import path or provider integration.

## Image caching and warming references

The warming chapters were checked against upstream commit `44bacb1bd4a9e80ac27749419822b0e441f560d4` on September 28, 2026, plus the dashboard control descriptions. Suggested tuning values are guide recommendations, not measured guarantees.

- [Settings and defaults](https://github.com/cedya77/aiometadata/blob/44bacb1bd4a9e80ac27749419822b0e441f560d4/addon/lib/settingsRegistry.ts)
- [Comprehensive catalog warmer](https://github.com/cedya77/aiometadata/blob/44bacb1bd4a9e80ac27749419822b0e441f560d4/addon/lib/comprehensiveCatalogWarmer.js)
- [Image warm queue and capacity checks](https://github.com/cedya77/aiometadata/blob/44bacb1bd4a9e80ac27749419822b0e441f560d4/addon/lib/posterCache/warmQueue.ts)
- [Essential and popular warming](https://github.com/cedya77/aiometadata/blob/44bacb1bd4a9e80ac27749419822b0e441f560d4/addon/lib/cacheWarmer.js)
- [MAL warming](https://github.com/cedya77/aiometadata/blob/44bacb1bd4a9e80ac27749419822b0e441f560d4/addon/lib/malCatalogWarmer.js)
