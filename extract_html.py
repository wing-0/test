import lxml
from lxml import html
from lxml.etree import tostring
import requests
import re

wp = input('web address: ')
xp = input('xpath: ')
fn = input('filename: ')

# Open webpage, get html tree and find the requested xpath
page = requests.get(wp)
tree = html.fromstring(page.content)
text = tree.xpath(xp)[0]

# Write to file
f = open(fn + '.html','w')
f.write(tostring(text, method='html').decode('utf-8'))
f.close()