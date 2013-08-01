#!/usr/bin/env python

import pandoc



pandoc.PANDOC_PATH = '/usr/bin/pandoc'

s = open("test.markdown", 'r').read()

doc = pandoc.Document()

doc.markdown = s

doc.to_file("output.epub")