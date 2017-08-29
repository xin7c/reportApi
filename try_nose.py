#!/usr/bin/env python
# encoding: utf-8

"""
@author: xuchu
@software: PyCharm
@file: try_nose.py
@time: 2017/8/28 下午4:44
"""

from report_main import Report_Api
import nose
from nose import with_setup
from nose.tools import *
from nose.case import Test
import unittest

def setUp():
    print "gogogo"

def tearDown():
    print "end"
@with_setup(setUp, tearDown)
def test_01_aa():
    ra = Report_Api()
    reportname = "channelinfo_install_top5_byhour"
    data = {
        "startdate": "2017-07-01",
        "enddate": "2017-08-28"
    }
    print ra.action(reportname, data)

def test_02_aa():
    ra = Report_Api()
    reportname = "channelinfo_install_top5_byhour"
    data = {
        "startdate": "2017-07-01",
        "enddate": "2017-08-28"
    }
    print ra.action(reportname, data)

if __name__ == "__main__":
    pass