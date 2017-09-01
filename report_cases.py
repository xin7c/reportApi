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
from nose.plugins.skip import SkipTest
from nose.plugins.attrib import attr
from datetime import *
import json
from tools.localException import ResponseIsNullException


class Test_Report(object):
    def __init__(self):
        self.appid = "0c88f597eba1f531d7318eb7c092c69f"
        self.campaignid = "_default_"
        self.data = {
            "startdate": "2017-07-01",
            "enddate": "2017-08-28"
        }
        self.data_install_pay = {
            "install_startdate": "2017-01-01",
            "install_enddate": "2017-08-28",
            "pay_startdate": "2017-01-01",
            "pay_enddate": "2017-08-28"
        }

    def setUp(self):
        print "[Start] @ %s" % datetime.today()
        self.ra = Report_Api(self.appid)

    def tearDown(self):
        print "[End] @ %s" % datetime.today()

    def checkReportName(self, req_reportname, res):
        """断言：提交reportname: 返回reportname"""
        try:
            json_res = json.loads(res)["reportname"][0]
            eq_(req_reportname, json_res, "No %s" % json_res)
        except:
            raise ResponseIsNullException(self.ra.appid)

    def test_001_channelinfo_install_top5_byhour(self):
        """001:来源分析>>渠道效果对比>>激活趋势TOP5"""
        reportname = "channelinfo_install_top5_byhour"
        data = self.data
        res = self.ra.action(reportname, data)
        self.checkReportName(reportname, res)

    def test_002_realtime_payer(self):
        """002:实时>>实时点击量"""
        reportname = "realtime_payer"
        data = self.data
        res = self.ra.action(reportname, data)
        self.checkReportName(reportname, res)

    def test_003_install_byhour(self):
        """003:仪表盘>>激活量趋势（按小时）"""
        reportname = "install_byhour"
        data = self.data
        res = self.ra.action(reportname, data)
        self.checkReportName(reportname, res)

    def test_004_campaigninfo_bypackagecampaign(self):
        """004:来源分析>>推广活动详情"""
        reportname = "campaigninfo_bypackagecampaign"
        data = self.data
        res = self.ra.action(reportname, data)
        self.checkReportName(reportname, res)

    def test_005_campaigninfo_bysubpackagecampaign(self):
        """005:来源分析>>分包推广活动详情>>子活动"""
        reportname = "campaigninfo_bysubpackagecampaign"
        data = self.data
        res = self.ra.action(reportname, data)
        self.checkReportName(reportname, res)

    def test_006_roi_bychannel(self):
        """006:来源分析>>推广活动详情>>百度关键词???"""
        reportname = "roi_bychannel"
        res = self.ra.action(reportname, self.data_install_pay)
        self.checkReportName(reportname, res)

    def test_007_channelinfo_base_top5_bychannel(self):
        """007:来源分析>>渠道效果对比>>基础数据top5（有实时）"""
        reportname = "channelinfo_base_top5_bychannel"
        data = self.data
        res = self.ra.action(reportname, data)
        self.checkReportName(reportname, res)

    def test_008_channelincome_top10_bychannel(self):
        """008:仪表盘>>渠道收入top10"""
        reportname = "channelincome_top10_bychannel"
        data = self.data
        res = self.ra.action(reportname, data)
        self.checkReportName(reportname, res)

    def test_009_retention_dau_dau_byds(self):
        """009:活跃活跃日留存"""
        reportname = "retention_dau_dau_byds"
        data = self.data
        data["usergroupsql"] = ""
        res = self.ra.action(reportname, data)
        self.checkReportName(reportname, res)

    def test_010_realtime_dau(self):
        """010:实时>>实时DAU"""
        reportname = "realtime_dau"
        data = self.data
        res = self.ra.action(reportname, data)
        self.checkReportName(reportname, res)

    def test_011_realtime_dupclick(self):
        """011:实时>>实时排重点击"""
        reportname = "realtime_dupclick"
        data = self.data
        res = self.ra.action(reportname, data)
        self.checkReportName(reportname, res)

    def test_012_retention_install_dau_byweekk(self):
        """012:新增活跃日留存"""
        reportname = "retention_install_dau_byweek"
        data = self.data
        data["usergroupsql"] = ""
        res = self.ra.action(reportname, data)
        self.checkReportName(reportname, res)

    def test_013_realtime_install(self):
        """013:新增活跃日留存？？？"""
        reportname = "realtime_install"
        data = self.data
        res = self.ra.action(reportname, data)
        self.checkReportName(reportname, res)

    def test_014_decision_payment_level_byds(self):
        """014:决策支持>>付费洞察>>新用户已付费情况"""
        reportname = "decision_payment_level_byds"
        data = self.data
        res = self.ra.action(reportname, data)
        self.checkReportName(reportname, res)

    def test_015_rate_install_byds(self):
        """015:仪表盘>>激活率趋势（按天）"""
        reportname = "rate_install_byds"
        data = self.data
        res = self.ra.action(reportname, data)
        self.checkReportName(reportname, res)

    def test_016_rate_install_byhour(self):
        """016:仪表盘>>激活率趋势（按小时）"""
        reportname = "rate_install_byhour"
        data = self.data
        res = self.ra.action(reportname, data)
        self.checkReportName(reportname, res)

    def test_017_device_bymodel(self):
        """017:决策支持>>设备分析>>型号列表"""
        reportname = "device_bymodel"
        data = self.data
        res = self.ra.action(reportname, data)
        self.checkReportName(reportname, res)

    def test_018_device_byos(self):
        """017:决策支持>>设备分析>>系统列表"""
        reportname = "device_byos"
        data = self.data
        res = self.ra.action(reportname, data)
        self.checkReportName(reportname, res)

    def test_019_bd_bykwid(self):
        """019:来源分析>>推广活动详情>>百度关键词"""
        reportname = "bd_bykwid"
        data = self.data
        data["campaignid"] = "_default_"
        res = self.ra.action(reportname, data)
        self.checkReportName(reportname, res)

    def test_020_income_byhour(self):
        """020:仪表盘>>收入趋势（按小时）"""
        reportname = "income_byhour"
        data = self.data
        res = self.ra.action(reportname, data)
        self.checkReportName(reportname, res)

    def test_021_device_bycarrier(self):
        """021:决策支持>>设备分析>>运营商列表"""
        reportname = "device_bycarrier"
        data = self.data
        res = self.ra.action(reportname, data)
        self.checkReportName(reportname, res)

    def test_022_rate_retentiond1_byds(self):
        """022:仪表盘>>次日留存趋势（按天）"""
        reportname = "rate_retentiond1_byds"
        data = self.data
        res = self.ra.action(reportname, data)
        self.checkReportName(reportname, res)

    def test_023_retention_dau_dau_bymonth(self):
        """023:活跃活跃月留存"""
        reportname = "retention_dau_dau_bymonth"
        data = self.data
        data["usergroupsql"] = ""
        res = self.ra.action(reportname, data)
        self.checkReportName(reportname, res)

    def test_024_decision_payment_rmb_byds(self):
        """024:决策支持>>付费洞察>>新用户付费分布"""
        reportname = "decision_payment_rmb_byds"
        data = self.data
        res = self.ra.action(reportname, data)
        self.checkReportName(reportname, res)

    def test_025_campaigninfo_h5_bycampaign(self):
        """025:来源分析>>推广活动详情>>推广活动>>H5监测数据"""
        reportname = "campaigninfo_h5_bycampaign"
        data = self.data
        res = self.ra.action(reportname, data)
        self.checkReportName(reportname, res)

    @attr(mode='1')
    def test_026_sdk_debug_device_count(self):
        """026:新建APP>>数据测试>>调试设备列表"""
        reportname = "sdk_debug_device_count"
        data = {
            "datatype": "list"
        }
        res = self.ra.action(reportname, data)
        self.checkReportName(reportname, res)

    def test_027_click_byhour(self):
        """027:仪表盘>>点击量趋势（按小时）"""
        reportname = "click_byhour"
        data = self.data
        res = self.ra.action(reportname, data)
        self.checkReportName(reportname, res)

    def test_028_bd_bycampaign_count(self):
        """028:来源分析>>推广活动详情>>百度关键词???"""
        reportname = "bd_bycampaign_count"
        data = self.data
        res = self.ra.action(reportname, data)
        self.checkReportName(reportname, res)

    def test_029_channelinfo_reged_top5_byds(self):
        """029:来源分析>>渠道效果对比>>注册趋势TOP5"""
        reportname = "channelinfo_reged_top5_byds"
        data = self.data
        res = self.ra.action(reportname, data)
        self.checkReportName(reportname, res)

    def test_030_bd_bycreative(self):
        """030:来源分析>>推广活动详情>>百度关键词???"""
        reportname = "bd_bycreative"
        data = self.data
        data["campaignid"] = "_default_"
        res = self.ra.action(reportname, data)
        self.checkReportName(reportname, res)
