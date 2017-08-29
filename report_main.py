#!/usr/bin/env python
# encoding=utf-8
# @Time    : 2017/8/28 10:10
# @Author  : xuchu
# @File    : report_main.py
# @Software: PyCharm

import requests
import urllib
import time
import os


class TaskName(object):
    def __init__(self):
        """打印执行函数名"""
        pass

    def __call__(self, func):
        def _call(*args, **kw):
            print func.__doc__ + "@ %s" % time.asctime(time.localtime(time.time()))
            return func(*args, **kw)

        return _call


class Report_Api(object):

    def __init__(self):
        self.headers = {
            "Content-Type": "application/json"
        }
        self.host = "http://ec2-54-223-136-157.cn-north-1.compute.amazonaws.com.cn:8089/api/trackingio"
        self.appid = "0c88f597eba1f531d7318eb7c092c69f"

    def url_Maker(self, reportname, urlencode_data):
        """input : urlencode_data"""
        _url = os.path.join(self.host, reportname, self.appid) + "?" + urlencode_data
        return _url

    def action(self, reportname=None, data=None):
        """action"""
        data = urllib.urlencode(data)
        url = self.url_Maker(reportname=reportname,
                             urlencode_data=data)
        r = requests.post(url=url, headers=self.headers)
        return r.text


if __name__ == "__main__":
    ra = Report_Api()
    ra.action()
