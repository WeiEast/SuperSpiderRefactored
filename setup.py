from distutils.core import setup
import py2exe, sys, os

setup(console=['SuperSpider.py'],
      options={"py2exe": {"includes": ["sip", "os", "twisted", "BeautifulSoup", "re", "cookielib", "sys", "urllib", "urllib2", "chardet", "xlsxwriter", "PyQt4.QtGui", "PyQt4.uic", "PyQt4.QtCore"]}})