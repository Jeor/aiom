"""Shared presentation for the static guides; source Markdown stays readable."""
import re, html
OVERVIEWS={
 'Catalog Management':'Choose your sources, control where catalogs appear, and organize them with tags.',
 'Collections':'Build folders and rows from your catalogs, then export the layout to your app.',
 'Caching & Warming':'Cache artwork for repeat visits and prepare useful content before people browse.',
 'Jellyfin & Profiles':'Connect your player and give each person their own catalogs, trackers and playback source.'}
CHECKS={
 'Catalog Management':['Your intended catalogs are enabled.','Home visibility and tags match your plan.','The configuration is saved and the catalogs open in your app.'],
 'Collections':['Every folder has the intended sources.','The design is saved in AIOMetadata.','The exported layout is imported and opens correctly in your app.'],
 'Caching & Warming':['Settings are saved and any required restart is complete.','A repeat visit loads the artwork successfully.','Disk use and provider errors remain acceptable during a limited warm.'],
 'Jellyfin & Profiles':['The client connects as the intended user.','Catalogs, tracker accounts and playback source match that user.','A title opens and plays through the configured stream addon.']}
NEXT={'Catalog Management':('Collections','collections.html','Arrange your sources into folders and rows.'),'Collections':('Caching & Warming','caching-warming.html','Prepare artwork for smoother browsing.'),'Caching & Warming':('Jellyfin & Profiles','jellyfin.html','Set up users and connect a Jellyfin-compatible player.'),'Jellyfin & Profiles':('Catalog Management','catalogs.html','Refine the catalog sources and tags your profiles use.')}
def polish(content,label,stem,help_anchor,embedded,pages):
 prefix,rest=content.split('<section class="guide-section">',1)
 title_id=re.search(r'<h1 id="([^"]+)"',prefix)[1]
 prefix=re.sub(r'<h1.*?</h1>|<p class="reading-hint">.*?</p>|<div class="download">.*?</div>','',prefix,flags=re.S)
 # The concise overview replaces the first introductory paragraph, not the instructions.
 prefix=re.sub(r'<p>.*?</p>','',prefix,count=1,flags=re.S)
 prefix=re.sub(r'<p><strong>Visuals:</strong>.*?</p>','',prefix,flags=re.S)
 resources=f'<details class="resources"><summary>Downloads</summary><div><a href="{stem}.md">Markdown</a><a href="{stem}.html" download>Offline HTML</a></div></details>'
 header=f'<header class="guide-heading"><p class="eyebrow">COMMUNITY GUIDE</p><h1 id="{title_id}">{html.escape(label)}</h1><p class="guide-lead">{OVERVIEWS[label]}</p><div class="guide-tools"><a href="#{help_anchor}">Find a fix ↗</a>{resources}<button id="expand-details" type="button">Expand all details</button></div></header>'
 content=header+prefix+'<section class="guide-section">'+rest
 # Use choice cards only for decision tables; preserve real side-by-side comparisons.
 def table(m):
  raw=m[0]; heads=re.findall(r'<th\b[^>]*>(.*?)</th>',raw,re.S)
  rows=[re.findall(r'<td>(.*?)</td>',r,re.S) for r in re.findall(r'<tbody>(.*?)</tbody>',raw,re.S)[0].split('</tr>')]
  rows=[r for r in rows if r]
  if heads and heads[0] in ['Your setup','What you want','Who is this profile for?']:
   return '<div class="choice-cards">'+''.join('<article class="choice-card"><h3>'+r[0]+'</h3>'+''.join('<p><span class="field-label">'+h+'</span>'+v+'</p>' for h,v in zip(heads[1:],r[1:]))+'</article>' for r in rows)+'</div>'
  if heads and heads[0] in ['Problem','Question'] and len(heads)==2:
   return '<div class="help-list">'+''.join('<details class="help-item"><summary>'+r[0]+'</summary><div>'+r[1]+'</div></details>' for r in rows)+'</div>'
  return raw
 content=re.sub(r'<div class="table-wrap".*?</table></div>',table,content,flags=re.S)
 def note(m):
  first=m[1]; kind='Remember'
  if first.startswith(('Example','Typical sequence')):kind='Example'
  elif first.startswith(('Success check','Success')):kind='Check'
  return '<aside class="callout"><span class="callout-label">'+kind+'</span><p>'+m[0][3:-4]+'</p></aside>'
 content=re.sub(r'<p><strong>((?:Remember:|Important:|Common setup:|A tag describes|Adding by tag|No tags selected|Separate catalogs|For a local-only|Two different saves:|Success check:|Typical sequence:|Saving in AIO|Keep the address)[^<]*)</strong>.*?</p>',note,content,flags=re.S)
 nextlabel,nextroute,desc=NEXT[label]
 if embedded:nextroute=next(q[0]+'.html' for q in pages if q[2]==nextlabel)
 ending='<section class="finish"><p class="eyebrow">BEFORE YOU MOVE ON</p><h2>Check your setup</h2><ul>'+''.join('<li>'+x+'</li>' for x in CHECKS[label])+'</ul><a class="next-guide" href="'+nextroute+'"><span><small>Next guide</small><strong>'+nextlabel+'</strong><span>'+desc+'</span></span><b aria-hidden="true">→</b></a></section>'
 return content+ending
