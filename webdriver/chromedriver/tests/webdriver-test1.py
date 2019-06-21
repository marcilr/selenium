#!/usr/bin/python
# webdriver-test1.py
# Created Fri Jun 21 09:18:52 AKDT 2019
# Copyright (C) 2019 by Raymond E. Marcil <marcilr@gmail.com>
#
#
# WebDriver ChromeDriver web page existence check
#
#
# Fri Jun 21 09:18:52 AKDT 2019
# =============================
# 1. Install pip (Python package installer)
#    aptitude install python-pip
#    see: pip-install.txt
#
# 2. Install selenium:
#    pip install selenium
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
# print("webdriver - test 1")
#
# pip install -U selenium
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
