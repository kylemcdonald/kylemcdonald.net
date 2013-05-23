from string import Template
import os
import datetime
import time
import re

os.system("perl Markdown.pl --html4tags content.md > content.html")
c = open("content.html", "r")
o = open("outline.html", "r")
s = open("index.html", "w")
now = datetime.datetime.now()
s.write(Template(o.read()).substitute(content = c.read()))
os.system("rm content.html")