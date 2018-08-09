#!/usr/bin/python3
"""
mylife.py - various commentary on life
author: Ramblurr <unnamedrambler@gmail.com>
author: mutantmonkey <mutantmonkey@mutantmonkey.in>
"""

from tools import GrumbleError
import web
import lxml.html
from random import choice


def fml(phenny, input):
    """.fml - Grab something from fmylife.com."""
    req = web.get("http://www.fmylife.com/random")
    doc = lxml.html.fromstring(req)
    quote = choice(doc.xpath(".//p[@class = 'block hidden-xs']")).text_content().strip()
    phenny.say(quote)
fml.commands = ['fml']


def mlia(phenny, input):
    """.mlia - My life is average."""
    req = web.get("http://mylifeisaverage.com/")
    doc = lxml.html.fromstring(req)
    quote = choice(doc.find_class('story')).text_content().strip()
    phenny.say(quote)
mlia.commands = ['mlia']


if __name__ == '__main__':
    print(__doc__.strip())
