#!/usr/bin/env python3
"""
set-domain.py — put your real site address into every canonical / og:url / hreflang /
sitemap / robots reference, in one step.

Usage (from anywhere):
    python3 set-domain.py https://your-site.netlify.app
    python3 set-domain.py https://www.yourdomain.com --from https://your-site.netlify.app

It edits the site that sits one folder above this script (the folder with index.html).
Then re-upload the site folder to Netlify.
"""
import argparse, os, re, sys

DEFAULT_OLD = "https://ahmadzaheer.dev"

def main():
    ap = argparse.ArgumentParser(description="Set the site's public address.")
    ap.add_argument("new", help="new address, e.g. https://your-site.netlify.app")
    ap.add_argument("--from", dest="old", default=DEFAULT_OLD, help="address currently in the files")
    ap.add_argument("--root", default=os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."),
                    help="site folder (default: the folder above this script)")
    a = ap.parse_args()

    new = a.new.strip().rstrip("/")
    old = a.old.strip().rstrip("/")
    if not re.fullmatch(r"https://[A-Za-z0-9.-]+\.[A-Za-z]{2,}(:\d+)?", new):
        sys.exit("The new address must look like https://your-site.netlify.app (https, no path).")
    root = os.path.abspath(a.root)
    if not os.path.isfile(os.path.join(root, "index.html")):
        sys.exit(f"No index.html in {root} — pass --root pointing at the site folder.")

    changed = 0
    for dirpath, dirnames, files in os.walk(root):
        dirnames[:] = [d for d in dirnames if not d.startswith("_")]   # skip _extras
        for f in files:
            if not f.endswith((".html", ".xml", ".txt", ".json", ".js")):
                continue
            p = os.path.join(dirpath, f)
            with open(p, encoding="utf-8") as fh:
                s = fh.read()
            if old in s:
                with open(p, "w", encoding="utf-8") as fh:
                    fh.write(s.replace(old, new))
                changed += 1
    print(f"Done: {old}  ->  {new}   ({changed} files updated)")

if __name__ == "__main__":
    main()
