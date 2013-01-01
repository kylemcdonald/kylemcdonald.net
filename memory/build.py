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
contentSub = Template(c.read()).substitute(lastupdated = now.strftime("%A, %B %d, %Y"))
contentSub = re.sub(r"First", "<img src='1st.png' class='badge'/>", contentSub)
contentSub = re.sub(r" with ", "<img src='with.png' class='badge'/>", contentSub)
contentSub = re.sub(r" at ", "<img src='at.png' class='badge'/>", contentSub)
s.write(Template(o.read()).substitute(content = contentSub))
os.system("rm content.html")