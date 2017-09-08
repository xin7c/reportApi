#!/usr/bin/env python
# encoding: utf-8

import json
import reportURI
import requests


class ApiDocChecker():
    def __init__(self):
        self.apiUrl = "http://ec2-54-223-136-157.cn-north-1.compute.amazonaws.com.cn:8089/api/trackingio/allreportinfo"

    def getApi(self):
        r = requests.get(url=self.apiUrl)
        uriList = r.text
        print len(uriList)
        for index, uri in enumerate(json.loads(uriList)):
            print index + 1, ":", uri["reportname"], "^", uri["desc"]


if __name__ == "__main__":
    adc = ApiDocChecker()
    adc.getApi()
