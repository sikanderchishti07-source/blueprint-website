# Reads blog posts and careers from content/*.md so the owner can edit them
# without touching Python. Each file has a small YAML-style header followed
# by the body.

import os, re, glob, datetime

ROOT = os.path.join(os.path.dirname(__file__), '..', 'content')


def _parse(path):
    """Split a Markdown file into its header fields and body."""
    raw = open(path, encoding='utf-8').read().lstrip('\ufeff')
    meta, body = {}, raw
    if raw.startswith('---'):
        end = raw.find('\n---', 3)
        if end != -1:
            head = raw[3:end]
            body = raw[end + 4:]
            for line in head.splitlines():
                if ':' not in line:
                    continue
                k, v = line.split(':', 1)
                v = v.strip()
                if len(v) > 1 and v[0] == v[-1] and v[0] in '"\'':
                    v = v[1:-1]
                meta[k.strip()] = v
    meta['slug'] = os.path.splitext(os.path.basename(path))[0]
    meta['body'] = body.strip()
    return meta


def _to_html(md):
    """Minimal Markdown for what the CMS editor produces. Anything already
    written as HTML passes straight through untouched."""
    if '<p' in md or '<h2' in md or '<div' in md:
        return md                                  # already HTML, leave it
    out, para = [], []

    def flush():
        if para:
            out.append('<p class="mb-5 leading-relaxed text-gray-700">'
                       + ' '.join(para) + '</p>')
            para.clear()

    for line in md.splitlines():
        s = line.strip()
        if not s:
            flush(); continue
        if s.startswith('### '):
            flush(); out.append('<h3 class="font-display text-lg font-bold text-bp-ink mt-8 mb-3">'
                                + s[4:] + '</h3>')
        elif s.startswith('## '):
            flush(); out.append('<h2 class="font-display text-2xl font-bold text-bp-ink mt-10 mb-4 tracking-tight">'
                                + s[3:] + '</h2>')
        elif s.startswith('- '):
            flush(); out.append('<li class="mb-2 text-gray-700">' + s[2:] + '</li>')
        else:
            para.append(s)
    flush()
    html = '\n'.join(out)
    # wrap loose list items
    html = re.sub(r'(<li[^>]*>.*?</li>\n?)+',
                  lambda m: '<ul class="list-disc pl-6 mb-5">' + m.group(0) + '</ul>',
                  html, flags=re.S)
    # **bold** and [text](url)
    html = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', html)
    html = re.sub(r'\[(.+?)\]\((.+?)\)',
                  r'<a href="\2" class="text-bp-primary underline">\1</a>', html)
    return html


def _sortkey(d):
    """Newest first, whatever format the date was written in."""
    v = str(d.get('date', '')).strip()
    for f in ('%Y-%m-%d', '%B %d, %Y', '%d %B %Y', '%d/%m/%Y'):
        try:
            return datetime.datetime.strptime(v, f)
        except ValueError:
            pass
    return datetime.datetime.min


def load_blog():
    items = [_parse(p) for p in glob.glob(os.path.join(ROOT, 'blog', '*.md'))]
    items = [i for i in items if i.get('title')]
    items.sort(key=_sortkey, reverse=True)
    for i in items:
        i['html'] = _to_html(i['body'])
        i.setdefault('category', 'Insight')
        i.setdefault('read', '')
        i.setdefault('summary', '')
        i.setdefault('image', 'assets/img/card-1.jpg')
        # the page templates were written against these key names
        i['img']     = i['image']
        i['fb']      = i['image']
        i['cat']     = i['category']
        i['excerpt'] = i['summary']
    return items


def load_careers():
    items = [_parse(p) for p in glob.glob(os.path.join(ROOT, 'careers', '*.md'))]
    items = [i for i in items if i.get('title')]
    # closed vacancies stay in the folder but drop off the site
    items = [i for i in items if str(i.get('status', 'open')).lower() != 'closed']
    items.sort(key=_sortkey, reverse=True)
    for i in items:
        i['html'] = _to_html(i['body'])
        i.setdefault('location', 'Riyadh, Saudi Arabia')
        i.setdefault('type', 'Full time')
        i.setdefault('department', '')
        i.setdefault('summary', '')
    return items
