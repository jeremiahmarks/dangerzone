#!/usr/bin/env python
# -*- coding: utf-8 -*-

import markdown
import codecs
import datetime
 
inf='/home/jlmarks/mycode/mynotes/software notes/markdown.md'
outf='/home/jlmarks/'+str(datetime.datetime.now().time())+'.html'

textin=codecs.open(inf, mode="r", encoding="utf-8").read()

html = markdown.markdown(textin, ['extra'])

htmlout=codecs.open(outf,'w',encoding='utf-8',errors="xmlcharrefreplace")

htmlout.write(html)