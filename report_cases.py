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
            "startdate": "2017-08-01",
            "enddate": "2017-08-28"
        }
        self.data_install_pay = {
            "install_startdate": "2017-08-01",
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
        data["datatype"] = "char"
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

    def test_012_retention_install_dau_byweek(self):
        """012:新增活跃日留存"""
        reportname = "retention_install_dau_byweek"
        data = self.data
        data["usergroupsql"] = ""
        data["datatype"] = "char"
        res = self.ra.action(reportname, data)
        self.checkReportName(reportname, res)

    def test_013_bd_bycampaign(self):
        """013:来源分析>>推广活动详情>>百度关键词???"""
        reportname = "bd_bycampaign"
        data = self.data
        data["campaignid"] = "_default"
        res = self.ra.action(reportname, data)
        self.checkReportName(reportname, res)

    def test_014_roi_byds(self):
        """014:来源分析>>推广活动详情>>百度关键词???"""
        reportname = "roi_byds"
        data = self.data_install_pay
        data["datatype"] = "list"
        res = self.ra.action(reportname, data)
        self.checkReportName(reportname, res)

    def test_015_reged_byds(self):
        """042:仪表盘>>注册量趋势（按天）"""
        reportname = "reged_byds"
        data = self.data
        res = self.ra.action(reportname, data)
        self.checkReportName(reportname, res)

    def test_016_realtime_income(self):
        """016:实时>>实时点击量"""
        reportname = "realtime_income"
        data = self.data
        res = self.ra.action(reportname, data)
        self.checkReportName(reportname, res)

    def test_017_channelinfo_click_top5_byds(self):
        """017:来源分析>>渠道效果对比>>点击趋势TOP5"""
        reportname = "channelinfo_click_top5_byds"
        data = self.data
        res = self.ra.action(reportname, data)
        self.checkReportName(reportname, res)

    def test_018_bd_bycreative(self):
        """018:来源分析>>推广活动详情>>百度关键词???"""
        reportname = "bd_bycreative"
        data = self.data
        data["campaignid"] = self.campaignid
        res = self.ra.action(reportname, data)
        self.checkReportName(reportname, res)

    def test_019_campaigninfo_bydatecampaign(self):
        """019:来源分析>>推广活动详情>>推广活动按日期分组???"""
        reportname = "campaigninfo_bydatecampaign"
        data = self.data
        res = self.ra.action(reportname, data)
        self.checkReportName(reportname, res)

    def test_020_device_byresolution(self):
        """020:决策支持>>设备分析>>分辨率列表???"""
        reportname = "device_byresolution"
        data = self.data
        res = self.ra.action(reportname, data)
        self.checkReportName(reportname, res)

    def test_021_channelinfo_reged_top5_byhour(self):
        """021:来源分析>>渠道效果对比>>注册趋势TOP5???"""
        reportname = "channelinfo_reged_top5_byhour"
        data = self.data
        res = self.ra.action(reportname, data)
        self.checkReportName(reportname, res)

    def test_022_campaigninfo_bycampgroup(self):
        """022:来源分析>>推广活动详情>>推广活动组???"""
        reportname = "campaigninfo_bycampgroup"
        data = self.data
        res = self.ra.action(reportname, data)
        self.checkReportName(reportname, res)

    def test_023_dau_byhour(self):
        """023:仪表盘>>DAU趋势（按小时）"""
        reportname = "dau_byhour"
        data = self.data
        res = self.ra.action(reportname, data)
        self.checkReportName(reportname, res)

    def test_024_campaigninfo_bychannel(self):
        """024:来源分析>>推广活动详情>>推广活动"""
        reportname = "campaigninfo_bychannel"
        data = self.data
        res = self.ra.action(reportname, data)
        self.checkReportName(reportname, res)

    def test_025_install_byds(self):
        """025:仪表盘>>激活量趋势（按天）"""
        reportname = "install_byds"
        data = self.data
        res = self.ra.action(reportname, data)
        self.checkReportName(reportname, res)

    def test_026_channelinfo_bychannel(self):
        """026:来源分析>>渠道效果对比>>渠道详情"""
        reportname = "channelinfo_bychannel"
        data = self.data
        res = self.ra.action(reportname, data)
        self.checkReportName(reportname, res)

    def test_027_retention_install_dau_byweekk(self):
        """027:新增活跃日留存[重复于012]"""
        reportname = "retention_install_dau_byweek"
        data = self.data
        data["usergroupsql"] = ""
        data["datatype"] = "char"
        res = self.ra.action(reportname, data)
        self.checkReportName(reportname, res)

    def test_028_realtime_install(self):
        """028:新增活跃日留存？？？"""
        reportname = "realtime_install"
        data = self.data
        res = self.ra.action(reportname, data)
        self.checkReportName(reportname, res)

    def test_029_decision_payment_level_byds(self):
        """029:决策支持>>付费洞察>>新用户已付费情况"""
        reportname = "decision_payment_level_byds"
        data = self.data
        res = self.ra.action(reportname, data)
        self.checkReportName(reportname, res)

    def test_030_rate_install_byds(self):
        """030:仪表盘>>激活率趋势（按天）"""
        reportname = "rate_install_byds"
        data = self.data
        res = self.ra.action(reportname, data)
        self.checkReportName(reportname, res)

    def test_031_rate_install_byhour(self):
        """031:仪表盘>>激活率趋势（按小时）"""
        reportname = "rate_install_byhour"
        data = self.data
        res = self.ra.action(reportname, data)
        self.checkReportName(reportname, res)

    def test_032_device_bymodel(self):
        """032:决策支持>>设备分析>>型号列表"""
        reportname = "device_bymodel"
        data = self.data
        res = self.ra.action(reportname, data)
        self.checkReportName(reportname, res)

    def test_033_device_byos(self):
        """033:决策支持>>设备分析>>系统列表"""
        reportname = "device_byos"
        data = self.data
        res = self.ra.action(reportname, data)
        self.checkReportName(reportname, res)

    def test_034_bd_bykwid(self):
        """034:来源分析>>推广活动详情>>百度关键词???"""
        reportname = "bd_bykwid"
        data = self.data
        data["campaignid"] = "_default_"
        res = self.ra.action(reportname, data)
        self.checkReportName(reportname, res)

    def test_035_income_byhour(self):
        """035:仪表盘>>收入趋势（按小时）"""
        reportname = "income_byhour"
        data = self.data
        res = self.ra.action(reportname, data)
        self.checkReportName(reportname, res)

    def test_036_device_bycarrier(self):
        """036:决策支持>>设备分析>>运营商列表"""
        reportname = "device_bycarrier"
        data = self.data
        res = self.ra.action(reportname, data)
        self.checkReportName(reportname, res)

    def test_037_rate_retentiond1_byds(self):
        """037:仪表盘>>次日留存趋势（按天）"""
        reportname = "rate_retentiond1_byds"
        data = self.data
        res = self.ra.action(reportname, data)
        self.checkReportName(reportname, res)

    def test_038_retention_dau_dau_bymonth(self):
        """038:活跃活跃月留存"""
        reportname = "retention_dau_dau_bymonth"
        data = self.data
        data["usergroupsql"] = ""
        data["datatype"] = "char"
        res = self.ra.action(reportname, data)
        self.checkReportName(reportname, res)

    def test_039_decision_payment_rmb_byds(self):
        """039:决策支持>>付费洞察>>新用户付费分布"""
        reportname = "decision_payment_rmb_byds"
        data = self.data
        res = self.ra.action(reportname, data)
        self.checkReportName(reportname, res)

    def test_040_campaigninfo_h5_bycampaign(self):
        """040:来源分析>>推广活动详情>>推广活动>>H5监测数据"""
        reportname = "campaigninfo_h5_bycampaign"
        data = self.data
        res = self.ra.action(reportname, data)
        self.checkReportName(reportname, res)

    def test_041_sdk_debug_device_count(self):
        """041:新建APP>>数据测试>>调试设备列表"""
        reportname = "sdk_debug_device_count"
        data = {
            "datatype": "list"
        }
        res = self.ra.action(reportname, data)
        self.checkReportName(reportname, res)

    def test_042_click_byhour(self):
        """042:仪表盘>>点击量趋势（按小时）"""
        reportname = "click_byhour"
        data = self.data
        res = self.ra.action(reportname, data)
        self.checkReportName(reportname, res)

    def test_043_bd_bycampaign_count(self):
        """043:来源分析>>推广活动详情>>百度关键词???"""
        reportname = "bd_bycampaign_count"
        data = self.data
        res = self.ra.action(reportname, data)
        self.checkReportName(reportname, res)

    def test_044_channelinfo_reged_top5_byds(self):
        """044:来源分析>>渠道效果对比>>注册趋势TOP5???"""
        reportname = "channelinfo_reged_top5_byds"
        data = self.data
        res = self.ra.action(reportname, data)
        self.checkReportName(reportname, res)

    def test_045_bd_bycreative(self):
        """045:来源分析>>推广活动详情>>百度关键词???[重复于18]"""
        reportname = "bd_bycreative"
        data = self.data
        data["campaignid"] = "_default_"
        res = self.ra.action(reportname, data)
        self.checkReportName(reportname, res)

    def test_046_retention_dau_dau_byweek(self):
        """046:活跃活跃周留存"""
        reportname = "retention_dau_dau_byweek"
        data = self.data
        data["usergroupsql"] = ""
        data["datatype"] = "char"
        res = self.ra.action(reportname, data)
        self.checkReportName(reportname, res)



