#!/usr/bin/env python
# encoding: utf-8
uri = [




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