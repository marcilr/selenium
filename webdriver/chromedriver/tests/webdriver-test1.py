#!/usr/bin/python
# webdriver-test1.py
# Created Fri Jun 21 09:18:52 AKDT 2019
# Copyright (C) 2019 by Raymond E. Marcil <marcilr@gmail.com>
#
# Usage:
#
# 1. Get python version:
# $ python --version
# Python 2.7.13   <=== i.e. Not python 3.x
#                           or python3-pip package yet
#
# 2. Install pip the python package installers:
#
# python-pip - Python package installer
# aptitude install python-pip
# The following NEW packages will be installed:
# libpython-all-dev{a} libpython-dev{a} python-all{a} python-all-dev{a} python-cffi-backend{a}
# python-crypto{a} python-cryptography{a} python-dbus{a} python-dev{a} python-enum34{a}
# python-idna{a} python-ipaddress{a} python-keyring{a} python-keyrings.alt{a} python-pip
# python-pip-whl{a} python-pyasn1{a} python-secretstorage{a} python-setuptools{a}
# python-wheel{a} python-xdg{a}
# 0 packages upgraded, 21 newly installed, 0 to remove and 0 not upgraded.
# Need to get 2,920 kB of archives. After unpacking 8,647 kB will be used.
# Do you want to continue? [Y/n/?] Y
# Get: 1 http://ftp.us.debian.org/debian stretch/main amd64 libpython-dev amd64 2.7.13-2 [20.1 kB]
Get: 2 http://ftp.us.debian.org/debian stretch/main amd64 libpython-all-dev amd64 2.7.13-2 [960 B]
Get: 3 http://ftp.us.debian.org/debian stretch/main amd64 python-all amd64 2.7.13-2 [942 B]
Get: 4 http://ftp.us.debian.org/debian stretch/main amd64 python-dev amd64 2.7.13-2 [1,126 B]
Get: 5 http://ftp.us.debian.org/debian stretch/main amd64 python-all-dev amd64 2.7.13-2 [962 B]
Get: 6 http://ftp.us.debian.org/debian stretch/main amd64 python-cffi-backend amd64 1.9.1-2 [69.0 kB]
Get: 7 http://ftp.us.debian.org/debian stretch/main amd64 python-crypto amd64 2.6.1-7 [259 kB]     
Get: 8 http://ftp.us.debian.org/debian stretch/main amd64 python-enum34 all 1.1.6-1 [35.0 kB]      
Get: 9 http://ftp.us.debian.org/debian stretch/main amd64 python-idna all 2.2-1 [32.6 kB]          
Get: 10 http://ftp.us.debian.org/debian stretch/main amd64 python-ipaddress all 1.0.17-1 [18.1 kB] 
Get: 11 http://ftp.us.debian.org/debian stretch/main amd64 python-pyasn1 all 0.1.9-2 [51.8 kB] 
Get: 11 http://ftp.us.debian.org/debian stretch/main amd64 python-pyasn1 all 0.1.9-2 [51.8 kB]     
Get: 12 http://ftp.us.debian.org/debian stretch/main amd64 python-setuptools all 33.1.1-1 [297 kB] 
Get: 13 http://ftp.us.debian.org/debian stretch/main amd64 python-cryptography amd64 1.7.1-3+deb9u1 [211 kB]
Get: 14 http://ftp.us.debian.org/debian stretch/main amd64 python-dbus amd64 1.2.4-1+b1 [185 kB]   
Get: 15 http://ftp.us.debian.org/debian stretch/main amd64 python-secretstorage all 2.3.1-2 [13.8 kB]
Get: 16 http://ftp.us.debian.org/debian stretch/main amd64 python-keyring all 10.1-1 [40.7 kB]     
Get: 17 http://ftp.us.debian.org/debian stretch/main amd64 python-keyrings.alt all 1.3-1 [16.4 kB] 
Get: 18 http://ftp.us.debian.org/debian stretch/main amd64 python-pip-whl all 9.0.1-2+deb9u1 [1,399 kB]
Get: 19 http://ftp.us.debian.org/debian stretch/main amd64 python-pip all 9.0.1-2+deb9u1 [179 kB]
Get: 20 http://ftp.us.debian.org/debian stretch/main amd64 python-wheel all 0.29.0-2 [51.7 kB]     
Get: 21 http://ftp.us.debian.org/debian stretch/main amd64 python-xdg all 0.25-4 [35.8 kB]         
Fetched 2,920 kB in 32s (89.9 kB/s)                                                                
Selecting previously unselected package libpython-dev:amd64.
(Reading database ... 185982 files and directories currently installed.)
Preparing to unpack .../00-libpython-dev_2.7.13-2_amd64.deb ...
...
Unpacking python-xdg (0.25-4) ...
Setting up python-idna (2.2-1) ...
Setting up python-pip-whl (9.0.1-2+deb9u1) ...
Setting up libpython-dev:amd64 (2.7.13-2) ...
Setting up python-setuptools (33.1.1-1) ...
Setting up python-crypto (2.6.1-7) ...
Setting up python-dev (2.7.13-2) ...
Setting up python-pyasn1 (0.1.9-2) ...
Setting up python-wheel (0.29.0-2) ...
Setting up libpython-all-dev:amd64 (2.7.13-2) ...
Setting up python-keyrings.alt (1.3-1) ...
# Setting up python-cffi-backend (1.9.1-2) ...
# Setting up python-enum34 (1.1.6-1) ...
# Processing triggers for man-db (2.7.6.1-2) ...
# Setting up python-dbus (1.2.4-1+b1) ...
# Remove stale byte-compiled files...
# Setting up python-ipaddress (1.0.17-1) ...
# Setting up python-pip (9.0.1-2+deb9u1) ...
# Setting up python-all (2.7.13-2) ...
# Setting up python-xdg (0.25-4) ...
# Setting up python-all-dev (2.7.13-2) ...
# Setting up python-cryptography (1.7.1-3+deb9u1) ...
# Setting up python-secretstorage (2.3.1-2) ...
# Setting up python-keyring (10.1-1) ...
#
#

#    python3-pip - Python package installer
#
#    # aptitude install python-pip python3-pip

# 1. Start the ChromeDriver server separately before running
#    your tests, and connect to it using the Remote WebDriver.
#
#    $ cd /usr/local/bin
#    ./chromedriver
#    Starting ChromeDriver 75.0.3770.90 (a6dcaf7e3ec6f70a194cc25e\
#    8149475c6590e025-refs/branch-heads/3770@{#1003}) on port 9515
#    Only local connections are allowed.
#    Please protect ports used by ChromeDriver and related \
#    test frameworks to prevent access by malicious code.
#
#
# Links
# =====
# Getting started
# ChromeDriver - WebDriver for Chrome
# https://sites.google.com/a/chromium.org/chromedriver/getting-started
#
print("webdriver - test 1")


pip install -U selenium 

import time

from selenium import webdriver
import selenium.webdriver.chrome.service as service

service = service.Service('/path/to/chromedriver')
service.start()
capabilities = {'chrome.binary': '/path/to/custom/chrome'}
driver = webdriver.Remote(service.service_url, capabilities)
driver.get('http://www.google.com/xhtml');
time.sleep(5) # Let the user actually see something!
driver.quit()
