"""Notify Bing (and other IndexNow engines) about new or changed pages.

Usage:
  python tools/indexnow.py                 # every URL in sitemap.xml
  python tools/indexnow.py URL [URL ...]   # only these URLs
"""
import json, pathlib, re, sys, urllib.request

ROOT = pathlib.Path(__file__).resolve().parent.parent
HOST = 'iacleaner.com'
key_files = [p for p in ROOT.glob('*.txt') if re.fullmatch(r'[0-9a-f]{32}\.txt', p.name)]
if len(key_files) != 1:
    sys.exit('Expected exactly one IndexNow key file (32 hex chars + .txt) in the site root.')
KEY = key_files[0].stem

urls = sys.argv[1:] or re.findall(r'<loc>([^<]+)</loc>', (ROOT / 'sitemap.xml').read_text(encoding='utf-8'))
body = json.dumps({'host': HOST, 'key': KEY, 'keyLocation': f'https://{HOST}/{KEY}.txt', 'urlList': urls}).encode()
req = urllib.request.Request('https://api.indexnow.org/indexnow', data=body,
                             headers={'Content-Type': 'application/json; charset=utf-8'})
try:
    with urllib.request.urlopen(req, timeout=30) as r:
        print(f'{r.status} {r.reason}: {len(urls)} URLs submitted')
except urllib.error.HTTPError as e:
    print(f'{e.code} {e.reason}: {e.read().decode(errors="ignore")[:300]}')
    sys.exit(1)
