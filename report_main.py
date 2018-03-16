#!/usr/bin/env python
# encoding=utf-8
# @Author  : xuchu
# @File    : report_main.py
# @Software: PyCharm

import requests
import urllib
import time
import os
import pprint


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

    def __init__(self, appid):
        self.headers = {
            "Content-Type": "application/x-www-form-urlencoded"
        }
        self.host = "http://ec2-54-223-136-157.cn-north-1.compute.amazonaws.com.cn:8089/api/trackingio"
        self.appid = appid
        # self.appid = "0c88f597eba1f531d7318eb7c092c69f"

    def url_Maker(self, reportname):
        """input : urlencode_data"""
        _url = os.path.join(self.host, reportname, self.appid)
        return _url

    def action(self, reportname=None, data=None):
        """action"""
        url = self.url_Maker(reportname=reportname)
        r = requests.post(headers=self.headers, url=url, data=data, timeout=5)
        result = r.text
        # print r.url
        # print data
        print result
        return result


# if __name__ == "__main__":
#     ra = Report_Api()
#     ra.action()
