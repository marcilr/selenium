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
# Links
# =====
# Python check if website exists
# https://stackoverflow.com/questions/16778435/python-check-if-website-exists
#
import urllib2


# =============
# Configuration
# =============

# List of websites to check
linksToCheckFile="links-to-check.txt"

# Single website to check
website='https://www.google.com'



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
