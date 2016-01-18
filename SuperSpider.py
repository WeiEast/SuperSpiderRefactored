# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
import re
import cookielib
import sys,urllib, urllib2 #, time,os, socket,random
import chardet
#from scrapy.selector import Selector

#from lxml.cssselect import CSSSelector
#from lxml.etree import fromstring
#from cssselect import GenericTranslator
#from lxml.etree import XPath


import xlsxwriter

from PyQt4 import QtGui
from PyQt4 import uic
from PyQt4 import QtCore
from PyQt4.QtCore import pyqtSlot
from PyQt4.QtCore import QThread



#from scrapy.cmdline import execute
#from scrapy.http import HtmlResponse
#from superSpider.items import SuperspiderItem
#from scrapy.http.cookies import CookieJar
#import ssl
#import scrapy

reload(sys)
sys.setdefaultencoding('utf-8')

# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'superSpider.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(598, 354)
        self.SDay2 = QtGui.QRadioButton(Dialog)
        self.SDay2.setGeometry(QtCore.QRect(80, 30, 131, 16))
        self.SDay2.setChecked(True)
        self.SDay2.setAutoRepeatInterval(101)
        self.SDay2.setObjectName(_fromUtf8("SDay2"))
        self.SDay1 = QtGui.QRadioButton(Dialog)
        self.SDay1.setGeometry(QtCore.QRect(80, 60, 90, 16))
        self.SDay1.setObjectName(_fromUtf8("SDay1"))
        self.resResultdate = QtGui.QDateEdit(Dialog)
        self.resResultdate.setGeometry(QtCore.QRect(180, 60, 110, 22))
        self.resResultdate.setDateTime(QtCore.QDateTime(QtCore.QDate(2016, 1, 14), QtCore.QTime(0, 0, 0)))
        self.resResultdate.setCalendarPopup(True)
        self.resResultdate.setObjectName(_fromUtf8("resResultdate"))
        self.resResultdate2 = QtGui.QDateEdit(Dialog)
        self.resResultdate2.setGeometry(QtCore.QRect(330, 60, 110, 22))
        self.resResultdate2.setDateTime(QtCore.QDateTime(QtCore.QDate(2016, 1, 28), QtCore.QTime(0, 0, 0)))
        self.resResultdate2.setCalendarPopup(True)
        self.resResultdate2.setObjectName(_fromUtf8("resResultdate2"))
        self.label = QtGui.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(20, 30, 56, 12))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(20, 110, 56, 12))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(90, 110, 56, 12))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_4 = QtGui.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(20, 170, 56, 12))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.label_5 = QtGui.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(300, 60, 21, 16))
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.label_6 = QtGui.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(300, 110, 21, 16))
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.logOfProgress = QtGui.QPlainTextEdit(Dialog)
        self.logOfProgress.setGeometry(QtCore.QRect(20, 220, 561, 101))
        self.logOfProgress.setReadOnly(True)
        self.logOfProgress.setPlainText(_fromUtf8(""))
        self.logOfProgress.setObjectName(_fromUtf8("logOfProgress"))
        self.resYongNm = QtGui.QComboBox(Dialog)
        self.resYongNm.setGeometry(QtCore.QRect(180, 160, 261, 22))
        self.resYongNm.setObjectName(_fromUtf8("resYongNm"))
        self.resYongNm.addItem(_fromUtf8(""))
        self.resYongNm.addItem(_fromUtf8(""))
        self.resYongNm.addItem(_fromUtf8(""))
        self.resYongNm.addItem(_fromUtf8(""))
        self.resYongNm.addItem(_fromUtf8(""))
        self.resYongNm.addItem(_fromUtf8(""))
        self.resYongNm.addItem(_fromUtf8(""))
        self.resYongNm.addItem(_fromUtf8(""))
        self.resYongNm.addItem(_fromUtf8(""))
        self.resYongNm.addItem(_fromUtf8(""))
        self.resYongNm.addItem(_fromUtf8(""))
        self.resYongNm.addItem(_fromUtf8(""))
        self.resYongNm.addItem(_fromUtf8(""))
        self.resYongNm.addItem(_fromUtf8(""))
        self.resYongNm.addItem(_fromUtf8(""))
        self.resYongNm.addItem(_fromUtf8(""))
        self.resYongNm.addItem(_fromUtf8(""))
        self.resYongNm.addItem(_fromUtf8(""))
        self.resYongNm.addItem(_fromUtf8(""))
        self.resYongNm.addItem(_fromUtf8(""))
        self.resYongNm.addItem(_fromUtf8(""))
        self.resYongNm.addItem(_fromUtf8(""))
        self.resYongNm.addItem(_fromUtf8(""))
        self.resYongNm.addItem(_fromUtf8(""))
        self.resYongNm.addItem(_fromUtf8(""))
        self.resYongNm.addItem(_fromUtf8(""))
        self.resYongNm.addItem(_fromUtf8(""))
        self.resYongNm.addItem(_fromUtf8(""))
        self.resTotGamAmt1 = QtGui.QComboBox(Dialog)
        self.resTotGamAmt1.setGeometry(QtCore.QRect(180, 110, 111, 22))
        self.resTotGamAmt1.setObjectName(_fromUtf8("resTotGamAmt1"))
        self.resTotGamAmt1.addItem(_fromUtf8(""))
        self.resTotGamAmt1.addItem(_fromUtf8(""))
        self.resTotGamAmt1.addItem(_fromUtf8(""))
        self.resTotGamAmt1.addItem(_fromUtf8(""))
        self.resTotGamAmt1.addItem(_fromUtf8(""))
        self.resTotGamAmt1.addItem(_fromUtf8(""))
        self.resTotGamAmt1.addItem(_fromUtf8(""))
        self.resTotGamAmt1.addItem(_fromUtf8(""))
        self.resTotGamAmt1.addItem(_fromUtf8(""))
        self.resTotGamAmt1.addItem(_fromUtf8(""))
        self.resTotGamAmt1.addItem(_fromUtf8(""))
        self.resTotGamAmt1.addItem(_fromUtf8(""))
        self.resTotGamAmt1.addItem(_fromUtf8(""))
        self.resTotGamAmt1.addItem(_fromUtf8(""))
        self.resTotGamAmt1.addItem(_fromUtf8(""))
        self.resTotGamAmt1.addItem(_fromUtf8(""))
        self.resTotGamAmt1.addItem(_fromUtf8(""))
        self.resTotGamAmt1.addItem(_fromUtf8(""))
        self.resTotGamAmt1.addItem(_fromUtf8(""))
        self.resTotGamAmt1.addItem(_fromUtf8(""))
        self.resTotGamAmt1.addItem(_fromUtf8(""))
        self.resTotGamAmt1.addItem(_fromUtf8(""))
        self.resTotGamAmt2 = QtGui.QComboBox(Dialog)
        self.resTotGamAmt2.setGeometry(QtCore.QRect(330, 110, 111, 22))
        self.resTotGamAmt2.setObjectName(_fromUtf8("resTotGamAmt2"))
        self.resTotGamAmt2.addItem(_fromUtf8(""))
        self.resTotGamAmt2.addItem(_fromUtf8(""))
        self.resTotGamAmt2.addItem(_fromUtf8(""))
        self.resTotGamAmt2.addItem(_fromUtf8(""))
        self.resTotGamAmt2.addItem(_fromUtf8(""))
        self.resTotGamAmt2.addItem(_fromUtf8(""))
        self.resTotGamAmt2.addItem(_fromUtf8(""))
        self.resTotGamAmt2.addItem(_fromUtf8(""))
        self.resTotGamAmt2.addItem(_fromUtf8(""))
        self.resTotGamAmt2.addItem(_fromUtf8(""))
        self.resTotGamAmt2.addItem(_fromUtf8(""))
        self.resTotGamAmt2.addItem(_fromUtf8(""))
        self.resTotGamAmt2.addItem(_fromUtf8(""))
        self.resTotGamAmt2.addItem(_fromUtf8(""))
        self.resTotGamAmt2.addItem(_fromUtf8(""))
        self.resTotGamAmt2.addItem(_fromUtf8(""))
        self.resTotGamAmt2.addItem(_fromUtf8(""))
        self.resTotGamAmt2.addItem(_fromUtf8(""))
        self.resTotGamAmt2.addItem(_fromUtf8(""))
        self.resTotGamAmt2.addItem(_fromUtf8(""))
        self.resTotGamAmt2.addItem(_fromUtf8(""))
        self.resTotGamAmt2.addItem(_fromUtf8(""))
        self.startButton = QtGui.QPushButton(Dialog)
        self.startButton.setGeometry(QtCore.QRect(500, 20, 75, 23))
        self.startButton.setObjectName(_fromUtf8("startButton"))
        self.endButton = QtGui.QPushButton(Dialog)
        self.endButton.setGeometry(QtCore.QRect(500, 50, 75, 23))
        self.endButton.setObjectName(_fromUtf8("endButton"))
        self.numOfTotal = QtGui.QLabel(Dialog)
        self.numOfTotal.setGeometry(QtCore.QRect(470, 180, 101, 20))
        self.numOfTotal.setAlignment(QtCore.Qt.AlignCenter)
        self.numOfTotal.setObjectName(_fromUtf8("numOfTotal"))
        self.numOfTotalItems = QtGui.QLabel(Dialog)
        self.numOfTotalItems.setGeometry(QtCore.QRect(470, 200, 101, 20))
        self.numOfTotalItems.setAlignment(QtCore.Qt.AlignCenter)
        self.numOfTotalItems.setObjectName(_fromUtf8("numOfTotalItems"))

        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.startButton, QtCore.SIGNAL(_fromUtf8("clicked()")), self.start_crawl)
        QtCore.QObject.connect(self.endButton, QtCore.SIGNAL(_fromUtf8("clicked()")), self.stop_crawl)
        QtCore.QMetaObject.connectSlotsByName(Dialog)


        ##
        nowYear=""
        nowMonth=""
        nowDay=""

        #create a QDateTimeEdit object
        myDTE = QtGui.QDateTimeEdit()
        now = QtCore.QDateTime.currentDateTime()
        today = QtCore.QDate.currentDate()

        self.resResultdate.setDate(today)
        self.resResultdate2.setDate(today.addDays(14))

        self.nowYear=str(today.year())
        self.nowMonth=str(today.month())
        self.nowDay=str(today.day())
        if(len(self.nowMonth)==1):
            self.nowMonth = "0"+self.nowMonth
        if(len(self.nowDay)==1):
            self.nowDay = "0"+self.nowDay

        self.superSpiderThread = self.SuperSpiderThread(self)
        QtCore.QObject.connect(self.superSpiderThread, QtCore.SIGNAL("finishedWork"), self.done)
        QtCore.QObject.connect(self.superSpiderThread, QtCore.SIGNAL("loggingWork"), self.traceLog)
        #This is about Signal and it is point https://nikolak.com/pyqt-threading-tutorial/

        #self.ui.show()

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Crawler", None))
        self.SDay2.setText(_translate("Dialog", "오늘이후 전체물건", None))
        self.SDay1.setText(_translate("Dialog", "날짜 선택", None))
        self.label.setText(_translate("Dialog", "입찰기일", None))
        self.label_2.setText(_translate("Dialog", "금액관련", None))
        self.label_3.setText(_translate("Dialog", "감정가", None))
        self.label_4.setText(_translate("Dialog", "용도지역", None))
        self.label_5.setText(_translate("Dialog", "~", None))
        self.label_6.setText(_translate("Dialog", "~", None))
        self.resYongNm.setItemText(0, _translate("Dialog", "선택하세요", None))
        self.resYongNm.setItemText(1, _translate("Dialog", "도시지역", None))
        self.resYongNm.setItemText(2, _translate("Dialog", "주거지역", None))
        self.resYongNm.setItemText(3, _translate("Dialog", "제1종 전용주거지역", None))
        self.resYongNm.setItemText(4, _translate("Dialog", "제2종 전용주거지역", None))
        self.resYongNm.setItemText(5, _translate("Dialog", "제1종 일반주거지역", None))
        self.resYongNm.setItemText(6, _translate("Dialog", "제2종 일반주거지역", None))
        self.resYongNm.setItemText(7, _translate("Dialog", "제3종 일반주거지역", None))
        self.resYongNm.setItemText(8, _translate("Dialog", "준 주거지역", None))
        self.resYongNm.setItemText(9, _translate("Dialog", "상업지역", None))
        self.resYongNm.setItemText(10, _translate("Dialog", "중심상업지역", None))
        self.resYongNm.setItemText(11, _translate("Dialog", "일반상업지역", None))
        self.resYongNm.setItemText(12, _translate("Dialog", "근린상업지역", None))
        self.resYongNm.setItemText(13, _translate("Dialog", "유통상업지역", None))
        self.resYongNm.setItemText(14, _translate("Dialog", "공업지역", None))
        self.resYongNm.setItemText(15, _translate("Dialog", "전용공업지역", None))
        self.resYongNm.setItemText(16, _translate("Dialog", "일반공업지역", None))
        self.resYongNm.setItemText(17, _translate("Dialog", "준 공업지역", None))
        self.resYongNm.setItemText(18, _translate("Dialog", "녹지지역", None))
        self.resYongNm.setItemText(19, _translate("Dialog", "보전녹지지역", None))
        self.resYongNm.setItemText(20, _translate("Dialog", "생산녹지지역", None))
        self.resYongNm.setItemText(21, _translate("Dialog", "자연녹지지역", None))
        self.resYongNm.setItemText(22, _translate("Dialog", "관리지역", None))
        self.resYongNm.setItemText(23, _translate("Dialog", "보전관리지역", None))
        self.resYongNm.setItemText(24, _translate("Dialog", "생산관리지역", None))
        self.resYongNm.setItemText(25, _translate("Dialog", "계획관리지역", None))
        self.resYongNm.setItemText(26, _translate("Dialog", "농림지역", None))
        self.resYongNm.setItemText(27, _translate("Dialog", "자연환경보전지역", None))
        self.resTotGamAmt1.setItemText(0, _translate("Dialog", "최소", None))
        self.resTotGamAmt1.setItemText(1, _translate("Dialog", "0원", None))
        self.resTotGamAmt1.setItemText(2, _translate("Dialog", "1천만", None))
        self.resTotGamAmt1.setItemText(3, _translate("Dialog", "3천만", None))
        self.resTotGamAmt1.setItemText(4, _translate("Dialog", "5천만", None))
        self.resTotGamAmt1.setItemText(5, _translate("Dialog", "7천만", None))
        self.resTotGamAmt1.setItemText(6, _translate("Dialog", "1억", None))
        self.resTotGamAmt1.setItemText(7, _translate("Dialog", "1억5천", None))
        self.resTotGamAmt1.setItemText(8, _translate("Dialog", "2억", None))
        self.resTotGamAmt1.setItemText(9, _translate("Dialog", "2억5천", None))
        self.resTotGamAmt1.setItemText(10, _translate("Dialog", "3억", None))
        self.resTotGamAmt1.setItemText(11, _translate("Dialog", "4억", None))
        self.resTotGamAmt1.setItemText(12, _translate("Dialog", "5억", None))
        self.resTotGamAmt1.setItemText(13, _translate("Dialog", "6억", None))
        self.resTotGamAmt1.setItemText(14, _translate("Dialog", "7억", None))
        self.resTotGamAmt1.setItemText(15, _translate("Dialog", "8억", None))
        self.resTotGamAmt1.setItemText(16, _translate("Dialog", "9억", None))
        self.resTotGamAmt1.setItemText(17, _translate("Dialog", "10억", None))
        self.resTotGamAmt1.setItemText(18, _translate("Dialog", "15억", None))
        self.resTotGamAmt1.setItemText(19, _translate("Dialog", "20억", None))
        self.resTotGamAmt1.setItemText(20, _translate("Dialog", "30억", None))
        self.resTotGamAmt1.setItemText(21, _translate("Dialog", "50억", None))
        self.resTotGamAmt2.setItemText(0, _translate("Dialog", "최대", None))
        self.resTotGamAmt2.setItemText(1, _translate("Dialog", "0원", None))
        self.resTotGamAmt2.setItemText(2, _translate("Dialog", "1천만", None))
        self.resTotGamAmt2.setItemText(3, _translate("Dialog", "3천만", None))
        self.resTotGamAmt2.setItemText(4, _translate("Dialog", "5천만", None))
        self.resTotGamAmt2.setItemText(5, _translate("Dialog", "7천만", None))
        self.resTotGamAmt2.setItemText(6, _translate("Dialog", "1억", None))
        self.resTotGamAmt2.setItemText(7, _translate("Dialog", "1억5천", None))
        self.resTotGamAmt2.setItemText(8, _translate("Dialog", "2억", None))
        self.resTotGamAmt2.setItemText(9, _translate("Dialog", "2억5천", None))
        self.resTotGamAmt2.setItemText(10, _translate("Dialog", "3억", None))
        self.resTotGamAmt2.setItemText(11, _translate("Dialog", "4억", None))
        self.resTotGamAmt2.setItemText(12, _translate("Dialog", "5억", None))
        self.resTotGamAmt2.setItemText(13, _translate("Dialog", "6억", None))
        self.resTotGamAmt2.setItemText(14, _translate("Dialog", "7억", None))
        self.resTotGamAmt2.setItemText(15, _translate("Dialog", "8억", None))
        self.resTotGamAmt2.setItemText(16, _translate("Dialog", "9억", None))
        self.resTotGamAmt2.setItemText(17, _translate("Dialog", "10억", None))
        self.resTotGamAmt2.setItemText(18, _translate("Dialog", "15억", None))
        self.resTotGamAmt2.setItemText(19, _translate("Dialog", "20억", None))
        self.resTotGamAmt2.setItemText(20, _translate("Dialog", "30억", None))
        self.resTotGamAmt2.setItemText(21, _translate("Dialog", "50억 이상", None))
        self.startButton.setText(_translate("Dialog", "검색시작", None))
        self.endButton.setText(_translate("Dialog", "검색종료", None))
        self.numOfTotal.setText(_translate("Dialog", "총 페이지수", None))
        self.numOfTotalItems.setText(_translate("Dialog", "총 건수", None))

       # self.selfInitSetup()

    #def selfInitSetup(self):


        #print self.ui.resResultdate.date().year()
        #print self.ui.resResultdate.date().month()
        #print self.ui.resResultdate.date().day()



#class Form(QtGui.QDialog):

#    crawl_flag=False
#    nowYear=""
#    nowMonth=""
#    nowDay=""
#    SDay=""
#    resYear1=""
#    resMonth1=""
#    resday1=""
#    resResultdate=""
#    resYear2=""
#    resMonth2=""
#    resday2=""
#    resTotGamAmt1=""
#    resTotGamAmt2=""
#    resYongNm=""

    resYear1=""
    resMonth1=""
    resday1=""
#    resResultdate=""
    resYear2=""
    resMonth2=""
    resday2=""
    crawl_flag=False

   # def __init__(self, parent=None):
#        QtGui.QDialog.__init__(self, parent)

#        Dialog = QtGui.QDialog()
#        ui = Ui_Dialog()
#        self.ui = ui.setupUi(Dialog) #def setupUi(self, Dialog):
        #Dialog.show()

        #self.ui = uic.loadUi("superSpider.ui", self)








    def closeEvent(self, event):
        print "User has clicked the red x on the main window"
        event.accept()

    def done(self, sigstr):
        print "SigStr~~"
        print sigstr
        self.logOfProgress.setPlainText("End, Complete\n"+self.logOfProgress.toPlainText()) #QObject: Cannot create children for a parent that is in a different thread.
        print "Done!" #TypeError: done() takes exactly 1 argument (2 given)

    def traceLog(self, sigLogStr):
        print "SigLogStr~~"
        print sigLogStr
        self.logOfProgress.setPlainText(sigLogStr+"\n"+self.logOfProgress.toPlainText()) #QObject: Cannot create children for a parent that is in a different thread.
        print "Logging!" #TypeError: done() takes exactly 1 argument (2 given)

    @pyqtSlot()
    def start_crawl(self):
        self.crawl_flag=False

        if(self.SDay2.isChecked()):
            self.SDay="2"
            self.resYear1=str(self.resResultdate.date().year())
            self.resMonth1=str(self.resResultdate.date().month())
            self.resday1=str(self.resResultdate.date().day())

            if(len(self.resMonth1)==1):
               self.resMonth1 = "0"+self.resMonth1
            if(len(self.resday1)==1):
                self.resday1 = "0"+self.resday1

            self.resResultdate = self.resYear1+"-"+self.resMonth1+"-"+self.resday1
            print self.resResultdate
            self.resYear2=""
            self.resMonth2=""
            self.resday2=""

        elif(self.SDay1.isChecked()):
            self.SDay="1"
            resYear1=str(self.resResultdate.date().year())
            resMonth1=str(self.resResultdate.date().month())
            resday1=str(self.resResultdate.date().day())

            if(len(self.resMonth1)==1):
               self.resMonth1 = "0"+self.resMonth1
            if(len(self.resday1)==1):
                self.resday1 = "0"+self.resday1

            self.resResultdate = self.resYear1+"-"+self.resMonth1+"-"+self.resday1

            self.resYear2=str(self.resResultdate2.date().year())
            self.resMonth2=str(self.resResultdate2.date().month())
            self.resday2=str(self.resResultdate2.date().day())

            if(len(self.resMonth2)==1):
               self.resMonth2 = "0"+self.resMonth2
            if(len(self.resday2)==1):
                self.resday2 = "0"+self.resday2

        else:
            self.SDay="2"
            self.resYear1=str(self.resResultdate.date().year())
            self.resMonth1=str(self.resResultdate.date().month())
            self.resday1=str(self.resResultdate.date().day())

            if(len(self.resMonth1)==1):
               self.resMonth1 = "0"+self.resMonth1
            if(len(self.resday1)==1):
                self.resday1 = "0"+self.resday1

            self.resResultdate = self.resYear1+"-"+self.resMonth1+"-"+self.resday1
            print self.resResultdate
            self.resYear2=""
            self.resMonth2=""
            self.resday2=""


        choices = { '0':'', '1':'0', '2':'1', '3':'3', '4':'5', '5':'7', '6':'10', '7':'15', '8':'20', '9':'25', '10':'30',
                    '11':'40', '12':'50', '13':'60', '14':'70', '15':'80', '16':'90', '17':'100', '18':'150', '19':'200', '20':'300','21':'500'}
        self.resTotGamAmt1 = choices[str(self.resTotGamAmt1.currentIndex())]

        choices2 = { '0':'', '1':'0', '2':'1', '3':'3', '4':'5', '5':'7', '6':'10', '7':'15', '8':'20', '9':'25', '10':'30',
                    '11':'40', '12':'50', '13':'60', '14':'70', '15':'80', '16':'90', '17':'100', '18':'150', '19':'200', '20':'300','21':'999999'}
        self.resTotGamAmt2 = choices2[str(self.resTotGamAmt2.currentIndex())]
        print self.resTotGamAmt1
        print self.resTotGamAmt2

        choices3 = {
            '0':'', '1':'A1,A2,A3,A4,A5,A6,B1,B2,B3,B4,C1,C2,C3,D1,D2,D3', '2':'A1,A2,A3,A4,A5,A6', '3':'A1', '4':'A2', '5':'A3',
        '6':'A4', '7':'A5', '8':'A6', '9':'B1,B2,B3,B4', '10':'B1', '11':'B2', '12':'B3', '13':'B4',
        '14':'C1,C2,C3', '15':'C1', '16':'C2', '17':'C3', '18':'D1,D2,D3', '19':'D1', '20':'D2', '21':'D3', '22':'E1,E2,E3',
        '23':'E1', '24':'E2', '25':'E3', "26":'F1', '27':'G1'
        }
        self.resYongNm = choices3[str(self.resYongNm.currentIndex())]
        print self.resYongNm


        self.logOfProgress.setPlainText("Start Downloading....\n")
       # self.show()

        self.superSpiderThread.start()
        #execute(['scrapy','crawl','super'])
        #self.ui.label.setText("Hello~")

    @pyqtSlot()
    def stop_crawl(self):
        self.crawl_flag=True
        #self.ui.label.setText("두번째 버튼")




#http://edoli.tistory.com/46 // urllib cookie example



    class SuperSpiderThread (QThread):



        def __init__(self, super):
            QThread.__init__(self)
            self.super = super

        def __del__(self):
            self.wait()

        def run(self):
            #your logic here

            print self.super.resYongNm
            name = "super"
            allowed_domains = ["www.ggi.co.kr"]
            base_url = "http://www.ggi.co.kr"
            start_urls = ["https://www.ggi.co.kr/home1.asp"]

            cookie = ""


            formdata=urllib.urlencode({'resid':'gusco7880', 'respass':'gusco7880'})
            cj = cookielib.CookieJar()
            opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
            urllib2.install_opener(opener)
            req = urllib2.Request("http://www.ggi.co.kr/home1.asp", formdata)
            res = opener.open(req)
            self.after_login(res)



        def after_login(self, response):

            base_url = "http://www.ggi.co.kr"
            cookie = ""
            cj = cookielib.CookieJar()
            opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
            urllib2.install_opener(opener)
            params = urllib.urlencode({'back_url':'/home1.asp',
                                       'back_string':'',
                                       'resid':'gusco7880',
                                       'respass':'gusco7880'})



            print "Succeed!!!"


            print response.url


            req = urllib2.Request("http://www.ggi.co.kr/login/ggi_login.asp", params)
            res = opener.open(req)


            cookie = res.headers.get('Set-Cookie')
           # print self.cookie


            req2 = urllib2.Request("http://www.ggi.co.kr/member/my_today.asp")
            req2.add_header('cookie', cookie)
            res2 = opener.open(req2)
            #print res2.headers.get('Set-Cookie') #Note!! even though it shows None -> it works.. I can't explain it however I guess visiting my_today.asp is keypoint to get cookies
            #self.cookie = res2.headers.get('Set-Cookie')
            #print self.cookie

            print self.super.resResultdate
            print "resTotGamAmt1 Test!!"
            print self.super.resTotGamAmt1
            print "resTotGamAmt1 End!!"

            formdata=urllib.urlencode({
                                            'groupresult':'',
                                            'resChgPage':'1',
                                            'nowpge':'',
                                            'choice':'1',
                                            'seqno_no':'',
                                            'popgugun':'',
                                            'popemdong':'',
                                            'search_save':'Y',
                                            'save_seq':'',
                                            'resultchk':'N',
                                            'SDay':self.super.SDay,
                                            'resResultdate':self.super.resResultdate,
                                            'AreaSelect':'1',
                                            'resSiDo':'00',
                                            'resSiGuGun':'',
                                            'resEMDong':'',
                                            'resRi':'',
                                            'addr':'',
                                            'l_addr1':'',
                                            'l_addr2':'',
                                            'resTotGamAmt1':self.super.resTotGamAmt1,
                                            'resTotGamAmt2':self.super.resTotGamAmt2,
                                            'resTotLowestAmt1':'',
                                            'resTotLowestAmt2':'',
                                            'reslandArea1':'',
                                            'reslandArea2':'',
                                            'pyung':'',
                                            'resjicheung':'ji_all',
                                            'resbuilArea1':'',
                                            'resbuilArea2':'',
                                            'bdname':'',
                                            'resYongNm':self.super.resYongNm,
                                            'resBuildYear1':'',
                                            'resBuildYear2':'',
                                            'resAuctionResult':'',
                                            'resAuctionResult2':'',
                                            'resYouchalCnt1':'',
                                            'resYouchalCnt2':'',
                                            'resjugam1':'',
                                            'resjugam2':'',
                                            'kyungGubun':'',
                                            'resSort1':'',
                                            'pgesize':'20',
                                            'Newuse':'',
                                            'useall':'',
                                            'resuse':'',
                                            'use_inc':'',
                                            'ListGubun':'',
                                            'matchchk':'',
                                            'matchname':'',
                                            'matchCount':'0',
                                            'mathchreset':'Y',
                                            'reg_mgroup':''
                                     })
            print formdata

            req = urllib2.Request("http://www.ggi.co.kr/search/sojae_search.asp", formdata)
            req.add_header('cookie',cookie)
            res = opener.open(req)
           # print res.headers.get('Set-Cookie')
    #            print self.cookie

            searchResultHtml = res.read()

            soup = BeautifulSoup(searchResultHtml,"html5lib")
            parsingNumOfTotalPage = soup.select('#noprint > td.text_Align_center')[0].get_text(strip=True).split(' P')[0].split('(')[1]
            print parsingNumOfTotalPage
            NumOfTotalPage = int(re.search(r'\d+', parsingNumOfTotalPage).group())
            print NumOfTotalPage

            paramNumOfTotal = "Total "+str(NumOfTotalPage)+" Pages"
            self.super.numOfTotal.setText(paramNumOfTotal)

            parsingNumOfTotalItems = soup.select('#noprint > td.text_Align_center')[0].get_text(strip=True).split(', ')[1]
            NumOfTotalItems = int(re.search(r'\d+', parsingNumOfTotalItems).group())

            paramNumOfTotalItems = "Total "+str(NumOfTotalItems)+" Items"
            self.super.numOfTotalItems.setText(paramNumOfTotalItems)

           # Create an new Excel file and add a worksheet.
            fileName = self.super.nowYear+self.super.nowMonth+self.super.nowDay+"_"+"경매물건DB.xlsx".encode('cp949','ignore')
            workbook = xlsxwriter.Workbook(fileName)
            worksheet = workbook.add_worksheet()

            # Widen the first column to make the text clearer.
            worksheet.set_column('A:A', 20)
            worksheet.set_column('B:B', 15)
            worksheet.set_column('C:C', 40)
            worksheet.set_column('D:D', 20)
            worksheet.set_column('E:E', 20)

            # Add a bold format to use to highlight cells.
            bold = workbook.add_format({'bold': True})

            # Write some simple text.
            worksheet.write('A1', '사건번호')
            worksheet.write('B1', '성명')
            worksheet.write('C1', '주소')
            worksheet.write('D1', '감정가')
            worksheet.write('E1', '최저가')
            worksheet.write('F1', '상태')

            # Text with formatting.
            #worksheet.write('A2', 'World', bold)

            #res 2 is after 14 days check

            indexOfItems = 0
            rowidx = 0
            for pageNo in range(1,NumOfTotalPage+1):
                formdata = urllib.urlencode({
                                                "search_save":"",
                                                "resSiDo":"0",
                                                "resSiGuGun":"",
                                                "resEMDong":"",
                                                "resYear1":self.super.resYear1,
                                                "resMonth1":self.super.resMonth1,
                                                "resday1":self.super.resday1,
                                                "resYear2":self.super.resYear2,
                                                "resMonth2":self.super.resMonth2,
                                                "resday2":self.super.resday2,
                                                "resTotGamAmt1":self.super.resTotGamAmt1,
                                                "resTotGamAmt2":self.super.resTotGamAmt2,
                                                "resTotLowestAmt1":"",
                                                "resTotLowestAmt2":"",
                                                "resLowAmtRatio":"",
                                                "resYouchalCnt1":"",
                                                "resYouchalCnt2":"",
                                                "resAuctionResult":"",
                                                "resUse":"",
                                                "useall":"",
                                                "addr":"",
                                                "resRi":"",
                                                "TodayNew":"",
                                                "TodayNewStr":"",
                                                "title_code":"",
                                                "ListGubun":"1",
                                                "resright":"",
                                                "resright2":"",
                                                "pyung":"",
                                                "resBubwon":"",
                                                "resGae":"",
                                                "AreaSelect":"1",
                                                "sday":self.super.SDay,
                                                "Ex":"",
                                                "resChgPage":"1",
                                                "nowpge":pageNo,
                                                "resYongNm":self.super.resYongNm,
                                                "resBuildYear1":"",
                                                "resBuildYear2":"",
                                                "bdname":"",
                                                "reslandArea1":"",
                                                "reslandArea2":"",
                                                "resbuilArea1":"",
                                                "resbuilArea2":"",
                                                "gummulipchal":"",
                                                "tojiipchal":"",
                                                "sunimcha":"",
                                                "daejidung":"",
                                                "kyungGubun":"",
                                                "resjicheung":"ji_all",
                                                "Gubun":"",
                                                "dajung":"",
                                                "selectuse":"",
                                                "m_group":"",
                                                "mathchreset":"N",
                                                "popgugun":"",
                                                "popemdong":"",
                                                "resAuctionResult2":"",
                                                "resResultYear":"",
                                                "resResultMonth":"",
                                                "resResultDay":"",
                                                "resultchk":"N",
                                                "jigu_type":"",
                                                "r_resSiDo":"",
                                                "r_resSiGuGun":"",
                                                "roadnm":"",
                                                "gunno":"",
                                                "jiguchk":"",
                                                "choice":"1",
                                                "UseCd":"",
                                                "restotdate1":"",
                                                "restotdate2":"",
                                                "use_inc":"",
                                                "resResultdate":"42384",
                                                "resjugam1":"",
                                                "resjugam2":"",
                                                "resSort2":"startdate_asc",
                                                "pgesize":"20"
                                                })

                #change the way writing excel files
                #make way to stop terminal!
                req = urllib2.Request("http://www.ggi.co.kr/search/sojae_search.asp", formdata)
                req.add_header('cookie',cookie)
                res = opener.open(req)
               # print res.headers.get('Set-Cookie')
        #            print self.cookie

                searchResultHtml = res.read()
#
#                filenmae = 'test.html'
#                with open(filenmae, 'wb') as f:
#                    f.write(searchResultHtml)

                #list_link
                soup = BeautifulSoup(searchResultHtml,"html5lib")
                links = soup.select('.list_link')
                #links = soup.find_all('a', href=True):

                #h = fromstring(searchResultHtml)
                #links = XPath(GenericTranslator().css_to_xpath('//a[contains(@href, "common/mulgun_detail_popup2")]/@href'))
                #links = XPath(('//a[contains(@href, "common/mulgun_detail_popup2")]/@href')).text()
                #print links
                #links = Selector(text=searchResultHtml).xpath('//a[contains(@href, "common/mulgun_detail_popup2")]/@href').extract()
#Table13 > tbody > tr:nth-child(1) > td > a
#trimg_0 > td:nth-child(5)
#trimg_1 > td:nth-child(5)

                links = list(set(links)) #remove duplicated data

                for index, link in enumerate(links):

                    print link.parent.parent.parent.parent.parent.find_next_siblings()[1]#.get_text(strip=True).encode('cp949','ignore')
                    #Note , Check This is the point what I want to get a state


                    links[index] = link['href']
                    print link['href']
                    links[index] = link['href'].replace("..",base_url)
                    #print links[index]

#                links = list(set(links)) #remove duplicated data
                sizeOfLinks = len(links)


                itemsList = []

                for linkIdx, link in enumerate(links):
                    req = urllib2.Request(link)
                    res = opener.open(req)
                    print res.url

                    rawdata = res.read()
                    encoding = chardet.detect(rawdata)
                    html = rawdata.decode(encoding['encoding'])

                    indexOfItems = indexOfItems+1

           # links = response.xpath('//a[contains(@href, "common/mulgun_detail_popup2")]/@href').extract()
                  #  print Selector(text=html).css('td[class="td1"]').extract()

        #http://www.dreamy.pe.kr/zbxe/CodeClip/163260
        #http://www.yangbeom.link/post/130613532096/python%EC%9D%84-%EC%9D%B4%EC%9A%A9%ED%95%9C-%ED%81%B4%EB%A6%AC%EC%95%99-%ED%8C%8C%EC%84%9C%EB%A7%8C%EB%93%A4%EA%B8%B0-beautifulsoup-%EC%82%AC%EC%9A%A9%ED%8E%B8
                    self.emit(QtCore.SIGNAL('loggingWork'), "=======Downloading and Parsing HTML files "+str(indexOfItems)+"/"+str(NumOfTotalItems)+"======")
                    #print "=======Beautiful soup Parsing HTML "+str(indexOfItems)+"/"+str(NumOfTotalItems)+"======"
                   # logOfProgress.setPlainText("=======Beautiful soup Parsing HTML "+str(linkIdx+1)+"/"+str(sizeOfLinks)+"======\n")

                    soup = BeautifulSoup(html,"html5lib") #you have install it with "pip install html5lib"
                   # find_mytr = soup.find_all("tr", attrs={'class':"td_1"})
                  #  print soup
                    #print soup.title.get_text().encode('cp949','ignore') # refer from https://kldp.org/node/81708
                    #itemLocNo = soup.title.get_text().encode('cp949','ignore').split()[0]
                    itemLocNoSplited = soup.title.get_text().split()
                    itemLocNo = itemLocNoSplited[0]+" "+itemLocNoSplited[1]
                    #print soup.title.get_text().encode('cp949','ignore')
                    #print soup.title.get_text()
                   # print soup.find_all(id="Table1")
                    #print soup.find_all("td", class_="td_1")
                    #print soup.select("#Table1 > tbody")
                    #print soup.select("#Table1 > tbody > tr")
                    #print soup.select("#Table1 > tbody > tr + tr")
                    #print soup.select("#Table1 > tbody > tr + tr > td")
                    #print soup.select('td[class="td_1"]')  # I find it!!
                    tdList = soup.select('td[class="td_1"]')
                #    for td in tdList:
                #        print td.get_text(strip=True).encode('cp949','ignore')
                    #itemLocation = tdList[0].get_text(strip=True).encode('cp949','ignore')
                    #itemName = tdList[4].get_text(strip=True).encode('cp949','ignore')
                    itemLocation = tdList[0].get_text(strip=True).split('[')[0]
                    itemLocation = itemLocation.split('(')[0] #without name of road
                    itemName = tdList[4].get_text(strip=True)
                    itemExpectedPrice = tdList[6].get_text(strip=True)
                    itemMinPrice = tdList[9].get_text(strip=True)
                    #itemPrice = itemExpectedPrice+" / "+itemMinPrice
                    #print itemName
                    #print itemLocNo
                    #print itemLocation
                    items = [itemLocNo, itemName, itemLocation, itemExpectedPrice, itemMinPrice]

                    itemsList.append(items)



                    rowidx = rowidx+1
                    for colindx, item in enumerate(items):
                        worksheet.write(rowidx, colindx, item)

                    if(self.super.crawl_flag):
                        print "Close Excel File"
                        workbook.close() #page End if button will be clicked , I have to make it
                        break

                if(self.super.crawl_flag):
                    print "break outer loop"
                    break


                # Write some numbers, with row/column notation.

                #for rowidx, items in enumerate(itemsList):
                #    for colindx, item in enumerate(items):
                #        worksheet.write(rowidx+1, colindx, item)



            print "End of Loop"
            workbook.close() #page Final End
            self.emit(QtCore.SIGNAL('finishedWork'), "hi program finished from thread")

            #workbook 닫는 타이밍
            #사건번호 정규식 및 엔터
            #Python regex test web   regexr.com






                    #print soup.select("#Table1 > tbody > tr + tr > td.td_1")
                    #//*[@id="Table1"]/tbody/tr[1]/td[2]
                    ##Table1 > tbody > tr:nth-child(1) > td.td_1  ## error reason : http://stackoverflow.com/questions/24720442/selecting-second-child-in-beautiful-soup-with-soup-select

                    #print find_mytr
                    #for t in find_mytr:
                    #    print t.get_text(strip=True).encode('cp949','ignore').decode('cp949')

                 #   filenmae = 'test.html'
                 #   with open(filenmae, 'wb') as f:
                 #       f.write(html)


#if __name__ == '__main__':
#    app = QtGui.QApplication(sys.argv)
#    w = Form()
#    sys.exit(app.exec_())

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Dialog = QtGui.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())


#        Dialog = QtGui.QDialog()
#        ui = Ui_Dialog()
#        self.ui = ui.setupUi(Dialog) #def setupUi(self, Dialog):
        #Dialog.show()