from distutils.core import setup
import py2exe, sys, os

setup(console=['SuperSpider.py'],
      options={"py2exe": {"includes": ["sip", "os", "twisted", "BeautifulSoup", "re", "cookielib", "sys", "urllib", "urllib2", "chardet", "xlsxwriter", "PyQt4.QtGui", "PyQt4.uic", "PyQt4.QtCore", 'ElementC14N', 'ElementTree', 'PyQt4.elementtree.ElementTree', '_scproxy', '_sysconfigdata', 'bs4', 'cjkcodecs.aliases', 'elementtree.ElementTree', 'html', 'http', 'iconv_codec', 'urllib.parse', 'zope']}})