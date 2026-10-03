from pathlib import Path
import re,html,base64,zipfile,shutil,struct,json
from layout import polish
from PIL import Image
p=Path(__file__).parent
pages=[('Catalog-Management-Guide','catalogs.html','Catalog Management','common-tag-questions'),('Collection-Builder-Guide','collections.html','Collections','10-quick-troubleshooting'),('Caching-Warming-Guide','caching-warming.html','Caching & Warming','which-setting-should-i-check'),('Jellyfin-Guide','jellyfin.html','Jellyfin & Profiles','troubleshooting')]
imgs=[]
SITE_HEADER='<header class="app-header"><a class="brand" href="index.html"><svg aria-hidden="true" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"><path d="m12 3 10 5-10 5L2 8l10-5Z"/><path d="m2 12 10 5 10-5M2 16l10 5 10-5"/></svg><div><div class="brand-name">AIOMetadata</div><div class="brand-subtitle">Community guides</div></div></a><nav class="header-links" aria-label="Project links"><a class="repo-link" href="https://github.com/cedya77/aiometadata">GitHub</a><a class="coffee-link" href="https://buymeacoffee.com/cedya" aria-label="Support the AIOMetadata creator on Buy Me a Coffee" title="Support the AIOMetadata creator"><svg aria-hidden="true" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M18 8h1a3 3 0 0 1 0 6h-1M3 8h15v9a3 3 0 0 1-3 3H6a3 3 0 0 1-3-3V8ZM6 2v3M10 2v3M14 2v3"/></svg><span>Support the creator</span></a></nav></header>'
SITE_HEADER=SITE_HEADER.replace('<nav class="header-links"', '<button class="search-trigger" type="button" aria-haspopup="dialog">Search guides</button><nav class="header-links"')
def slug(s):return re.sub(r'[^\w\- ]','',s.lower()).replace(' ','-')
def inline(s):
 s=html.escape(s)
 s=re.sub(r'`([^`]+)`',r'<code>\1</code>',s)
 s=re.sub(r'\*\*([^*]+)\*\*',r'<strong>\1</strong>',s)
 s=re.sub(r'\[([^]]+)\]\(([^)]+)\)',r'<a href="\2">\1</a>',s)
 return s
def search_ui(embedded=False):
 entries=[]
 for stem,route,label,_ in pages:
  source=(p/(stem+'.md')).read_text()
  for match in re.finditer(r'^## ([^\n]+)\n(.*?)(?=^## |\Z)',source,re.M|re.S):
   title,body=match.groups()
   body=re.sub(r'!\[[^]]*\]\([^)]*\)','',body)
   body=re.sub(r'\[([^]]+)\]\([^)]*\)',r'\1',body)
   body=re.sub(r'[#*`|>]',' ',body)
   body=re.sub(r'\s+',' ',body).strip()
   entries.append(dict(guide=label,title=title,text=body,url=(stem+'.html' if embedded else route)+'#'+slug(title)))
 data=json.dumps(entries).replace('<','\\u003c')
 return '<script type="application/json" id="guide-search-data">'+data+'</script><script>'+ (p/'search.js').read_text()+'</script>'
def render(src, page, embedded):
 stem,route,label,help_anchor=page
 headings=[(slug(t),t) for t in re.findall(r'^## (.*)$',src,re.M)]
 for other in pages:
  src=src.replace('('+other[0]+'.md', '('+(other[0]+'.html' if embedded else other[1]))
 out=[];lines=src.splitlines();i=0
 while i<len(lines):
  s=lines[i]
  if not s.strip():i+=1;continue
  if s.startswith('|'):
   tab=[]
   while i<len(lines) and lines[i].startswith('|'):
    cells=[x.strip() for x in lines[i].strip('|').split('|')]
    if not all(re.fullmatch(r':?-+:?',x) for x in cells):tab.append(cells)
    i+=1
   out.append('<div class="table-wrap" tabindex="0" role="region" aria-label="Reference table"><table><thead><tr>'+''.join('<th scope="col">'+inline(c)+'</th>' for c in tab[0])+'</tr></thead><tbody>'+''.join('<tr>'+''.join('<td>'+inline(c)+'</td>' for c in row)+'</tr>' for row in tab[1:])+'</tbody></table></div>');continue
  m=re.match(r'!\[([^]]*)\]\(([^)]+)\)',s)
  if m:
   with Image.open(p/m[2]) as image:
    width,height=image.size
    mime=Image.MIME[image.format]
   path='data:'+mime+';base64,'+base64.b64encode((p/m[2]).read_bytes()).decode() if embedded else m[2]
   focus={'images/06-choose-catalog.png':(304,54,675,620),'images/07-build-folder.png':(374,200,840,407)}.get(m[2])
   if focus:
    x,y,w,h=focus
    out.append(f'<figure><button class="screenshot-open focused-shot" type="button" aria-label="Enlarge screenshot" style="aspect-ratio:{w}/{h}"><img style="position:absolute;max-width:none;width:{width/w*100}%;left:{-x/w*100}%;top:{-y/h*100}%;" width="{width}" height="{height}" alt="'+html.escape(m[1],quote=True)+'" src="'+path+'"></button><figcaption>'+html.escape(m[1])+' · Focused view; click for full screenshot.</figcaption>')
    if m[2].endswith('06-choose-catalog.png'):out.append('<figcaption class="shot-key"><span><b>2</b> Find the movie catalog in Your catalogs.</span><span><b>3</b> Tick the source, then choose Add 1.</span></figcaption>')
    else:out.append('<figcaption class="shot-key"><span><b>2</b> Name the collection.</span><span><b>3</b> Add a folder.</span><span><b>4</b> Give the folder its title.</span></figcaption>')
    out.append('</figure>');i+=1;continue
   out.append(f'<figure><button class="screenshot-open" type="button" aria-label="Enlarge screenshot"><img loading="lazy" width="{width}" height="{height}" alt="'+html.escape(m[1],quote=True)+'" src="'+path+'"></button><figcaption>'+html.escape(m[1])+'</figcaption></figure>');i+=1;continue
  m=re.match(r'(#{1,3}) (.*)',s)
  if m:
   n=len(m[1]);out.append(f'<h{n} id="{slug(m[2])}">'+inline(m[2])+f'</h{n}>')
   if n==1 and not embedded:out.append(f'<div class="download"><a href="{stem}.md">Read Markdown</a><a href="{stem}.html" download>Download offline guide</a><a href="#{help_anchor}">Find a fix</a></div>')
   i+=1;continue
  if s=='---':out.append('<hr>');i+=1;continue
  m=re.match(r'(?:\d+\. |\- )(.*)',s)
  if m:
   ordered=bool(re.match(r'\d',s));tag='ol' if ordered else 'ul';items=[];pat=r'\d+\. (.*)' if ordered else r'\- (.*)'
   while i<len(lines) and (m:=re.match(pat,lines[i])):items.append('<li>'+inline(m[1])+'</li>');i+=1
   out.append(f'<{tag}>'+''.join(items)+f'</{tag}>');continue
  out.append('<p>'+inline(s)+'</p>');i+=1
 content=''.join(out)
 sections=re.split(r'(?=<h2 )',content)
 # Keep the main path visible; references and optional branches open on demand.
 folded_sections={
  'Jellyfin & Profiles': {'connect-your-app','other-user-controls','troubleshooting'},
  'Collections': {'1-what-are-you-building','4-understand-the-editor','6-customize-folders-and-collections','7-fusion-example-a-normal-catalog-row','9-share-a-layout-without-sharing-your-account-link'},
  'Catalog Management': {'filter-select-and-manage-tags','use-tags-to-build-a-collection-faster','tagged-profiles-and-optional-content-ratings','common-tag-questions','example-make-a-source-then-put-it-in-a-folder','where-does-the-builder-get-its-catalog-list'},
  'Caching & Warming': {'save-and-verify-settings','image-caching','warming-modes','progress-and-troubleshooting'},
 }
 folded_subsections={'tracker-reads-versus-tracker-writes','watchlist-and-favourites','forget-imported-history','defaults-and-suggested-values','which-button-should-i-use','read-the-catalog-management-list','see-what-a-complete-layout-looks-like','d-find-a-source-directly-from-a-provider','e-check-the-finished-movie-night-example','updating-an-existing-layout','image-caching','my-folder-is-empty','i-saved-but-nothing-changed-in-my-app','i-cannot-save-or-cannot-see-a-genre-option','my-artwork-is-blank','other-problems'}
 def fold(part,level):
  heading,body=part.split(f'</h{level}>',1)
  return '<details class="reference"><summary>'+heading+f'</h{level}>'+'</summary><div class="reference-body">'+body+'</div></details>'
 def subsections(part):
  pieces=re.split(r'(?=<h3 )',part)
  result=pieces[0]
  for piece in pieces[1:]:
   ident=re.search(r'id="([^"]+)"',piece)[1]
   result+=fold(piece,3) if ident in folded_subsections else '<div class="guide-subsection">'+piece+'</div>'
  return result
 content=sections[0]+''.join('<section class="guide-section">'+(fold(subsections(part),2) if re.search(r'id="([^"]+)"',part)[1] in folded_sections[label] else subsections(part))+'</section>' for part in sections[1:])
 content=re.sub(r"(</h1>)", r'\1<p class="reading-hint">Follow the visible steps. Open a reference when you need more detail. <button type="button" id="expand-details">Expand all details</button></p>', content, count=1)
 content+='<script>const detailSections=[...document.querySelectorAll("main details.reference, main details.help-item")];const expandButton=document.getElementById("expand-details");expandButton.addEventListener("click",()=>{const expand=detailSections.some(d=>!d.open);detailSections.forEach(d=>d.open=expand);expandButton.textContent=expand?"Collapse all details":"Expand all details";});function revealSection(){const target=document.getElementById(decodeURIComponent(location.hash.slice(1)));if(!target)return;let ancestor=target.parentElement;while(ancestor){if(ancestor.tagName==="DETAILS")ancestor.open=true;ancestor=ancestor.parentElement;}requestAnimationFrame(()=>target.scrollIntoView());}addEventListener("hashchange",revealSection);if(location.hash)revealSection();addEventListener("beforeprint",()=>detailSections.forEach(d=>{d.dataset.wasOpen=d.open;d.open=true;}));addEventListener("afterprint",()=>detailSections.forEach(d=>d.open=d.dataset.wasOpen==="true"));</script>'
 content=polish(content,label,stem,help_anchor,embedded,pages)
 css='<style>'+(p/'guide.css').read_text()+'</style>' if embedded else '<link rel="stylesheet" href="guide.css">'
 page_nav='<nav class="guide-pages" aria-label="Guide pages"><a href="index.html">All guides</a>'+''.join('<a href="'+(q[0]+'.html' if embedded else q[1])+'"'+(' aria-current="page"' if q==page else '')+'>'+html.escape(q[2])+'</a>' for q in pages)+'</nav>'
 mobile='<label class="mobile-guide">Guide<select aria-label="Choose guide" onchange="location.href=this.value"><option value="index.html">All guides</option>'+''.join('<option value="'+(q[0]+'.html' if embedded else q[1])+'"'+(' selected' if q==page else '')+'>'+html.escape(q[2])+'</option>' for q in pages)+'</select></label>'
 nav='<aside class="sidebar">'+mobile+page_nav+'<details open><summary>On this page</summary><nav aria-label="Guide sections">'+''.join('<a href="#'+a+'">'+html.escape(t)+'</a>' for a,t in headings)+'</nav></details><script>if(matchMedia("(max-width:720px)").matches)document.querySelector(".sidebar details").open=false;</script></aside>'
 header=SITE_HEADER
 lightbox='<dialog class="image-viewer" aria-label="Enlarged screenshot"><button class="image-close" autofocus>Close</button><img alt=""></dialog><script>const viewer=document.querySelector(".image-viewer");document.querySelectorAll(".screenshot-open").forEach(button=>button.addEventListener("click",()=>{const source=button.querySelector("img");const image=viewer.querySelector("img");image.src=source.src;image.alt=source.alt;viewer.showModal();}));viewer.querySelector("button").addEventListener("click",()=>viewer.close());viewer.addEventListener("click",event=>{if(event.target===viewer)viewer.close();});</script>'
 return '<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="description" content="A practical illustrated guide to AIOMetadata catalogs, collections, Nuvio and Fusion layouts, saving, sharing and troubleshooting."><title>AIOMetadata — '+html.escape(label)+'</title>'+css+'</head><body><a class="skip" href="#main">Skip to guide</a>'+header+'<div class="shell">'+nav+'<main id="main">'+content+lightbox+'<script>if("IntersectionObserver" in window){const links=[...document.querySelectorAll(".sidebar details nav a")];const observer=new IntersectionObserver(entries=>{for(const e of entries){if(e.isIntersecting){for(const a of links){if(a.hash==="#"+e.target.id)a.setAttribute("aria-current","location");else a.removeAttribute("aria-current");}}}},{rootMargin:"0px 0px -65% 0px"});document.querySelectorAll("main h2").forEach(h=>observer.observe(h));}</script><footer><a class="back" href="#main">Back to top</a></footer></main></div>'+search_ui(embedded)+'</body></html>'
for page in pages:
 src=(p/(page[0]+'.md')).read_text()
 for bad in ['192.168.','/home/','d9fcc103','access_token=','api_key=']:
  assert bad.lower() not in src.lower(),bad
 ids={slug(t) for t in re.findall(r'^#{1,3} (.*)$',src,re.M)}
 for anchor in re.findall(r'\]\(#([^)]+)\)',src):assert anchor in ids,anchor
 imgs+=re.findall(r'!\[[^\]]*\]\(([^)]+)\)',src)
 online=render(src,page,False)
 (p/page[1]).write_text(online)
 (p/(page[0]+'.html')).write_text(render(src,page,True))
# Keep shared links to sections of the former index working.
redirects={slug(t):'collections.html#'+slug(t) for t in re.findall(r'^#{1,3} (.*)$',(p/'Collection-Builder-Guide.md').read_text(),re.M)}
for title in re.findall(r'^#{1,3} (.*)$',(p/'Catalog-Management-Guide.md').read_text(),re.M):
 key=slug(title)
 if key!='quick-start':redirects[key]='catalogs.html#'+key
redirects['catalogs-and-the-builder']='catalogs.html#catalog-controls'
for old,new in {'11-cache-images-for-faster-repeat-browsing':'image-caching','12-choose-a-warming-mode':'warming-modes','13-check-warming-progress-and-solve-problems':'progress-and-troubleshooting'}.items():redirects[old]='caching-warming.html#'+new
home=(p/'home-template.html').read_text().replace('{{HEADER}}',SITE_HEADER).replace('{{REDIRECTS}}',json.dumps(redirects))
(p/'index.html').write_text(home.replace('</body>',search_ui()+'</body>'))
assert all((p/x).is_file() for x in imgs)
# Only curated guide files and referenced screenshots enter the publication package.
repo=p/'github-ready';repo.mkdir(exist_ok=True)
files=['index.html','home-template.html','README.md','guide.css','build.py','layout.py','search.js','CONTRIBUTING.md','ATTRIBUTION.md','.nojekyll','.gitignore']
for page in pages:files += [page[0]+'.md',page[0]+'.html',page[1]]
files+=list(dict.fromkeys(imgs))
for f in files:
 dest=repo/f;dest.parent.mkdir(exist_ok=True,parents=True);shutil.copy2(p/f,dest)
with zipfile.ZipFile(p/'Collection-Builder-Guide.zip','w',zipfile.ZIP_DEFLATED) as z:
 for f in files:z.write(repo/f,'collection-builder-guide/'+f)
print('Built',len(pages),'guide pages, offline editions and package with',len(set(imgs)),'screenshots.')
