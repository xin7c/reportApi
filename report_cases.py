#!/usr/bin/env python
# encoding: utf-8

"""
@author: xuchu
@software: PyCharm
@file: report_cases.py
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


# def test_action():
#     pass

class Test_Report(object):
    def __init__(self):

        self.appid = "453c2f5cc4a2cf56763f8211be2cd2e5"
        # self.appid = "e31caee07ebedf8c172267e73204802f"
        self.campaignid = "_default_"
        self.categoryid = "38"
        self.cid = "23"
        self.usergroupsql = ""
        self.subchannel = "__CID__"
        self.datatype_list = "list"
        self.datatype_char = "char"
        self.data = {
            "startdate": "2018-01-01",
            "enddate": "2018-03-05"
        }
        self.data_install_pay = {
            "install_startdate": "2018-01-01",
            "install_enddate": "2018-03-05",
            "pay_startdate": "2018-01-01",
            "pay_enddate": "2018-03-05"
        }
        self.ra = Report_Api(self.appid)

    def setUp(self):
        print "[Start] @ %s" % datetime.today()

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
        """001:来源分析>>渠道效果对比>>激活趋势TOP5???"""
        reportname = "channelinfo_install_top5_byhour"
        data = self.data
        res = self.ra.action(reportname, data)
        self.checkReportName(reportname, res)

    def test_002_realtime_payer(self):
        """002:实时>>实时点击量???"""
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
        """009:活跃活跃日留存???"""
        reportname = "retention_dau_dau_byds"
        data = self.data
        data["usergroupsql"] = self.usergroupsql
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
        data["usergroupsql"] = self.usergroupsql
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
        """016:实时>>实时点击量???"""
        reportname = "realtime_income"
        data = self.data
        res = self.ra.action(reportname, data)
        self.checkReportName(reportname, res)

    def test_017_channelinfo_click_top5_byds(self):
        """017:来源分析>>渠道效果对比>>点击趋势TOP5???"""
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
        """024:来源分析>>推广活动详情>>推广活动???"""
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
        data["usergroupsql"] = self.usergroupsql
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
        """038:活跃活跃月留存???"""
        reportname = "retention_dau_dau_bymonth"
        data = self.data
        data["usergroupsql"] = self.usergroupsql
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
        """040:来源分析>>推广活动详情>>推广活动>>H5监测数据???"""
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
        """045:来源分析>>推广活动详情>>百度关键词???[重复于018]"""
        reportname = "bd_bycreative"
        data = self.data
        data["campaignid"] = "_default_"
        res = self.ra.action(reportname, data)
        self.checkReportName(reportname, res)

    def test_046_retention_dau_dau_byweek(self):
        """046:活跃活跃周留存"""
        reportname = "retention_dau_dau_byweek"
        data = self.data
        data["usergroupsql"] = self.usergroupsql
        data["datatype"] = "char"
        res = self.ra.action(reportname, data)
        self.checkReportName(reportname, res)

    def test_047_campaigninfo_bycampaign(self):
        """047:来源分析>>推广活动详情>>推广活动???"""
        reportname = "campaigninfo_bycampaign"
        data = self.data
        res = self.ra.action(reportname, data)
        self.checkReportName(reportname, res)

    def test_048_rate_channelinfo_install_top5_bychannel(self):
        """048:来源分析>>渠道效果对比>>激活率top5（有实时）"""
        reportname = "rate_channelinfo_install_top5_bychannel"
        data = self.data
        res = self.ra.action(reportname, data)
        self.checkReportName(reportname, res)

    def test_049_decision_potencial_top10_bychannel(self):
        """049:决策支持>>潜在用户群>>潜在用户推广来源top10"""
        reportname = "decision_potencial_top10_bychannel"
        data = self.data
        data["categoryid"] = self.categoryid
        res = self.ra.action(reportname, data)
        self.checkReportName(reportname, res)

    def test_050_rate_channelinfo_install_top5_byds(self):
        """050:来源分析>>渠道效果对比>>点击趋势TOP5???"""
        reportname = "rate_channelinfo_install_top5_byds"
        data = self.data
        res = self.ra.action(reportname, data)
        self.checkReportName(reportname, res)

    def test_051_channelinfo_click_top5_byhour(self):
        """051:来源分析>>渠道效果对比>>点击趋势TOP5???"""
        reportname = "channelinfo_click_top5_byhour"
        data = self.data
        res = self.ra.action(reportname, data)
        self.checkReportName(reportname, res)

    def test_052_home_dau_bygeo(self):
        """052:门户地图报表"""
        reportname = "home_dau_bygeo"
        data = self.data
        res = self.ra.action(reportname, data)
        self.checkReportName(reportname, res)

    def test_053_channelinfo_payer_top5_byhour(self):
        """053:来源分析>>渠道效果对比>>付费设备趋势TOP5???"""
        reportname = "channelinfo_payer_top5_byhour"
        data = self.data
        res = self.ra.action(reportname, data)
        self.checkReportName(reportname, res)

    def test_054_subchannel_bycampaign(self):
        """054:来源分析>>推广活动详情>>子渠道???"""
        reportname = "subchannel_bycampaign"
        data = self.data
        data["subchannel"] = self.subchannel
        res = self.ra.action(reportname, data)
        self.checkReportName(reportname, res)

    def test_055_subchannel_bycampaign(self):
        """055:仪表盘>>DAU趋势（按天）"""
        reportname = "dau_byds"
        data = self.data
        res = self.ra.action(reportname, data)
        self.checkReportName(reportname, res)

    def test_056_channelclick_top10_bychannel(self):
        """056:仪表盘>>渠道点击top10"""
        reportname = "channelclick_top10_bychannel"
        data = self.data
        res = self.ra.action(reportname, data)
        self.checkReportName(reportname, res)

    def test_057_reged_byhour(self):
        """057:仪表盘>>注册量趋势（按小时）"""
        reportname = "reged_byhour"
        data = self.data
        res = self.ra.action(reportname, data)
        self.checkReportName(reportname, res)

    def test_058_retention_install_dau_byds(self):
        """058:新增活跃日留存"""
        reportname = "retention_install_dau_byds"
        data = self.data
        data["usergroupsql"] = self.usergroupsql
        res = self.ra.action(reportname, data)
        self.checkReportName(reportname, res)

    def test_059_retention_install_dau_bymonth(self):
        """059:新增活跃月留存"""
        reportname = "retention_install_dau_bymonth"
        data = self.data
        data["usergroupsql"] = self.usergroupsql
        res = self.ra.action(reportname, data)
        self.checkReportName(reportname, res)

    def test_060_delay_install_bycampaign(self):
        """060:归因分析>>激活延迟分析>>按激活"""
        reportname = "delay_install_bycampaign"
        data = self.data
        res = self.ra.action(reportname, data)
        self.checkReportName(reportname, res)

    def test_061_delay_click_bycampaign(self):
        """061:归因分析>>激活延迟分析>>按点击"""
        reportname = "delay_click_bycampaign"
        data = self.data
        res = self.ra.action(reportname, data)
        self.checkReportName(reportname, res)

    def test_062_app_install_register_byappids(self):
        """062:APP/H5>>APP列表>>激活注册数"""
        reportname = "app_install_register_byappids"
        data = self.data
        data["appid"] = self.appid
        res = self.ra.action(reportname, data)
        self.checkReportName(reportname, res)

    def test_063_retention_install_dau_bymonth(self):
        """063:新增活跃月留存[重复于059]"""
        reportname = "retention_install_dau_bymonth"
        data = self.data
        data["usergroupsql"] = self.usergroupsql
        res = self.ra.action(reportname, data)
        self.checkReportName(reportname, res)

    def test_064_channelinfo_amount_top5_byds(self):
        """064:来源分析>>渠道效果对比>>收入趋势TOP5???"""
        reportname = "channelinfo_amount_top5_byds"
        data = self.data
        res = self.ra.action(reportname, data)
        self.checkReportName(reportname, res)

    def test_065_device_byregion(self):
        """065:决策支持>>设备分析>>地域列表"""
        reportname = "device_byregion"
        data = self.data
        res = self.ra.action(reportname, data)
        self.checkReportName(reportname, res)

    def test_066_retention_dau_dau_byweek(self):
        """066:活跃活跃周留存"""
        reportname = "retention_dau_dau_byweek"
        data = self.data
        data["usergroupsql"] = self.usergroupsql
        res = self.ra.action(reportname, data)
        self.checkReportName(reportname, res)

    def test_067_subchannel_bysubchannel(self):
        """067:来源分析>>推广活动详情>>子渠道???"""
        reportname = "subchannel_bysubchannel"
        data = self.data
        data["cid"] = self.cid
        res = self.ra.action(reportname, data)
        self.checkReportName(reportname, res)

    def test_068_sdk_debug_log(self):
        """068:新建APP>>数据测试>>app测试日志"""
        reportname = "sdk_debug_log"
        data = self.data
        res = self.ra.action(reportname, data)
        self.checkReportName(reportname, res)

    def test_069_subchannel_bychannel(self):
        """069:来源分析>>推广活动详情>>子渠道???"""
        reportname = "subchannel_bychannel"
        data = self.data
        data["campaignid"] = self.campaignid
        res = self.ra.action(reportname, data)
        self.checkReportName(reportname, res)

    def test_070_retention_dau_dau_byds(self):
        """070:活跃活跃日留存"""
        reportname = "retention_dau_dau_byds"
        data = self.data
        data["usergroupsql"] = self.usergroupsql
        res = self.ra.action(reportname, data)
        self.checkReportName(reportname, res)

    def test_071_campaigninfo_h5_bydatecampaign(self):
        """071:来源分析>>推广活动详情>>推广活动>>H5监测数据???"""
        reportname = "campaigninfo_h5_bydatecampaign"
        data = self.data
        res = self.ra.action(reportname, data)
        self.checkReportName(reportname, res)

    def test_072_retention_install_dau_byds(self):
        """072:新增活跃日留存[重复于058]"""
        reportname = "retention_install_dau_byds"
        data = self.data
        data["usergroupsql"] = self.usergroupsql
        res = self.ra.action(reportname, data)
        self.checkReportName(reportname, res)

    def test_073_decision_potencial_bycategory(self):
        """073:决策支持>>潜在用户群>>潜在用户群分析"""
        reportname = "decision_potencial_bycategory"
        data = self.data
        res = self.ra.action(reportname, data)
        self.checkReportName(reportname, res)

    def test_074_channelinstall_top10_bychannel(self):
        """074:仪表盘>>渠道激活top10"""
        reportname = "channelinstall_top10_bychannel"
        data = self.data
        res = self.ra.action(reportname, data)
        self.checkReportName(reportname, res)

    def test_075_device_bynetwork(self):
        """075:决策支持>>设备分析>>网络列表"""
        reportname = "device_bynetwork"
        data = self.data
        res = self.ra.action(reportname, data)
        self.checkReportName(reportname, res)

    def test_076_campaigninfo_byds(self):
        """076:来源分析>>推广活动详情>>日期"""
        reportname = "campaigninfo_byds"
        data = self.data
        res = self.ra.action(reportname, data)
        self.checkReportName(reportname, res)

    def test_077_channelinfo_payer_top5_byds(self):
        """077:来源分析>>渠道效果对比>>付费设备趋势TOP5???"""
        reportname = "channelinfo_payer_top5_byds"
        data = self.data
        res = self.ra.action(reportname, data)
        self.checkReportName(reportname, res)

    def test_078_rate_channelinfo_install_top5_byhour(self):
        """077:来源分析>>渠道效果对比>>点击趋势TOP5???"""
        reportname = "rate_channelinfo_install_top5_byhour"
        data = self.data
        res = self.ra.action(reportname, data)
        self.checkReportName(reportname, res)

    def test_079_channelinfo_install_top5_byds(self):
        """079:来源分析>>渠道效果对比>>激活趋势TOP5???"""
        reportname = "channelinfo_install_top5_byds"
        data = self.data
        res = self.ra.action(reportname, data)
        self.checkReportName(reportname, res)

    def test_080_bd_bykwid_dates(self):
        """080:来源分析>>推广活动详情>>百度关键词按日期"""
        reportname = "bd_bykwid_date"
        data = self.data
        data["campaignid"] = self.campaignid
        res = self.ra.action(reportname, data)
        self.checkReportName(reportname, res)

    def test_081_retention_dau_dau_bymonth(self):
        """081:活跃活跃月留存???[重复于038]"""
        reportname = "retention_dau_dau_bymonth"
        data = self.data
        data["usergroupsql"] = self.usergroupsql
        res = self.ra.action(reportname, data)
        self.checkReportName(reportname, res)

    def test_082_realtime_click(self):
        """082:实时>>实时点击量???"""
        reportname = "realtime_click"
        data = self.data
        res = self.ra.action(reportname, data)
        self.checkReportName(reportname, res)

    def test_083_income_byds(self):
        """083:仪表盘>>收入趋势（按天）"""
        reportname = "income_byds"
        data = self.data
        res = self.ra.action(reportname, data)
        self.checkReportName(reportname, res)

    def test_084_roi_byinterval(self):
        """084:来源分析>>推广活动详情>>百度关键词???"""
        reportname = "roi_byinterval"
        data = self.data_install_pay
        data["datatype"] = "list"
        res = self.ra.action(reportname, data)
        self.checkReportName(reportname, res)

    def test_085_decision_payment_byds(self):
        """085:决策支持>>付费洞察>>新用户付费趋势"""
        reportname = "decision_payment_byds"
        data = self.data
        res = self.ra.action(reportname, data)
        self.checkReportName(reportname, res)

    def test_086_bd_bykwid(self):
        """086:来源分析>>推广活动详情>>百度关键词???[重复于34]"""
        reportname = "bd_bykwid"
        data = self.data
        data["campaignid"] = "_default_"
        res = self.ra.action(reportname, data)
        self.checkReportName(reportname, res)

    def test_087_sdk_debug_events_count(self):
        """087:新建APP>>数据测试>>APP上报事件数"""
        reportname = "sdk_debug_events_count"
        data = {
            "datatype": "list"
        }
        res = self.ra.action(reportname, data)
        self.checkReportName(reportname, res)

    def test_088_rate_channelinfo_retention_top5_bychannel(self):
        """088:来源分析>>渠道效果对比>>留存top5"""
        reportname = "rate_channelinfo_retention_top5_bychannel"
        data = self.data
        res = self.ra.action(reportname, data)
        self.checkReportName(reportname, res)

    def test_089_channelinfo_amount_top5_byhour(self):
        """089:来源分析>>渠道效果对比>>收入趋势TOP5"""
        reportname = "channelinfo_amount_top5_byhour"
        data = self.data
        res = self.ra.action(reportname, data)
        self.checkReportName(reportname, res)

    def test_090_click_byds(self):
        """090:仪表盘>>点击量趋势（按天）"""
        reportname = "click_byds"
        data = self.data
        res = self.ra.action(reportname, data)
        self.checkReportName(reportname, res)

    def test_091_roi_bycampaign(self):
        """091:来源分析>>推广活动详情>>百度关键词???"""
        reportname = "roi_bycampaign"
        data = self.data_install_pay
        res = self.ra.action(reportname, data)
        self.checkReportName(reportname, res)
