#!/usr/bin/python
# test1.py
# Created Fri Jun 21 09:18:52 AKDT 2019
# Copyright (C) 2019 by Raymond E. Marcil <marcilr@gmail.com>
#
# Links
# =====
# Getting started
# ChromeDriver - WebDriver for Chrome
# https://sites.google.com/a/chromium.org/chromedriver/getting-started
#
print("Test 1")

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
