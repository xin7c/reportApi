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
ra = Report_Api(appid="0c88f597eba1f531d7318eb7c092c69f")
def setUp():
    print "gogogo"

def tearDown():
    print "end"

def test_009_retention_dau_dau_byds():
    """009:活跃活跃日留存"""
    reportname = "retention_dau_dau_byds"
    data = {
        "startdate": "2017-08-01",
        "enddate": "2017-08-28",
        "datatype": "list",
        "usergroupsql": ""
    }
    ra.action(reportname, data)

if __name__ == "__main__":
    pass