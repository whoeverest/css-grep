#!/usr/bin/env python2
from __future__ import absolute_import, division, print_function

import sys
from lxml.html import fromstring, tostring
from lxml.cssselect import CSSSelector

if len(sys.argv) < 2:
  print('Usage:\n  cat example.html | cssgrep "a.something > div"')
  exit(1)

content = sys.stdin.read() or ''
parsed = fromstring(content)
selector = CSSSelector(sys.argv[1])
results = selector(parsed)

for node in results:
  print(tostring(node, encoding='unicode').strip())
