# phenny
[![Build Status](https://travis-ci.org/apertium/phenny.png?branch=master)](https://travis-ci.org/apertium/phenny)
[![Coverage Status](https://coveralls.io/repos/github/apertium/phenny/badge.svg?branch=master)](https://coveralls.io/github/apertium/phenny?branch=master)

This is phenny, a Python IRC bot. Originally written by Sean B. Palmer, it has
been ported to Python3.

This version comes with many new modules, IPv6 support, TLS support, and unit
tests.

Compatibility with existing phenny modules has been mostly retained, but they
will need to be updated to run on Python3 if they do not already. All of the
core modules have been ported, removed, or replaced.

## Requirements
* Python 3.5+
* [python-requests](http://docs.python-requests.org/en/latest/)

## Installation
1. Run `./phenny` - this creates a default config file
2. Edit `~/.phenny/default.py`
3. Run `./phenny` - this now runs phenny with your settings

Enjoy!

## Testing
You will need the Python3 versions of `python-nose` and `python-mock`. To run
the tests, simply run `nosetests3`.

## Security
You may want to disable `pester`. It can be used to crash the bot with no admin permissions needed.

    <botname>: pester <botname> tell <anyone> <anything>

You may also want to disable `update`. Due to a known bug, spamming `.update` repeatedly makes the process go into the background.

## Authors
* Sean B. Palmer, http://inamidst.com/sbp/
* mutantmonkey, http://mutantmonkey.in
* Apertium developers, especially GCI students
