from pathlib import Path
import re,html,base64,zipfile,shutil,struct
p=Path(__file__).parent
src=(p/'Collection-Builder-Guide.md').read_text()
for bad in ['192.168.','/home/','d9fcc103','access_token=','api_key=']:
 assert bad.lower() not in src.lower(),bad
imgs=re.findall(r'!\[[^\]]*\]\(([^)]+)\)',src)
assert all((p/x).is_file() for x in imgs)
def slug(s):return re.sub(r'[^\w\- ]','',s.lower()).replace(' ','-')
def inline(s):
 s=html.escape(s)
 s=re.sub(r'`([^`]+)`',r'<code>\1</code>',s)
 s=re.sub(r'\*\*([^*]+)\*\*',r'<strong>\1</strong>',s)
 s=re.sub(r'\[([^]]+)\]\((#[^)]+)\)',r'<a href="\2">\1</a>',s)
 return s
headings=[(slug(t),t) for t in re.findall(r'^## (.*)$',src,re.M)]
ids=set(slug(t) for t in re.findall(r'^#{1,3} (.*)$',src,re.M))
for anchor in re.findall(r'\]\(#([^)]+)\)',src):assert anchor in ids,anchor
def render(embedded):
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
   out.append(f'<figure><img loading="eager" width="{width}" height="{height}" alt="'+html.escape(m[1],quote=True)+'" src="'+path+'"><figcaption>'+html.escape(m[1])+'</figcaption></figure>');i+=1;continue
  m=re.match(r'(#{1,3}) (.*)',s)
  if m:
   n=len(m[1]);out.append(f'<h{n} id="{slug(m[2])}">'+inline('Collection Builder Guide' if n==1 else m[2])+f'</h{n}>')
   if n==1 and not embedded:out.append('<div class="download"><a href="Collection-Builder-Guide.md">Read Markdown</a><a href="Collection-Builder-Guide.html" download>Download offline guide</a><a href="#10-quick-troubleshooting">Find a fix</a></div>')
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
 nav='<aside class="sidebar"><details open><summary>On this page</summary><nav aria-label="Guide sections">'+''.join('<a href="#'+a+'">'+html.escape(t)+'</a>' for a,t in headings)+'</nav></details><script>if(matchMedia("(max-width:720px)").matches)document.querySelector(".sidebar details").open=false;</script></aside>'
 header='<header class="app-header"><a class="brand" href="#main"><svg aria-hidden="true" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"><path d="m12 3 10 5-10 5L2 8l10-5Z"/><path d="m2 12 10 5 10-5M2 16l10 5 10-5"/></svg><div><div class="brand-name">AIOMetadata</div><div class="brand-subtitle">Community guide · Collections &amp; Widgets</div></div></a><a class="repo-link" href="https://github.com/cedya77/aiometadata">GitHub</a></header>'
 return '<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="description" content="A practical illustrated guide to AIO Metadata catalogs, collections, Nuvio and Fusion layouts, saving, sharing and troubleshooting."><title>AIO Metadata Collection Builder Guide</title>'+css+'</head><body><a class="skip" href="#main">Skip to guide</a>'+header+'<div class="shell">'+nav+'<main id="main">'+content+'<script>if("IntersectionObserver" in window){const links=[...document.querySelectorAll(".sidebar nav a")];const observer=new IntersectionObserver(entries=>{for(const e of entries){if(e.isIntersecting){for(const a of links){if(a.hash==="#"+e.target.id)a.setAttribute("aria-current","location");else a.removeAttribute("aria-current");}}}},{rootMargin:"0px 0px -65% 0px"});document.querySelectorAll("main h2").forEach(h=>observer.observe(h));}</script><footer><a class="back" href="#main">Back to top</a></footer></main></div></body></html>'
(p/'index.html').write_text(render(False))
(p/'Collection-Builder-Guide.html').write_text(render(True))
# The publication directory is allowlisted: no drafts, logs, account exports or unrelated files.
repo=p/'github-ready';repo.mkdir(exist_ok=True)
files=['README.md','Collection-Builder-Guide.md','index.html','guide.css','Collection-Builder-Guide.html','build.py','CONTRIBUTING.md','ATTRIBUTION.md','.nojekyll','.gitignore']+list(dict.fromkeys(imgs))
for f in files:
 dest=repo/f;dest.parent.mkdir(exist_ok=True,parents=True);shutil.copy2(p/f,dest)
with zipfile.ZipFile(p/'Collection-Builder-Guide.zip','w',zipfile.ZIP_DEFLATED) as z:
 for f in files:z.write(repo/f,'collection-builder-guide/'+f)
print('Built dark guide, offline edition and GitHub package with',len(imgs),'screenshots.')
