from string import Template
import os
import datetime
import time

os.system('python -m markdown story.md > content.html')
content = open('content.html').read()
outline = open('outline.html').read()

now = datetime.datetime.now()
with open('index.html', 'w') as f:
  outline = outline.replace('${content}', content)
  f.write(outline)