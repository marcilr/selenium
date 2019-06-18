#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# checkpage.py
#
# Created Tue Jun 18 11:02:34 AKDT 2019
# Copyright (C) 2019 by Raymond E. Marcil <marcilr@gmail.com>
#
# Check if web pages exists
#
#
# Links
# =====
# How to comment out a block of code in Python [duplicate]
# https://stackoverflow.com/questions/675442/how-to-comment-out-a-block-of-code-in-python
#
# Python check if website exists
# https://stackoverflow.com/questions/16778435/python-check-if-website-exists
#
# Python functions
# https://www.tutorialspoint.com/python/python_functions.htm
#
import urllib2


# =============
# Configuration
# =============

# List of websites to check
linksToCheckFile="links-to-check.txt"

# Single website to check
website='https://www.google.com'


# =========
# Functions
# =========



infile = open(linksToCheckFile, "r")

for aline in infile:
   print(aline)

infile.close()




# Use triple quotes to comment out block:
"""
try:
    response = urllib2.urlopen(website)
    if response.code==200:
        print("site exists!")
    else:
        print("site doesn't exists!")

except urllib2.HTTPError, e:
    print(e.code)

except urllib2.URLError, e:
    print(e.args)
"""
