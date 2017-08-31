#!/usr/bin/env python
# encoding: utf-8

"""
@author: xuchu
@software: PyCharm
@file: report_cases.py
@time: 2017/8/28 下午2:01
"""
import sys

reload(sys)
sys.setdefaultencoding('utf8')
from report_main import Report_Api
from nose.tools import *
from datetime import *
import json
from tools.localException import ResponseIsNullException


def checkReportName(req_reportname, res):
    """断言：提交reportname: 返回reportname"""
    try:
        json_res = json.loads(res)["reportname"][0]
        eq_(req_reportname, json_res, "No %s" % json_res)
    except:
        raise ResponseIsNullException("Null")
def test_026_sdk_debug_device_count():
    """026:新建APP>>数据测试>>调试设备列表"""
    ra = Report_Api("0c88f597eba1f531d7318eb7c092c69f")
    reportname = "sdk_debug_device_count"
    data = {
        "appid": ra.appid
    }
    res = ra.action(reportname, data)
    checkReportName(reportname, res)