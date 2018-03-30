#!/usr/bin/python3
"""
commit.py - what the commit
author: mutantmonkey <mutantmonkey@mutantmonkey.in>
"""

import web
from tools import GrumbleError


def commit(phenny, input):
    """.commit - Get a What the Commit commit message."""

    msg = web.get("http://whatthecommit.com/index.txt")
    phenny.reply(msg)
commit.commands = ['commit']

if __name__ == '__main__':
    print(__doc__.strip())
