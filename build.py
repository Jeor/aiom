from pathlib import Path
import re,html,base64,zipfile,shutil,struct
p=Path(__file__).parent
pages=[('Collection-Builder-Guide','index.html','Collections','10-quick-troubleshooting'),('Caching-Warming-Guide','caching-warming.html','Caching & Warming','which-setting-should-i-check')]
imgs=[]
def slug(s):return re.sub(r'[^\w\- ]','',s.lower()).replace(' ','-')
def inline(s):
 s=html.escape(s)
 s=re.sub(r'`([^`]+)`',r'<code>\1</code>',s)
 s=re.sub(r'\*\*([^*]+)\*\*',r'<strong>\1</strong>',s)
 s=re.sub(r'\[([^]]+)\]\(([^)]+)\)',r'<a href="\2">\1</a>',s)
 return s
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
   path='data:image/png;base64,'+base64.b64encode((p/m[2]).read_bytes()).decode() if embedded else m[2]
   width,height=struct.unpack('>II',(p/m[2]).read_bytes()[16:24])
   out.append(f'<figure><button class="screenshot-open" type="button" aria-label="Enlarge screenshot"><img loading="eager" width="{width}" height="{height}" alt="'+html.escape(m[1],quote=True)+'" src="'+path+'"></button><figcaption>'+html.escape(m[1])+'</figcaption></figure>');i+=1;continue
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
 def subsections(part):
  pieces=re.split(r'(?=<h3 )',part)
  return pieces[0]+''.join('<div class="guide-subsection">'+piece+'</div>' for piece in pieces[1:])
 content=sections[0]+''.join('<section class="guide-section" aria-labelledby="'+re.search(r'id="([^"]+)"',part)[1]+'">'+subsections(part)+'</section>' for part in sections[1:])
 css='<style>'+(p/'guide.css').read_text()+'</style>' if embedded else '<link rel="stylesheet" href="guide.css">'
 page_nav='<nav class="guide-pages" aria-label="Guide pages">'+''.join('<a href="'+(q[0]+'.html' if embedded else q[1])+'"'+(' aria-current="page"' if q==page else '')+'>'+html.escape(q[2])+'</a>' for q in pages)+'</nav>'
 nav='<aside class="sidebar">'+page_nav+'<details open><summary>On this page</summary><nav aria-label="Guide sections">'+''.join('<a href="#'+a+'">'+html.escape(t)+'</a>' for a,t in headings)+'</nav></details><script>if(matchMedia("(max-width:720px)").matches)document.querySelector(".sidebar details").open=false;</script></aside>'
 header='<header class="app-header"><a class="brand" href="#main"><svg aria-hidden="true" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"><path d="m12 3 10 5-10 5L2 8l10-5Z"/><path d="m2 12 10 5 10-5M2 16l10 5 10-5"/></svg><div><div class="brand-name">AIOMetadata</div><div class="brand-subtitle">Community guides</div></div></a><a class="repo-link" href="https://github.com/cedya77/aiometadata">GitHub</a></header>'
 lightbox='<dialog class="image-viewer" aria-label="Enlarged screenshot"><button class="image-close" autofocus>Close</button><img alt=""></dialog><script>const viewer=document.querySelector(".image-viewer");document.querySelectorAll(".screenshot-open").forEach(button=>button.addEventListener("click",()=>{const source=button.querySelector("img");const image=viewer.querySelector("img");image.src=source.src;image.alt=source.alt;viewer.showModal();}));viewer.querySelector("button").addEventListener("click",()=>viewer.close());viewer.addEventListener("click",event=>{if(event.target===viewer)viewer.close();});</script>'
 return '<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="description" content="A practical illustrated guide to AIO Metadata catalogs, collections, Nuvio and Fusion layouts, saving, sharing and troubleshooting."><title>AIO Metadata — '+html.escape(label)+'</title>'+css+'</head><body><a class="skip" href="#main">Skip to guide</a>'+header+'<div class="shell">'+nav+'<main id="main">'+content+lightbox+'<script>if("IntersectionObserver" in window){const links=[...document.querySelectorAll(".sidebar details nav a")];const observer=new IntersectionObserver(entries=>{for(const e of entries){if(e.isIntersecting){for(const a of links){if(a.hash==="#"+e.target.id)a.setAttribute("aria-current","location");else a.removeAttribute("aria-current");}}}},{rootMargin:"0px 0px -65% 0px"});document.querySelectorAll("main h2").forEach(h=>observer.observe(h));}</script><footer><a class="back" href="#main">Back to top</a></footer></main></div></body></html>'
for page in pages:
 src=(p/(page[0]+'.md')).read_text()
 for bad in ['192.168.','/home/','d9fcc103','access_token=','api_key=']:
  assert bad.lower() not in src.lower(),bad
 ids={slug(t) for t in re.findall(r'^#{1,3} (.*)$',src,re.M)}
 for anchor in re.findall(r'\]\(#([^)]+)\)',src):assert anchor in ids,anchor
 imgs+=re.findall(r'!\[[^\]]*\]\(([^)]+)\)',src)
 online=render(src,page,False)
 if page[1]=='index.html':
  redirects={'11-cache-images-for-faster-repeat-browsing':'image-caching','12-choose-a-warming-mode':'warming-modes','13-check-warming-progress-and-solve-problems':'progress-and-troubleshooting'}
  import json
  script='<script>const moved='+json.dumps(redirects)+';if(moved[location.hash.slice(1)])location.replace("caching-warming.html#"+moved[location.hash.slice(1)]);</script>'
  online=online.replace('</head>',script+'</head>')
 (p/page[1]).write_text(online)
 (p/(page[0]+'.html')).write_text(render(src,page,True))
assert all((p/x).is_file() for x in imgs)
# Only curated guide files and referenced screenshots enter the publication package.
repo=p/'github-ready';repo.mkdir(exist_ok=True)
files=['README.md','guide.css','build.py','CONTRIBUTING.md','ATTRIBUTION.md','.nojekyll','.gitignore']
for page in pages:files += [page[0]+'.md',page[0]+'.html',page[1]]
files+=list(dict.fromkeys(imgs))
for f in files:
 dest=repo/f;dest.parent.mkdir(exist_ok=True,parents=True);shutil.copy2(p/f,dest)
with zipfile.ZipFile(p/'Collection-Builder-Guide.zip','w',zipfile.ZIP_DEFLATED) as z:
 for f in files:z.write(repo/f,'collection-builder-guide/'+f)
print('Built',len(pages),'guide pages, offline editions and package with',len(set(imgs)),'screenshots.')
