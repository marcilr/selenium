#!/usr/bin/python
# webdriver-test1.py
# Created Fri Jun 21 09:18:52 AKDT 2019
# Copyright (C) 2019 by Raymond E. Marcil <marcilr@gmail.com>
#
#
# WebDriver ChromeDriver web page existence check
#
# This opens a chrome window for 5 seconds to:
#    https://www.google.com/webhp?gws_rd=ssl
#
#
# Fri Jun 21 13:56:01 AKDT 2019
# =============================
# 1. Install pip (Python package installer)
#    aptitude install python-pip
#    see: pip-install.txt
#
# 2. Install selenium on Debian 9.9.0 vm:
#    # pip install -U selenium
#    Collecting selenium
#    Using cached https://files.pythonhosted.org/packages/80/d6/\
#    4294f0b4bce4de0abf13e17190289f9d0613b0a44e5dd6a7f5ca98459853/\
#    selenium-3.141.0-py2.py3-none-any.whl
#    Requirement already up-to-date: urllib3 in \
#    /usr/local/lib/python2.7/dist-packages (from selenium)
#    Installing collected packages: selenium
#    Successfully installed selenium-3.141.0
#    #
#
# 3. Start the ChromeDriver server separately before running
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
import time

from selenium import webdriver
import selenium.webdriver.chrome.service as service

print("webdriver - test 1")

service = service.Service('/usr/local/bin/chromedriver')
service.start()
capabilities = {'chrome.binary': '/usr/bin/google-chrome'}
driver = webdriver.Remote(service.service_url, capabilities)
driver.get('http://www.google.com/xhtml');
time.sleep(5) # Let the user actually see something!
driver.quit()
