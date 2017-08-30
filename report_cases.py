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


class Test_Report(object):
    def setUp(self):
        print "[Start] @ %s" % datetime.today()
        self.ra = Report_Api()

    def tearDown(self):
        print "[End] @ %s" % datetime.today()

    def checkReportName(self, req_reportname, res):
        """断言：提交reportname: 返回reportname"""
        json_res = json.loads(res)["reportname"][0]
        eq_(req_reportname, json_res, "No %s" % json_res)

    def test_001_channelinfo_install_top5_byhour(self):
        """001:来源分析>>渠道效果对比>>激活趋势TOP5"""
        reportname = "channelinfo_install_top5_byhour"
        data = {
            "startdate": "2017-07-01",
            "enddate": "2017-08-28"
        }
        res = self.ra.action(reportname, data)
        print res
        self.checkReportName(reportname, res)

    def test_002_realtime_payer(self):
        """002:实时>>实时点击量"""
        reportname = "realtime_payer"
        data = {
            "startdate": "2017-07-01",
            "enddate": "2017-08-28"
        }
        res = self.ra.action(reportname, data)
        print res
        self.checkReportName(reportname, res)

    def test_003_install_byhour(self):
        """003:仪表盘>>激活量趋势（按小时）"""
        reportname = "install_byhour"
        data = {
            "startdate": "2017-07-01",
            "enddate": "2017-08-28"
        }
        print self.ra.action(reportname, data)

    def test_004_campaigninfo_bypackagecampaign(self):
        """004:来源分析>>推广活动详情"""
        reportname = "campaigninfo_bypackagecampaign"
        data = {
            "startdate": "2017-07-01",
            "enddate": "2017-08-28"
        }
        res = self.ra.action(reportname, data)
        print res
        self.checkReportName(reportname, res)

    def test_005_campaigninfo_bysubpackagecampaign(self):
        """005:来源分析>>分包推广活动详情>>子活动"""
        reportname = "campaigninfo_bysubpackagecampaign"
        data = {
            "startdate": "2017-07-01",
            "enddate": "2017-08-28"
        }
        res = self.ra.action(reportname, data)
        print res
        self.checkReportName(reportname, res)

    def test_006_roi_bychannel(self):
        """006:来源分析>>推广活动详情>>百度关键词"""
        reportname = "roi_bychannel"
        data = {
            "install_startdate": "2017-01-01",
            "install_enddate": "2017-08-28",
            "pay_startdate": "2017-01-01",
            "pay_enddate": "2017-08-28"
        }
        res = self.ra.action(reportname, data)
        print res
        self.checkReportName(reportname, res)

    def test_007_channelinfo_base_top5_bychannel(self):
        """007:来源分析>>渠道效果对比>>基础数据top5（有实时）"""
        reportname = "channelinfo_base_top5_bychannel"
        data = {
            "startdate": "2017-07-01",
            "enddate": "2017-08-28"
        }
        res = self.ra.action(reportname, data)
        print res
        self.checkReportName(reportname, res)

    def test_008_channelincome_top10_bychannel(self):
        """008:仪表盘>>渠道收入top10"""
        reportname = "channelincome_top10_bychannel"
        data = {
            "startdate": "2017-07-01",
            "enddate": "2017-08-28"
        }
        res = self.ra.action(reportname, data)
        print res
        self.checkReportName(reportname, res)

    def test_009_retention_dau_dau_byds(self):
        """009:活跃活跃日留存"""
        reportname = "retention_dau_dau_byds"
        data = {
            "startdate": "2017-07-01",
            "enddate": "2017-08-28",
            "usergroupsql": ""
        }
        res = self.ra.action(reportname, data)
        print res
        self.checkReportName(reportname, res)

    def test_010_realtime_dau(self):
        """010:实时>>实时DAU"""
        reportname = "realtime_dau"
        data = {
            "startdate": "2017-07-01",
            "enddate": "2017-08-28",
        }
        res = self.ra.action(reportname, data)
        print res
        self.checkReportName(reportname, res)

    def test_011_realtime_dupclick(self):
        """011:实时>>实时排重点击"""
        reportname = "realtime_dupclick"
        data = {
            "startdate": "2017-07-01",
            "enddate": "2017-08-28",
        }
        res = self.ra.action(reportname, data)
        print res
        self.checkReportName(reportname, res)

    def test_012_retention_install_dau_byweekk(self):
        """012:新增活跃日留存"""
        reportname = "retention_install_dau_byweek"
        data = {
            "startdate": "2017-07-01",
            "enddate": "2017-08-28",
            "usergroupsql": ""
        }
        res = self.ra.action(reportname, data)
        print res
        self.checkReportName(reportname, res)

    def test_013_realtime_install(self):
        """013:新增活跃日留存？？？"""
        reportname = "realtime_install"
        data = {
            "startdate": "2017-07-01",
            "enddate": "2017-08-28",
        }
        res = self.ra.action(reportname, data)
        print res
        self.checkReportName(reportname, res)

    def test_014_decision_payment_level_byds(self):
        """014:决策支持>>付费洞察>>新用户已付费情况"""
        reportname = "decision_payment_level_byds"
        data = {
            "startdate": "2017-07-01",
            "enddate": "2017-08-28",
        }
        res = self.ra.action(reportname, data)
        print res
        self.checkReportName(reportname, res)

    def test_015_rate_install_byds(self):
        """015:仪表盘>>激活率趋势（按天）"""
        reportname = "rate_install_byds"
        data = {
            "startdate": "2017-07-01",
            "enddate": "2017-08-28",
        }
        res = self.ra.action(reportname, data)
        print res
        self.checkReportName(reportname, res)

    def test_016_rate_install_byhour(self):
        """016:仪表盘>>激活率趋势（按小时）"""
        reportname = "rate_install_byhour"
        data = {
            "startdate": "2017-07-01",
            "enddate": "2017-08-28",
        }
        res = self.ra.action(reportname, data)
        print res
        self.checkReportName(reportname, res)

    def test_017_device_bymodel(self):
        """017:决策支持>>设备分析>>型号列表"""
        reportname = "device_bymodel"
        data = {
            "startdate": "2017-07-01",
            "enddate": "2017-08-28",
        }
        res = self.ra.action(reportname, data)
        print res
        self.checkReportName(reportname, res)

    def test_018_device_byos(self):
        """017:决策支持>>设备分析>>系统列表"""
        reportname = "device_byos"
        data = {
            "startdate": "2017-07-01",
            "enddate": "2017-08-28",
        }
        res = self.ra.action(reportname, data)
        print res
        self.checkReportName(reportname, res)

    def test_019_bd_bykwid(self):
        """019:来源分析>>推广活动详情>>百度关键词"""
        reportname = "bd_bykwid"
        data = {
            "startdate": "2017-07-01",
            "enddate": "2017-08-28",
            "campaignid": "_default_"
        }
        res = self.ra.action(reportname, data)
        print res
        self.checkReportName(reportname, res)

    def test_020_income_byhour(self):
        """020:仪表盘>>收入趋势（按小时）"""
        reportname = "income_byhour"
        data = {
            "startdate": "2017-07-01",
            "enddate": "2017-08-28",
            "campaignid": "_default_"
        }
        res = self.ra.action(reportname, data)
        print res
        self.checkReportName(reportname, res)
