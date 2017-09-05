#!/usr/bin/env python
# encoding: utf-8
uri = [

    {
        "args": "[{name=appid, required=true, example=app unique key, 32字符, 例:37a4c0f4cc0810ccd34c61edb409c6e4}, {name=startdate, required=true, example=起始日期, 例:2016-12-01}, {name=enddate, required=true, example=结束日期, 例:2016-12-07}, {name=subchannel, required=true, example=渠道id, 例：23}, {name=iscache, required=false, example=是否需要缓存, 1为是，0为不缓存，默认1}]",
        "reportname": "subchannel_bysubchannel",
        "datasource": "mysql",
        "column": "[subchannel, num_click_total, num_click, dupnum_click_all, num_ins, dupnum_reg, rate_install]",
        "name": "[子渠道, 点击总数, 有效点击总数, 排重点击数, 排重激活设备数, 排重注册设备数, 激活率]",
        "key": "subchannel",
        "desc": "来源分析>>推广活动详情>>子渠道"
    },
    {
        "args": "[{name=appid, required=true, example=app unique key, 32字符, 例:37a4c0f4cc0810ccd34c61edb409c6e4}, {name=id, required=false, example=数据的ID,例如:1}]",
        "reportname": "sdk_debug_log",
        "datasource": "mysql",
        "column": "[id, appid, xwhat, xwhen, xwho, xwhere, xcontext, ds]",
        "name": "[ID, APPKEY, 事件, 时间, 设备, xwhere, 上报数据, 日期]",
        "key": "id",
        "desc": "新建APP>>数据测试>>app测试日志"
    },
    {
        "args": "[{name=appid, required=true, example=app unique key, 32字符, 例:37a4c0f4cc0810ccd34c61edb409c6e4}, {name=startdate, required=true, example=起始日期, 例:2016-12-01}, {name=enddate, required=true, example=结束日期, 例:2016-12-07}, {name=campaignid, required=true, example=推广活动unique key, 32位, 例：37a4c0f4cc0810ccd34c61edb409c6e4}, {name=iscache, required=false, example=是否需要缓存, 1为是，0为不缓存，默认1}]",
        "reportname": "subchannel_bychannel",
        "datasource": "mysql",
        "column": "[cid, num_click_total, num_click, dupnum_click_all, num_ins, dupnum_reg, rate_install]",
        "name": "[渠道, 点击总数, 有效点击总数, 排重点击数, 排重激活设备数, 排重注册设备数, 激活率]",
        "key": "cid",
        "desc": "来源分析>>推广活动详情>>子渠道"
    },
    {
        "args": "[{name=appid, required=true, example=app unique key, 32字符, 例:37a4c0f4cc0810ccd34c61edb409c6e4}, {name=startdate, required=true, example=起始日期, 例:2016-12-01}, {name=enddate, required=true, example=结束日期, 例:2016-12-07}, {name=usergroupsql, required=true, example=用户组sql，如果没有用户组筛选，就传空字符串}, {name=iscache, required=false, example=是否需要缓存, 1为是，0为不缓存，默认1}]",
        "reportname": "retention_dau_dau_byds",
        "datasource": "presto",
        "column": "[ds, init, retention1, retention2, retention3, retention4, retention5, retention6, retention7, retention14, retention30]",
        "name": "[日期, 初始人数, 1日后, 2日后, 3日后, 4日后, 5日后, 6日后, 7日后, 14日后, 30日后]",
        "key": "ds",
        "desc": "活跃活跃日留存"
    },
    {
        "args": "[{name=appid, required=true, example=app unique key, 32字符, 例:37a4c0f4cc0810ccd34c61edb409c6e4}, {name=startdate, required=true, example=起始日期, 例:2016-12-01}, {name=enddate, required=true, example=结束日期, 例:2016-12-07}, {name=campaignid, required=false, example=推广活动unique key, 32位, 例：37a4c0f4cc0810ccd34c61edb409c6e4}, {name=iscache, required=false, example=是否需要缓存, 1为是，0为不缓存，默认1}]",
        "reportname": "campaigninfo_h5_bydatecampaign",
        "datasource": "mysql",
        "column": "[ds, campaignid, num_click, num_dis_ip, num_register, rate_reged_h5, num_loggin, num_pv, num_uv, num_finishload, num_finishload_uv, num_download, num_order, num_amout, num_payers]",
        "name": "[日期, 推广活动, 点击总数, 排重点击IP数, 注册总数, 注册率, 登陆总数, PV, UV, 页面加载完成数, 页面加载完成UV, 下载总数, 订单总数, 付费总金额, 付费总人数]",
        "key": "campaignid",
        "desc": "来源分析>>推广活动详情>>推广活动>>H5监测数据"
    },
    {
        "args": "[{name=appid, required=true, example=app unique key, 32字符, 例:37a4c0f4cc0810ccd34c61edb409c6e4}, {name=startdate, required=true, example=起始日期, 例:2016-12-01}, {name=enddate, required=true, example=结束日期, 例:2016-12-07}, {name=usergroupsql, required=true, example=用户组sql，如果没有用户组筛选，就传空字符串}, {name=iscache, required=false, example=是否需要缓存, 1为是，0为不缓存，默认1}]",
        "reportname": "retention_install_dau_byds",
        "datasource": "presto",
        "column": "[ds, init, retention1, retention2, retention3, retention4, retention5, retention6, retention7, retention14, retention30]",
        "name": "[日期, 初始人数, 1日后, 2日后, 3日后, 4日后, 5日后, 6日后, 7日后, 14日后, 30日后]",
        "key": "ds",
        "desc": "新增活跃日留存"
    },
    {
        "args": "[{name=appid, required=true, example=app unique key, 32字符, 例:37a4c0f4cc0810ccd34c61edb409c6e4}, {name=startdate, required=true, example=起始日期, 例:2016-12-01}, {name=enddate, required=true, example=结束日期, 例:2016-12-07}, {name=iscache, required=false, example=是否需要缓存, 1为是，0为不缓存，默认1}]",
        "reportname": "decision_potencial_bycategory",
        "datasource": "mysql",
        "column": "[num_potencial]",
        "name": "[用户数]",
        "key": "category_id",
        "desc": "决策支持>>潜在用户群>>潜在用户群分析"
    },
    {
        "args": "[{name=appid, required=true, example=app unique key, 32字符, 例:37a4c0f4cc0810ccd34c61edb409c6e4}, {name=startdate, required=true, example=起始日期, 例:2016-12-01}, {name=enddate, required=true, example=结束日期, 例:2016-12-07}, {name=iscache, required=false, example=是否需要缓存, 1为是，0为不缓存，默认1}]",
        "reportname": "channelinstall_top10_bychannel",
        "datasource": "mysql",
        "column": "[cid, num_install]",
        "name": "[渠道, 激活量]",
        "key": "cid",
        "desc": "仪表盘>>渠道激活top10"
    },
    {
        "args": "[{name=appid, required=true, example=app unique key, 32字符, 例:37a4c0f4cc0810ccd34c61edb409c6e4}, {name=startdate, required=true, example=起始日期, 例:2016-12-01}, {name=enddate, required=true, example=结束日期, 例:2016-12-07}, {name=iscache, required=false, example=是否需要缓存, 1为是，0为不缓存，默认1}]",
        "reportname": "device_bynetwork",
        "datasource": "mysql",
        "column": "[network, num_ins, dau, num_startup]",
        "name": "[网络类型, 激活设备, 活跃设备, 启动次数]",
        "key": "network",
        "desc": "决策支持>>设备分析>>网络列表"
    },
    {
        "args": "[{name=appid, required=true, example=app unique key, 32字符, 例:37a4c0f4cc0810ccd34c61edb409c6e4}, {name=startdate, required=true, example=起始日期, 例:2016-12-01}, {name=enddate, required=true, example=结束日期, 例:2016-12-07}, {name=dupnum_click_day, required=false, example=按天排重点击, 例：true}, {name=rate_install, required=false, example=激活率, 例：true}, {name=dupnum_reged_day, required=false, example=注册设备数, 例：true}, {name=dupnum_reged_mon, required=false, example=排重注册设备数, 例：true}, {name=rate_reged, required=false, example=注册率, 例：true}, {name=rate_retentiond1, required=false, example=D1留存, 例：true}, {name=rate_retentiond3, required=false, example=D3留存, 例：true}, {name=rate_retentiond7, required=false, example=D7留存, 例：true}, {name=rate_retentiond30, required=false, example=D30留存, 例：true}, {name=amt_ltv0, required=false, example=LTV0, 例：true}, {name=amt_ltv7, required=false, example=LTV7, 例：true}, {name=amt_ltv30, required=false, example=LTV30, 例：true}, {name=amt_income_region, required=false, example=区间付费, 例：true}, {name=amt_income_new_user, required=false, example=新增付费, 例：true}, {name=num_payer_new_user, required=false, example=新增付费设备, 例：true}, {name=amt_income_all_user, required=false, example=总付费, 例：true}, {name=num_payer_all_user, required=false, example=总付费设备, 例：true}, {name=num_click_fake, required=false, example=异常点击总数, 例：true}, {name=rate_click_fake, required=false, example=异常点击率, 例：true}, {name=num_install_fake, required=false, example=异常激活设备总数, 例：true}, {name=rate_install_fake, required=false, example=异常激活率, 例：true}, {name=cid, required=false, example=渠道id, 例：23}, {name=campaignid, required=false, example=推广活动unique key, 32位, 例：37a4c0f4cc0810ccd34c61edb409c6e4}, {name=iscache, required=false, example=是否需要缓存, 1为是，0为不缓存，默认1}]",
        "reportname": "campaigninfo_byds",
        "datasource": "mysql",
        "column": "[ds, num_click_total, num_click, dupnum_click_all, dupnum_click_day, num_install, rate_install, dupnum_reged_day, dupnum_reged_mon, rate_reged, rate_retentiond1, rate_retentiond3, rate_retentiond7, rate_retentiond30, amt_ltv0, amt_ltv7, amt_ltv30, amt_income_region, amt_income_new_user, num_payer_new_user, amt_income_all_user, num_payer_all_user, num_click_fake, rate_click_fake, num_install_fake, rate_install_fake]",
        "name": "[日期, 点击总数, 有效点击总数, 排重点击数, 按天排重点击数, 排重激活设备数, 激活率, 按天排重注册设备数, 排重注册设备数, 注册率, D1留存, D3留存, D7留存, D30留存, LTV0, LTV7, LTV30, 区间付费, 新增付费, 新增付费设备数, 总付费, 总付费设备数, 异常点击总数, 异常点击率, 异常激活设备数, 异常激活率]",
        "key": "ds",
        "desc": "来源分析>>推广活动详情>>日期"
    },
    {
        "args": "[{name=appid, required=true, example=app unique key, 32字符, 例:37a4c0f4cc0810ccd34c61edb409c6e4}, {name=startdate, required=true, example=起始日期, 例:2016-12-01}, {name=enddate, required=true, example=结束日期, 例:2016-12-07}, {name=cid, required=false, example=渠道id, 例：23}, {name=iscache, required=false, example=是否需要缓存, 1为是，0为不缓存，默认1}]",
        "reportname": "channelinfo_payer_top5_byds",
        "datasource": "mysql",
        "column": "[ds, num_payer_all_user]",
        "name": "[日期, 付费设备数]",
        "key": "ds",
        "desc": "来源分析>>渠道效果对比>>付费设备趋势TOP5"
    },
    {
        "args": "[{name=appid, required=true, example=app unique key, 32字符, 例:37a4c0f4cc0810ccd34c61edb409c6e4}, {name=startdate, required=true, example=起始日期, 例:2016-12-01}, {name=enddate, required=true, example=结束日期, 例:2016-12-07}, {name=cid, required=false, example=渠道id, 例：23}, {name=iscache, required=false, example=是否需要缓存, 1为是，0为不缓存，默认1}]",
        "reportname": "rate_channelinfo_install_top5_byhour",
        "datasource": "mysql",
        "column": "[hours, rate_install]",
        "name": "[小时, 激活率]",
        "key": "hours",
        "desc": "来源分析>>渠道效果对比>>点击趋势TOP5"
    },
    {
        "args": "[{name=appid, required=true, example=app unique key, 32字符, 例:37a4c0f4cc0810ccd34c61edb409c6e4}, {name=startdate, required=true, example=起始日期, 例:2016-12-01}, {name=enddate, required=true, example=结束日期, 例:2016-12-07}, {name=cid, required=false, example=渠道id, 例：23}, {name=iscache, required=false, example=是否需要缓存, 1为是，0为不缓存，默认1}]",
        "reportname": "channelinfo_install_top5_byds",
        "datasource": "mysql",
        "column": "[ds, num_install]",
        "name": "[日期, 激活量]",
        "key": "ds",
        "desc": "来源分析>>渠道效果对比>>激活趋势TOP5"
    },
    {
        "args": "[{name=appid, required=true, example=app unique key, 32字符, 例:37a4c0f4cc0810ccd34c61edb409c6e4}, {name=startdate, required=true, example=起始日期, 例:2016-12-01}, {name=enddate, required=true, example=结束日期, 例:2016-12-07}, {name=campaignid, required=true, example=推广活动unique key, 32位, 例：37a4c0f4cc0810ccd34c61edb409c6e4}, {name=creative, required=false, example=创意id, 例：23}, {name=iscache, required=false, example=是否需要缓存, 1为是，0为不缓存，默认1}, {name=orderby, required=false, example=排序字段}]",
        "reportname": "bd_bykwid_date",
        "datasource": "mysql",
        "column": "[ds, kwid, num_click_total, num_click, dupnum_click_all, num_ins, rate_install, dupnum_reg, amt_pay_new, num_pay_new]",
        "name": "[日期, 关键字, 点击总数, 有效点击总数, 子活动排重点击数, 排重激活设备数, 激活率, 排重注册设备数, 新增付费金额, 新增付费设备数]",
        "key": "kwid",
        "desc": "来源分析>>推广活动详情>>百度关键词按日期"
    },
    {
        "args": "[{name=appid, required=true, example=app unique key, 32字符, 例:37a4c0f4cc0810ccd34c61edb409c6e4}, {name=startdate, required=true, example=起始月1号, 例:2016-12-01}, {name=enddate, required=true, example=结束月1号, 例:2017-02-01}, {name=usergroupsql, required=true, example=用户组sql，如果没有用户组筛选，就传空字符串}, {name=iscache, required=false, example=是否需要缓存, 1为是，0为不缓存，默认1}]",
        "reportname": "retention_dau_dau_bymonth",
        "datasource": "presto",
        "column": "[ds, init, retention1, retention2, retention3]",
        "name": "[日期, 初始人数, 1月后, 2月后, 3月后]",
        "key": "",
        "desc": "活跃活跃月留存"
    },
    {
        "args": "[{name=appid, required=true, example=app unique key, 32字符, 例:37a4c0f4cc0810ccd34c61edb409c6e4}, {name=startdate, required=true, example=起始日期, 例:2016-12-01}, {name=enddate, required=true, example=结束日期, 例:2016-12-07}, {name=iscache, required=false, example=是否需要缓存, 1为是，0为不缓存，默认1}, {name=cid, required=false, example=渠道在业务系统中的自增id, 例:2}, {name=campaignid, required=false, example=推广活动 唯一键, 32位字符, 例:37a4c0f4cc0810ccd34c61edb409c6e4}]",
        "reportname": "realtime_click",
        "datasource": "mysql",
        "column": "[hours, click_tod, click_yes]",
        "name": "[小时, 今日, 昨日]",
        "key": "hours",
        "desc": "实时>>实时点击量"
    },
    {
        "args": "[{name=appid, required=true, example=app unique key, 32字符, 例:37a4c0f4cc0810ccd34c61edb409c6e4}, {name=startdate, required=true, example=起始日期, 例:2016-12-01}, {name=enddate, required=true, example=结束日期, 例:2016-12-07}, {name=iscache, required=false, example=是否需要缓存, 1为是，0为不缓存，默认1}, {name=campaignid, required=false, example=推广活动 唯一键, 32位字符, 例:37a4c0f4cc0810ccd34c61edb409c6e4}, {name=isnature, required=false, example=是否展现自然量数据, 1为是，0为不显示，默认1}]",
        "reportname": "income_byds",
        "datasource": "mysql",
        "column": "[ds, amt_income_cam, amt_income_def]",
        "name": "[日期, 推广量, 自然量]",
        "key": "ds",
        "desc": "仪表盘>>收入趋势（按天）"
    },
    {
        "args": "[{name=appid, required=true, example=app unique key, 32字符, 例:37a4c0f4cc0810ccd34c61edb409c6e4}, {name=install_startdate, required=true, example=激活起始日期, 例:2016-12-01}, {name=install_enddate, required=true, example=激活结束日期, 例:2016-12-07}, {name=pay_startdate, required=true, example=激活起始日期, 例:2016-12-01}, {name=pay_enddate, required=true, example=激活结束日期, 例:2016-12-07}, {name=campaignid, required=false, example=推广活动unique key, 32位, 例：37a4c0f4cc0810ccd34c61edb409c6e4}, {name=cid, required=false, example=渠道自增id}, {name=iscache, required=false, example=是否需要缓存, 1为是，0为不缓存，默认1}]",
        "reportname": "roi_byinterval",
        "datasource": "mysql",
        "column": "[ins_ds, pay_ds, amt_amount]",
        "name": "[日期, 付费日期, 付费金额]",
        "key": "ins_ds",
        "desc": "来源分析>>推广活动详情>>百度关键词"
    },
    {
        "args": "[{name=appid, required=true, example=app unique key, 32字符, 例:37a4c0f4cc0810ccd34c61edb409c6e4}, {name=startdate, required=true, example=起始日期, 例:2016-12-01}, {name=enddate, required=true, example=结束日期, 例:2016-12-07}, {name=iscache, required=false, example=是否需要缓存, 1为是，0为不缓存，默认1}]",
        "reportname": "decision_payment_byds",
        "datasource": "mysql",
        "column": "[num_pay, num_potential, num_not_pay]",
        "name": "[已付费, 潜在付费, 未付费]",
        "key": "ds",
        "desc": "决策支持>>付费洞察>>新用户付费趋势"
    },
    {
        "args": "[{name=appid, required=true, example=app unique key, 32字符, 例:37a4c0f4cc0810ccd34c61edb409c6e4}, {name=startdate, required=true, example=起始日期, 例:2016-12-01}, {name=enddate, required=true, example=结束日期, 例:2016-12-07}, {name=campaignid, required=true, example=推广活动unique key, 32位, 例：37a4c0f4cc0810ccd34c61edb409c6e4}, {name=creative, required=false, example=创意id, 例：23}, {name=iscache, required=false, example=是否需要缓存, 1为是，0为不缓存，默认1}, {name=orderby, required=false, example=排序字段}]",
        "reportname": "bd_bykwid",
        "datasource": "mysql",
        "column": "[number]",
        "name": "[关键字总数]",
        "key": "",
        "desc": "来源分析>>推广活动详情>>百度关键词"
    },
    {
        "args": "[{name=appid, required=true, example=app unique key, 32字符, 例:37a4c0f4cc0810ccd34c61edb409c6e4}]",
        "reportname": "sdk_debug_events_count",
        "datasource": "mysql",
        "column": "[appid, xwhat, num]",
        "name": "[APPKEY, 事件, 事件数量]",
        "key": "appid",
        "desc": "新建APP>>数据测试>>APP上报事件数"
    },
    {
        "args": "[{name=appid, required=true, example=app unique key, 32字符, 例:37a4c0f4cc0810ccd34c61edb409c6e4}, {name=startdate, required=true, example=起始日期, 例:2016-12-01}, {name=enddate, required=true, example=结束日期, 例:2016-12-07}, {name=cid, required=false, example=渠道id, 例：23}, {name=orderby, required=true, example=排序指标, 例:d1}, {name=iscache, required=false, example=是否需要缓存, 1为是，0为不缓存，默认1}]",
        "reportname": "rate_channelinfo_retention_top5_bychannel",
        "datasource": "mysql",
        "column": "[cid, rate_retentiond1, rate_retentiond3, rate_retentiond7]",
        "name": "[渠道, 次留, 三留, 七留]",
        "key": "cid",
        "desc": "来源分析>>渠道效果对比>>留存top5"
    },
    {
        "args": "[{name=appid, required=true, example=app unique key, 32字符, 例:37a4c0f4cc0810ccd34c61edb409c6e4}, {name=startdate, required=true, example=起始日期, 例:2016-12-01}, {name=enddate, required=true, example=结束日期, 例:2016-12-07}, {name=cid, required=false, example=渠道id, 例：23}, {name=iscache, required=false, example=是否需要缓存, 1为是，0为不缓存，默认1}]",
        "reportname": "channelinfo_amount_top5_byhour",
        "datasource": "mysql",
        "column": "[hours, amt_income_all_user]",
        "name": "[小时, 付费设备数]",
        "key": "hours",
        "desc": "来源分析>>渠道效果对比>>收入趋势TOP5"
    },
    {
        "args": "[{name=appid, required=true, example=app unique key, 32字符, 例:37a4c0f4cc0810ccd34c61edb409c6e4}, {name=startdate, required=true, example=起始日期, 例:2016-12-01}, {name=enddate, required=true, example=结束日期, 例:2016-12-07}, {name=iscache, required=false, example=是否需要缓存, 1为是，0为不缓存，默认1}, {name=campaignid, required=false, example=推广活动 唯一键, 32位字符, 例:37a4c0f4cc0810ccd34c61edb409c6e4}]",
        "reportname": "click_byds",
        "datasource": "mysql",
        "column": "[ds, num_click]",
        "name": "[日期, 点击量]",
        "key": "ds",
        "desc": "仪表盘>>点击量趋势（按天）"
    },
    {
        "args": "[{name=appid, required=true, example=app unique key, 32字符, 例:37a4c0f4cc0810ccd34c61edb409c6e4}, {name=install_startdate, required=true, example=激活起始日期, 例:2016-12-01}, {name=install_enddate, required=true, example=激活结束日期, 例:2016-12-07}, {name=pay_startdate, required=true, example=激活起始日期, 例:2016-12-01}, {name=pay_enddate, required=true, example=激活结束日期, 例:2016-12-07}, {name=isincome, required=false, example=是否展现自然量数据, 1为是，0为不显示，默认1}, {name=campaignid, required=true, example=推广活动unique key, 32位, 例：37a4c0f4cc0810ccd34c61edb409c6e4}, {name=cid, required=false, example=渠道自增id}, {name=iscache, required=false, example=是否需要缓存, 1为是，0为不缓存，默认1}]",
        "reportname": "roi_bycampaign",
        "datasource": "mysql",
        "column": "[campaignid, num_click, dupnum_click_day, dupnum_click_all, dupnum_reg, num_ins, num_pay, amt_amount, amt_arpu, amt_arppu, rate_pay]",
        "name": "[推广活动, 点击总数, 按天排重点击数, 排重点击数, 排重注册设备数, 排重激活设备数, 付费设备数, 注收比付费, arpu, arppu, 付费率]",
        "key": "campaignid",
        "desc": "来源分析>>推广活动详情>>百度关键词"
    }
]