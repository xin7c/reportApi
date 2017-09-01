#!/usr/bin/env python
# encoding: utf-8

class ResponseIsNullException(Exception):
    def __init__(self, errorAppid=None):
        Exception.__init__(self)
        self.reason = u"[异常]:返回值为空Json\n[appid]%s" %errorAppid
        print self.reason