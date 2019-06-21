#!/usr/bin/python
# unittest-test2.py
# Created Fri Jun 21 14:11:17 AKDT 2019
# Copyright (C) 2019 by Raymond E. Marcil <marcilr@gmail.com>
#
# Links
# =====
# Getting started
# ChromeDriver - WebDriver for Chrome
# Source for:
#   driver = webdriver.Chrome('/path/to/chromedriver')
# https://sites.google.com/a/chromium.org/chromedriver/getting-started
#
# selenium 3.141.0
# pip install selenium
# Source for this unittest
# https://pypi.org/project/selenium/
#
import unittest
from selenium import webdriver

class GoogleTestCase(unittest.TestCase):

    def setUp(self):
#        self.browser = webdriver.Firefox()
        self.browser = webdriver.Chrome('/usr/local/bin/chromedriver')
        self.addCleanup(self.browser.quit)

    def testPageTitle(self):
        self.browser.get('http://www.google.com')
        self.assertIn('Google', self.browser.title)

if __name__ == '__main__':
    unittest.main(verbosity=2)

