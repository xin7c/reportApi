var uri = [
    {
        "args": "[{name=appid, required=true, example=app unique key, 32字符, 例:37a4c0f4cc0810ccd34c61edb409c6e4}, {name=startdate, required=true, example=起始日期, 例:2016-12-01}, {name=enddate, required=true, example=结束日期, 例:2016-12-07}, {name=cid, required=false, example=渠道id, 例：23}, {name=iscache, required=false, example=是否需要缓存, 1为是，0为不缓存，默认1}]",
        "reportname": "channelinfo_install_top5_byhour",
        "datasource": "mysql",
        "column": "[hours, num_install]",
        "name": "[小时, 激活量]",
        "key": "hours",
        "desc": "来源分析>>渠道效果对比>>激活趋势TOP5"
    },
    {
        "args": "[{name=appid, required=true, example=app unique key, 32字符, 例:37a4c0f4cc0810ccd34c61edb409c6e4}, {name=startdate, required=true, example=起始日期, 例:2016-12-01}, {name=enddate, required=true, example=结束日期, 例:2016-12-07}, {name=iscache, required=false, example=是否需要缓存, 1为是，0为不缓存，默认1}, {name=cid, required=false, example=渠道在业务系统中的自增id, 例:2}, {name=campaignid, required=false, example=推广活动 唯一键, 32位字符, 例:37a4c0f4cc0810ccd34c61edb409c6e4}]",
        "reportname": "realtime_payer",
        "datasource": "mysql",
        "column": "[hours, payer_tod, payer_yes]",
        "name": "[小时, 今日, 昨日]",
        "key": "hours",
        "desc": "实时>>实时点击量"
    },
    {
        "args": "[{name=appid, required=true, example=app unique key, 32字符, 例:37a4c0f4cc0810ccd34c61edb409c6e4}, {name=startdate, required=true, example=起始日期, 例:2016-12-01}, {name=enddate, required=true, example=结束日期, 例:2016-12-07}, {name=iscache, required=false, example=是否需要缓存, 1为是，0为不缓存，默认1}, {name=campaignid, required=false, example=推广活动 唯一键, 32位字符, 例:37a4c0f4cc0810ccd34c61edb409c6e4}, {name=isnature, required=false, example=是否展现自然量数据, 1为是，0为不显示，默认1}]",
        "reportname": "install_byhour",
        "datasource": "mysql",
        "column": "[hours, num_install_cam, num_install_def]",
        "name": "[小时, 推广量, 自然量]",
        "key": "hours",
        "desc": "仪表盘>>激活量趋势（按小时）"
    },
    {
        "args": "[{name=appid, required=true, example=app unique key, 32字符, 例:37a4c0f4cc0810ccd34c61edb409c6e4}, {name=startdate, required=true, example=起始日期, 例:2016-12-01}, {name=enddate, required=true, example=结束日期, 例:2016-12-07}, {name=dupnum_click_day, required=false, example=按天排重点击, 例：true}, {name=rate_install, required=false, example=激活率, 例：true}, {name=dupnum_reged_day, required=false, example=按天排重注册设备数, 例：true}, {name=dupnum_reged_mon, required=false, example=排重注册设备数, 例：true}, {name=rate_reged, required=false, example=注册率, 例：true}, {name=rate_retentiond1, required=false, example=D1留存, 例：true}, {name=rate_retentiond3, required=false, example=D3留存, 例：true}, {name=rate_retentiond7, required=false, example=D7留存, 例：true}, {name=rate_retentiond30, required=false, example=D30留存, 例：true}, {name=amt_ltv0, required=false, example=LTV0, 例：true}, {name=amt_ltv7, required=false, example=LTV7, 例：true}, {name=amt_ltv30, required=false, example=LTV30, 例：true}, {name=amt_income_region, required=false, example=区间付费, 例：true}, {name=amt_income_new_user, required=false, example=新增付费, 例：true}, {name=num_payer_new_user, required=false, example=新增付费设备, 例：true}, {name=amt_income_all_user, required=false, example=总付费, 例：true}, {name=num_payer_all_user, required=false, example=总付费设备, 例：true}, {name=num_click_fake, required=false, example=异常点击总数, 例：true}, {name=rate_click_fake, required=false, example=异常点击率, 例：true}, {name=num_install_fake, required=false, example=异常激活设备总数, 例：true}, {name=rate_install_fake, required=false, example=异常激活率, 例：true}, {name=cid, required=false, example=渠道id, 例：23}, {name=campaignid, required=false, example=推广活动unique key, 32位, 例：37a4c0f4cc0810ccd34c61edb409c6e4}, {name=iscache, required=false, example=是否需要缓存, 1为是，0为不缓存，默认1}]",
        "reportname": "campaigninfo_bypackagecampaign",
        "datasource": "mysql",
        "column": "[campaignid, num_click_total, num_click, dupnum_click_all, dupnum_click_day, num_install, rate_install, dupnum_reged_day, dupnum_reged_mon, rate_reged, rate_retentiond1, rate_retentiond3, rate_retentiond7, rate_retentiond30, amt_ltv0, amt_ltv7, amt_ltv30, amt_income_region, amt_income_new_user, num_payer_new_user, amt_income_all_user, num_payer_all_user, num_click_fake, rate_click_fake, num_install_fake, rate_install_fake]",
        "name": "[推广活动, 点击总数, 有效点击总数, 排重点击数, 按天排重点击数, 排重激活设备数, 激活率, 按天排重注册设备数, 排重注册设备数, 注册率, D1留存, D3留存, D7留存, D30留存, LTV0, LTV7, LTV30, 区间付费, 新增付费, 新增付费设备数, 总付费, 总付费设备数, 异常点击总数, 异常点击率, 异常激活设备数, 异常激活率]",
        "key": "campaignid",
        "desc": "来源分析>>推广活动详情>>推广活动组"
    },
    {
        "args": "[{name=appid, required=true, example=app unique key, 32字符, 例:37a4c0f4cc0810ccd34c61edb409c6e4}, {name=startdate, required=true, example=起始日期, 例:2016-12-01}, {name=enddate, required=true, example=结束日期, 例:2016-12-07}, {name=parent_campaignid, required=false, example=推广活动unique key, 32位, 例：37a4c0f4cc0810ccd34c61edb409c6e4}, {name=campaignid, required=false, example=推广子活动unique key, 32位, 例：37a4c0f4cc0810ccd34c61edb409c6e4}, {name=iscache, required=false, example=是否需要缓存, 1为是，0为不缓存，默认1}]",
        "reportname": "campaigninfo_bysubpackagecampaign",
        "datasource": "mysql",
        "column": "[campaignid, num_click_total, num_click, dupnum_click_all, num_install, rate_install]",
        "name": "[推广活动, 点击总数, 有效点击总数, 排重点击数, 排重激活设备数, 激活率]",
        "key": "campaignid",
        "desc": "来源分析>>推广活动详情>>推广活动组"
    },
    {
        "args": "[{name=appid, required=true, example=app unique key, 32字符, 例:37a4c0f4cc0810ccd34c61edb409c6e4}, {name=install_startdate, required=true, example=激活起始日期, 例:2016-12-01}, {name=install_enddate, required=true, example=激活结束日期, 例:2016-12-07}, {name=pay_startdate, required=true, example=激活起始日期, 例:2016-12-01}, {name=pay_enddate, required=true, example=激活结束日期, 例:2016-12-07}, {name=isincome, required=false, example=是否展现自然量数据, 1为是，0为不显示，默认1}, {name=campaignid, required=false, example=推广活动unique key, 32位, 例：37a4c0f4cc0810ccd34c61edb409c6e4}, {name=cid, required=false, example=渠道自增id}, {name=iscache, required=false, example=是否需要缓存, 1为是，0为不缓存，默认1}]",
        "reportname": "roi_bychannel",
        "datasource": "mysql",
        "column": "[cid, num_click, dupnum_click_day, dupnum_click_all, dupnum_reg, num_ins, num_pay, amt_amount, amt_arpu, amt_arppu, rate_pay]",
        "name": "[渠道, 点击总数, 按天排重点击数, 排重点击数, 排重注册设备数, 排重激活设备数, 付费设备数, 注收比付费, arpu, arppu, 付费率]",
        "key": "cid",
        "desc": "来源分析>>推广活动详情>>百度关键词"
    },
    {
        "args": "[{name=appid, required=true, example=app unique key, 32字符, 例:37a4c0f4cc0810ccd34c61edb409c6e4}, {name=startdate, required=true, example=起始日期, 例:2016-12-01}, {name=enddate, required=true, example=结束日期, 例:2016-12-07}, {name=orderby, required=true, example=排序指标, 例:click}, {name=iscache, required=false, example=是否需要缓存, 1为是，0为不缓存，默认1}, {name=cid, required=false, example=渠道id, 例：23}, {name=isincome, required=false, example=是否展现自然量数据, 1为是，0为不显示，默认1}]",
        "reportname": "channelinfo_base_top5_bychannel",
        "datasource": "mysql",
        "column": "[cid, num_click, num_install, amt_income_all_user]",
        "name": "[渠道, 点击量, 激活量, 收入]",
        "key": "cid",
        "desc": "来源分析>>渠道效果对比>>基础数据top5（有实时）"
    },
    {
        "args": "[{name=appid, required=true, example=app unique key, 32字符, 例:37a4c0f4cc0810ccd34c61edb409c6e4}, {name=startdate, required=true, example=起始日期, 例:2016-12-01}, {name=enddate, required=true, example=结束日期, 例:2016-12-07}, {name=iscache, required=false, example=是否需要缓存, 1为是，0为不缓存，默认1}]",
        "reportname": "channelincome_top10_bychannel",
        "datasource": "mysql",
        "column": "[cid, amt_income]",
        "name": "[渠道, 收入]",
        "key": "cid",
        "desc": "仪表盘>>渠道收入top10"
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
        "args": "[{name=appid, required=true, example=app unique key, 32字符, 例:37a4c0f4cc0810ccd34c61edb409c6e4}, {name=startdate, required=true, example=起始日期, 例:2016-12-01}, {name=enddate, required=true, example=结束日期, 例:2016-12-07}, {name=iscache, required=false, example=是否需要缓存, 1为是，0为不缓存，默认1}, {name=cid, required=false, example=渠道在业务系统中的自增id, 例:2}, {name=campaignid, required=false, example=推广活动 唯一键, 32位字符, 例:37a4c0f4cc0810ccd34c61edb409c6e4}]",
        "reportname": "realtime_dau",
        "datasource": "mysql",
        "column": "[hours, dau_tod, dau_yes]",
        "name": "[小时, 今日, 昨日]",
        "key": "hours",
        "desc": "实时>>实时点击量"
    },
    {
        "args": "[{name=appid, required=true, example=app unique key, 32字符, 例:37a4c0f4cc0810ccd34c61edb409c6e4}, {name=startdate, required=true, example=起始日期, 例:2016-12-01}, {name=enddate, required=true, example=结束日期, 例:2016-12-07}, {name=iscache, required=false, example=是否需要缓存, 1为是，0为不缓存，默认1}, {name=cid, required=false, example=渠道在业务系统中的自增id, 例:2}, {name=campaignid, required=false, example=推广活动 唯一键, 32位字符, 例:37a4c0f4cc0810ccd34c61edb409c6e4}]",
        "reportname": "realtime_dupclick",
        "datasource": "mysql",
        "column": "[hours, dupclick_tod, dupclick_yes]",
        "name": "[小时, 今日, 昨日]",
        "key": "hours",
        "desc": "实时>>实时点击量"
    },
    {
        "args": "[{name=appid, required=true, example=app unique key, 32字符, 例:37a4c0f4cc0810ccd34c61edb409c6e4}, {name=startdate, required=true, example=起始周第一天, 例:2016-12-01}, {name=enddate, required=true, example=结束周第一天, 例:2016-12-07}, {name=usergroupsql, required=true, example=用户组sql，如果没有用户组筛选，就传空字符串}, {name=iscache, required=false, example=是否需要缓存, 1为是，0为不缓存，默认1}]",
        "reportname": "retention_install_dau_byweek",
        "datasource": "presto",
        "column": "[ds, init, retention1, retention2, retention3, retention4, retention5, retention6, retention7, retention8]",
        "name": "[日期, 初始人数, 1周后, 2周后, 3周后, 4周后, 5周后, 6周后, 7周后, 8周后]",
        "key": "",
        "desc": "新增活跃日留存"
    },
    {
        "args": "[{name=appid, required=true, example=app unique key, 32字符, 例:37a4c0f4cc0810ccd34c61edb409c6e4}, {name=startdate, required=true, example=起始日期, 例:2016-12-01}, {name=enddate, required=true, example=结束日期, 例:2016-12-07}, {name=campaignid, required=true, example=推广活动unique key, 32位, 例：37a4c0f4cc0810ccd34c61edb409c6e4}, {name=iscache, required=false, example=是否需要缓存, 1为是，0为不缓存，默认1}]",
        "reportname": "bd_bycampaign",
        "datasource": "mysql",
        "column": "[campaignid, num_click_total, num_click, dupnum_click_all, num_ins, rate_install, dupnum_reg, amt_pay_new, num_pay_new]",
        "name": "[推广活动, 点击总数, 有效点击总数, 子活动排重点击数, 排重激活设备数, 激活率, 排重注册设备数, 新增付费金额, 新增付费设备数]",
        "key": "campaignid",
        "desc": "来源分析>>推广活动详情>>百度关键词"
    },
    {
        "args": "[{name=appid, required=true, example=app unique key, 32字符, 例:37a4c0f4cc0810ccd34c61edb409c6e4}, {name=install_startdate, required=true, example=激活起始日期, 例:2016-12-01}, {name=install_enddate, required=true, example=激活结束日期, 例:2016-12-07}, {name=pay_startdate, required=true, example=激活起始日期, 例:2016-12-01}, {name=pay_enddate, required=true, example=激活结束日期, 例:2016-12-07}, {name=campaignid, required=false, example=推广活动unique key, 32位, 例：37a4c0f4cc0810ccd34c61edb409c6e4}, {name=cid, required=false, example=渠道自增id}, {name=iscache, required=false, example=是否需要缓存, 1为是，0为不缓存，默认1}]",
        "reportname": "roi_byds",
        "datasource": "mysql",
        "column": "[ds, pay_ds, num_ins, num_pay, amt_pay]",
        "name": "[日期, 付费日期, 排重激活设备数, 新增用户付费人数, 新增用户付费金额]",
        "key": "ds",
        "desc": "来源分析>>推广活动详情>>百度关键词"
    },
    {
        "args": "[{name=appid, required=true, example=app unique key, 32字符, 例:37a4c0f4cc0810ccd34c61edb409c6e4}, {name=startdate, required=true, example=起始日期, 例:2016-12-01}, {name=enddate, required=true, example=结束日期, 例:2016-12-07}, {name=iscache, required=false, example=是否需要缓存, 1为是，0为不缓存，默认1}, {name=campaignid, required=false, example=推广活动 唯一键, 32位字符, 例:37a4c0f4cc0810ccd34c61edb409c6e4}, {name=isnature, required=false, example=是否展现自然量数据, 1为是，0为不显示，默认1}]",
        "reportname": "reged_byds",
        "datasource": "mysql",
        "column": "[ds, num_reged_cam, num_reged_def]",
        "name": "[日期, 推广量, 自然量]",
        "key": "ds",
        "desc": "仪表盘>>注册量趋势（按天）"
    },
    {
        "args": "[{name=appid, required=true, example=app unique key, 32字符, 例:37a4c0f4cc0810ccd34c61edb409c6e4}, {name=startdate, required=true, example=起始日期, 例:2016-12-01}, {name=enddate, required=true, example=结束日期, 例:2016-12-07}, {name=iscache, required=false, example=是否需要缓存, 1为是，0为不缓存，默认1}, {name=cid, required=false, example=渠道在业务系统中的自增id, 例:2}, {name=campaignid, required=false, example=推广活动 唯一键, 32位字符, 例:37a4c0f4cc0810ccd34c61edb409c6e4}]",
        "reportname": "realtime_income",
        "datasource": "mysql",
        "column": "[hours, amt_income_tod, amt_income_yes]",
        "name": "[小时, 今日, 昨日]",
        "key": "hours",
        "desc": "实时>>实时点击量"
    },
    {
        "args": "[{name=appid, required=true, example=app unique key, 32字符, 例:37a4c0f4cc0810ccd34c61edb409c6e4}, {name=startdate, required=true, example=起始日期, 例:2016-12-01}, {name=enddate, required=true, example=结束日期, 例:2016-12-07}, {name=cid, required=false, example=渠道id, 例：23}, {name=iscache, required=false, example=是否需要缓存, 1为是，0为不缓存，默认1}]",
        "reportname": "channelinfo_click_top5_byds",
        "datasource": "mysql",
        "column": "[ds, num_click]",
        "name": "[日期, 点击量]",
        "key": "ds",
        "desc": "来源分析>>渠道效果对比>>点击趋势TOP5"
    },
    {
        "args": "[{name=appid, required=true, example=app unique key, 32字符, 例:37a4c0f4cc0810ccd34c61edb409c6e4}, {name=startdate, required=true, example=起始日期, 例:2016-12-01}, {name=enddate, required=true, example=结束日期, 例:2016-12-07}, {name=campaignid, required=true, example=推广活动unique key, 32位, 例：37a4c0f4cc0810ccd34c61edb409c6e4}, {name=kwid, required=false, example=关键词id, 例：23}, {name=iscache, required=false, example=是否需要缓存, 1为是，0为不缓存，默认1}]",
        "reportname": "bd_bycreative",
        "datasource": "mysql",
        "column": "[number]",
        "name": "[创意总数]",
        "key": "",
        "desc": "来源分析>>推广活动详情>>百度关键词"
    },
    {
        "args": "[{name=appid, required=true, example=app unique key, 32字符, 例:37a4c0f4cc0810ccd34c61edb409c6e4}, {name=startdate, required=true, example=起始日期, 例:2016-12-01}, {name=enddate, required=true, example=结束日期, 例:2016-12-07}, {name=dupnum_click_day, required=false, example=按天排重点击数, 例：true}, {name=rate_install, required=false, example=激活率, 例：true}, {name=dupnum_reged_day, required=false, example=按天排重注册设备数, 例：true}, {name=dupnum_reged_mon, required=false, example=排重注册设备数, 例：true}, {name=rate_reged, required=false, example=注册率, 例：true}, {name=rate_retentiond1, required=false, example=D1留存, 例：true}, {name=rate_retentiond3, required=false, example=D3留存, 例：true}, {name=rate_retentiond7, required=false, example=D7留存, 例：true}, {name=rate_retentiond30, required=false, example=D30留存, 例：true}, {name=amt_ltv0, required=false, example=LTV0, 例：true}, {name=amt_ltv7, required=false, example=LTV7, 例：true}, {name=amt_ltv30, required=false, example=LTV30, 例：true}, {name=amt_income_region, required=false, example=区间付费, 例：true}, {name=amt_income_new_user, required=false, example=新增付费, 例：true}, {name=num_payer_new_user, required=false, example=新增付费设备数, 例：true}, {name=amt_income_all_user, required=false, example=总付费, 例：true}, {name=num_payer_all_user, required=false, example=总付费设备数, 例：true}, {name=num_click_fake, required=false, example=异常点击总数, 例：true}, {name=rate_click_fake, required=false, example=异常点击率, 例：true}, {name=num_install_fake, required=false, example=异常激活设备数, 例：true}, {name=rate_install_fake, required=false, example=异常激活率, 例：true}, {name=cid, required=false, example=渠道id, 例：23}, {name=campaignid, required=false, example=推广活动unique key, 32位, 例：37a4c0f4cc0810ccd34c61edb409c6e4}, {name=iscache, required=false, example=是否需要缓存, 1为是，0为不缓存，默认1}]",
        "reportname": "campaigninfo_bydatecampaign",
        "datasource": "mysql",
        "column": "[ds, campaignid, num_click, dupnum_click_all, dupnum_click_day, num_install, rate_install, dupnum_reged_day, dupnum_reged_mon, rate_reged, rate_retentiond1, rate_retentiond3, rate_retentiond7, rate_retentiond30, amt_ltv0, amt_ltv7, amt_ltv30, amt_income_region, amt_income_new_user, num_payer_new_user, amt_income_all_user, num_payer_all_user, num_click_fake, rate_click_fake, num_install_fake, rate_install_fake]",
        "name": "[日期, 推广活动, 点击总数, 排重点击数, 按天排重点击, 排重激活设备数, 激活率, 按天排重注册设备数, 排重注册设备数, 注册率, D1留存, D3留存, D7留存, D30留存, LTV0, LTV7, LTV30, 区间付费, 新增付费, 新增付费设备, 总付费, 总付费设备, 异常点击总数, 异常点击率, 异常激活设备总数, 异常激活率]",
        "key": "campaignid",
        "desc": "来源分析>>推广活动详情>>推广活动按日期分组"
    },
    {
        "args": "[{name=appid, required=true, example=app unique key, 32字符, 例:37a4c0f4cc0810ccd34c61edb409c6e4}, {name=startdate, required=true, example=起始日期, 例:2016-12-01}, {name=enddate, required=true, example=结束日期, 例:2016-12-07}, {name=iscache, required=false, example=是否需要缓存, 1为是，0为不缓存，默认1}]",
        "reportname": "device_byresolution",
        "datasource": "mysql",
        "column": "[screen, num_ins, dau, num_startup]",
        "name": "[分辨率, 激活设备, 活跃设备, 启动次数]",
        "key": "screen",
        "desc": "决策支持>>设备分析>>分辨率列表"
    },
    {
        "args": "[{name=appid, required=true, example=app unique key, 32字符, 例:37a4c0f4cc0810ccd34c61edb409c6e4}, {name=startdate, required=true, example=起始日期, 例:2016-12-01}, {name=enddate, required=true, example=结束日期, 例:2016-12-07}, {name=cid, required=false, example=渠道id, 例：23}, {name=iscache, required=false, example=是否需要缓存, 1为是，0为不缓存，默认1}]",
        "reportname": "channelinfo_reged_top5_byhour",
        "datasource": "mysql",
        "column": "[hours, dupnum_reged_day]",
        "name": "[小时, 注册量]",
        "key": "hours",
        "desc": "来源分析>>渠道效果对比>>注册趋势TOP5"
    },
    {
        "args": "[{name=appid, required=true, example=app unique key, 32字符, 例:37a4c0f4cc0810ccd34c61edb409c6e4}, {name=startdate, required=true, example=起始日期, 例:2016-12-01}, {name=enddate, required=true, example=结束日期, 例:2016-12-07}, {name=dupnum_click_day, required=false, example=按天排重点击, 例：true}, {name=rate_install, required=false, example=激活率, 例：true}, {name=dupnum_reged_day, required=false, example=按天排重注册设备数, 例：true}, {name=dupnum_reged_mon, required=false, example=排重注册设备数, 例：true}, {name=rate_reged, required=false, example=注册率, 例：true}, {name=rate_retentiond1, required=false, example=D1留存, 例：true}, {name=rate_retentiond3, required=false, example=D3留存, 例：true}, {name=rate_retentiond7, required=false, example=D7留存, 例：true}, {name=rate_retentiond30, required=false, example=D30留存, 例：true}, {name=amt_ltv0, required=false, example=LTV0, 例：true}, {name=amt_ltv7, required=false, example=LTV7, 例：true}, {name=amt_ltv30, required=false, example=LTV30, 例：true}, {name=amt_income_region, required=false, example=区间付费, 例：true}, {name=amt_income_new_user, required=false, example=新增付费, 例：true}, {name=num_payer_new_user, required=false, example=新增付费设备, 例：true}, {name=amt_income_all_user, required=false, example=总付费, 例：true}, {name=num_payer_all_user, required=false, example=总付费设备, 例：true}, {name=num_click_fake, required=false, example=异常点击总数, 例：true}, {name=rate_click_fake, required=false, example=异常点击率, 例：true}, {name=num_install_fake, required=false, example=异常激活设备总数, 例：true}, {name=rate_install_fake, required=false, example=异常激活率, 例：true}, {name=cid, required=false, example=渠道id, 例：23}, {name=campaignid, required=false, example=推广活动unique key, 32位, 例：37a4c0f4cc0810ccd34c61edb409c6e4}, {name=iscache, required=false, example=是否需要缓存, 1为是，0为不缓存，默认1}]",
        "reportname": "campaigninfo_bycampgroup",
        "datasource": "mysql",
        "column": "[campaignid, num_click_total, num_click, dupnum_click_all, dupnum_click_day, num_install, rate_install, dupnum_reged_day, dupnum_reged_mon, rate_reged, rate_retentiond1, rate_retentiond3, rate_retentiond7, rate_retentiond30, amt_ltv0, amt_ltv7, amt_ltv30, amt_income_region, amt_income_new_user, num_payer_new_user, amt_income_all_user, num_payer_all_user, num_click_fake, rate_click_fake, num_install_fake, rate_install_fake]",
        "name": "[推广活动, 点击总数, 有效点击总数, 排重点击数, 按天排重点击数, 排重激活设备数, 激活率, 按天排重注册设备数, 排重注册设备数, 注册率, D1留存, D3留存, D7留存, D30留存, LTV0, LTV7, LTV30, 区间付费, 新增付费, 新增付费设备数, 总付费, 总付费设备数, 异常点击总数, 异常点击率, 异常激活设备数, 异常激活率]",
        "key": "campaignid",
        "desc": "来源分析>>推广活动详情>>推广活动组"
    },
    {
        "args": "[{name=appid, required=true, example=app unique key, 32字符, 例:37a4c0f4cc0810ccd34c61edb409c6e4}, {name=startdate, required=true, example=起始日期, 例:2016-12-01}, {name=enddate, required=true, example=结束日期, 例:2016-12-07}, {name=iscache, required=false, example=是否需要缓存, 1为是，0为不缓存，默认1}]",
        "reportname": "dau_byhour",
        "datasource": "mysql",
        "column": "[hours, dau]",
        "name": "[小时, DAU]",
        "key": "hours",
        "desc": "仪表盘>>DAU趋势（按小时）"
    },
    {
        "args": "[{name=appid, required=true, example=app unique key, 32字符, 例:37a4c0f4cc0810ccd34c61edb409c6e4}, {name=startdate, required=true, example=起始日期, 例:2016-12-01}, {name=enddate, required=true, example=结束日期, 例:2016-12-07}, {name=dupnum_click_day, required=false, example=按天排重点击, 例：true}, {name=rate_install, required=false, example=激活率, 例：true}, {name=dupnum_reged_day, required=false, example=按天排重注册设备数, 例：true}, {name=dupnum_reged_mon, required=false, example=排重注册设备数, 例：true}, {name=rate_reged, required=false, example=注册率, 例：true}, {name=rate_retentiond1, required=false, example=D1留存, 例：true}, {name=rate_retentiond3, required=false, example=D3留存, 例：true}, {name=rate_retentiond7, required=false, example=D7留存, 例：true}, {name=rate_retentiond30, required=false, example=D30留存, 例：true}, {name=amt_ltv0, required=false, example=LTV0, 例：true}, {name=amt_ltv7, required=false, example=LTV7, 例：true}, {name=amt_ltv30, required=false, example=LTV30, 例：true}, {name=amt_income_region, required=false, example=区间付费, 例：true}, {name=amt_income_new_user, required=false, example=新增付费, 例：true}, {name=num_payer_new_user, required=false, example=新增付费设备, 例：true}, {name=amt_income_all_user, required=false, example=总付费, 例：true}, {name=num_payer_all_user, required=false, example=总付费设备, 例：true}, {name=num_click_fake, required=false, example=异常点击总数, 例：true}, {name=rate_click_fake, required=false, example=异常点击率, 例：true}, {name=num_install_fake, required=false, example=异常激活设备总数, 例：true}, {name=rate_install_fake, required=false, example=异常激活率, 例：true}, {name=campaignid, required=true, example=推广活动unique key, 32位, 例：37a4c0f4cc0810ccd34c61edb409c6e4}, {name=cid, required=false, example=渠道id, 例：23}, {name=iscache, required=false, example=是否需要缓存, 1为是，0为不缓存，默认1}]",
        "reportname": "campaigninfo_bychannel",
        "datasource": "mysql",
        "column": "[cid, num_click_total, num_click, dupnum_click_all, dupnum_click_day, num_install, rate_install, dupnum_reged_day, dupnum_reged_mon, rate_reged, rate_retentiond1, rate_retentiond3, rate_retentiond7, rate_retentiond30, amt_ltv0, amt_ltv7, amt_ltv30, amt_income_region, amt_income_new_user, num_payer_new_user, amt_income_all_user, num_payer_all_user, num_click_fake, rate_click_fake, num_install_fake, rate_install_fake]",
        "name": "[渠道, 点击总数, 有效点击总数, 排重点击数, 按天排重点击数, 排重激活设备数, 激活率, 按天排重注册设备数, 排重注册设备数, 注册率, D1留存, D3留存, D7留存, D30留存, LTV0, LTV7, LTV30, 区间付费, 新增付费, 新增付费设备数, 总付费, 总付费设备数, 异常点击总数, 异常点击率, 异常激活设备数, 异常激活率]",
        "key": "cid",
        "desc": "来源分析>>推广活动详情>>推广活动"
    },
    {
        "args": "[{name=appid, required=true, example=app unique key, 32字符, 例:37a4c0f4cc0810ccd34c61edb409c6e4}, {name=startdate, required=true, example=起始日期, 例:2016-12-01}, {name=enddate, required=true, example=结束日期, 例:2016-12-07}, {name=iscache, required=false, example=是否需要缓存, 1为是，0为不缓存，默认1}, {name=campaignid, required=false, example=推广活动 唯一键, 32位字符, 例:37a4c0f4cc0810ccd34c61edb409c6e4}, {name=isnature, required=false, example=是否展现自然量数据, 1为是，0为不显示，默认1}]",
        "reportname": "install_byds",
        "datasource": "mysql",
        "column": "[ds, num_install_cam, num_install_def]",
        "name": "[日期, 推广量, 自然量]",
        "key": "ds",
        "desc": "仪表盘>>激活量趋势（按天）"
    },
    {
        "args": "[{name=appid, required=true, example=app unique key, 32字符, 例:37a4c0f4cc0810ccd34c61edb409c6e4}, {name=startdate, required=true, example=起始日期, 例:2016-12-01}, {name=enddate, required=true, example=结束日期, 例:2016-12-07}, {name=iscache, required=false, example=是否需要缓存, 1为是，0为不缓存，默认1}, {name=cid, required=false, example=渠道id, 例：23}, {name=isincome, required=false, example=是否展现自然量数据, 1为是，0为不显示，默认1}]",
        "reportname": "channelinfo_bychannel",
        "datasource": "mysql",
        "column": "[cid, num_click, num_install, dupnum_reged_day, amt_income_all_user, num_payer_all_user]",
        "name": "[渠道, 点击总数, 激活设备数, 注册设备数, 收入, 付费设备数]",
        "key": "cid",
        "desc": "来源分析>>渠道效果对比>>渠道详情"
    },
    {
        "args": "[{name=appid, required=true, example=app unique key, 32字符, 例:37a4c0f4cc0810ccd34c61edb409c6e4}, {name=startdate, required=true, example=起始周第一天, 例:2016-12-01}, {name=enddate, required=true, example=结束周第一天, 例:2016-12-07}, {name=usergroupsql, required=true, example=用户组sql，如果没有用户组筛选，就传空字符串}, {name=iscache, required=false, example=是否需要缓存, 1为是，0为不缓存，默认1}]",
        "reportname": "retention_install_dau_byweek",
        "datasource": "presto",
        "column": "[ds, init, retention1, retention2, retention3, retention4, retention5, retention6, retention7, retention8]",
        "name": "[日期, 初始人数, 1周后, 2周后, 3周后, 4周后, 5周后, 6周后, 7周后, 8周后]",
        "key": "",
        "desc": "新增活跃日留存"
    },
    {
        "args": "[{name=appid, required=true, example=app unique key, 32字符, 例:37a4c0f4cc0810ccd34c61edb409c6e4}, {name=startdate, required=true, example=起始日期, 例:2016-12-01}, {name=enddate, required=true, example=结束日期, 例:2016-12-07}, {name=iscache, required=false, example=是否需要缓存, 1为是，0为不缓存，默认1}, {name=cid, required=false, example=渠道在业务系统中的自增id, 例:2}, {name=campaignid, required=false, example=推广活动 唯一键, 32位字符, 例:37a4c0f4cc0810ccd34c61edb409c6e4}]",
        "reportname": "realtime_install",
        "datasource": "mysql",
        "column": "[hours, install_tod, install_yes]",
        "name": "[小时, 今日, 昨日]",
        "key": "hours",
        "desc": "实时>>实时点击量"
    },
    {
        "args": "[{name=appid, required=true, example=app unique key, 32字符, 例:37a4c0f4cc0810ccd34c61edb409c6e4}, {name=startdate, required=true, example=起始日期, 例:2016-12-01}, {name=enddate, required=true, example=结束日期, 例:2016-12-07}, {name=iscache, required=false, example=是否需要缓存, 1为是，0为不缓存，默认1}]",
        "reportname": "decision_payment_level_byds",
        "datasource": "mysql",
        "column": "[num_level_3, num_level_2, num_level_1]",
        "name": "[198元以上, 198元以下, 6元以下]",
        "key": "ds",
        "desc": "决策支持>>付费洞察>>新用户已付费情况"
    },
    {
        "args": "[{name=appid, required=true, example=app unique key, 32字符, 例:37a4c0f4cc0810ccd34c61edb409c6e4}, {name=startdate, required=true, example=起始日期, 例:2016-12-01}, {name=enddate, required=true, example=结束日期, 例:2016-12-07}, {name=iscache, required=false, example=是否需要缓存, 1为是，0为不缓存，默认1}, {name=campaignid, required=false, example=推广活动 唯一键, 32位字符, 例:37a4c0f4cc0810ccd34c61edb409c6e4}]",
        "reportname": "rate_install_byds",
        "datasource": "mysql",
        "column": "[ds, rate_install, rate_std]",
        "name": "[日期, 激活率, 行业中位数]",
        "key": "ds",
        "desc": "仪表盘>>激活率趋势（按天）"
    },
    {
        "args": "[{name=appid, required=true, example=app unique key, 32字符, 例:37a4c0f4cc0810ccd34c61edb409c6e4}, {name=startdate, required=true, example=起始日期, 例:2016-12-01}, {name=enddate, required=true, example=结束日期, 例:2016-12-07}, {name=iscache, required=false, example=是否需要缓存, 1为是，0为不缓存，默认1}, {name=campaignid, required=false, example=推广活动 唯一键, 32位字符, 例:37a4c0f4cc0810ccd34c61edb409c6e4}]",
        "reportname": "rate_install_byhour",
        "datasource": "mysql",
        "column": "[hours, rate_install, rate_std]",
        "name": "[小时, 激活率, 行业中位数]",
        "key": "hours",
        "desc": "仪表盘>>激活率趋势（按小时）"
    },
    {
        "args": "[{name=appid, required=true, example=app unique key, 32字符, 例:37a4c0f4cc0810ccd34c61edb409c6e4}, {name=startdate, required=true, example=起始日期, 例:2016-12-01}, {name=enddate, required=true, example=结束日期, 例:2016-12-07}, {name=iscache, required=false, example=是否需要缓存, 1为是，0为不缓存，默认1}, {name=ismanufacturer, required=false, example=1是品牌，0为设备型号}]",
        "reportname": "device_bymodel",
        "datasource": "mysql",
        "column": "[model, num_ins, dau, num_startup]",
        "name": "[设备型号, 激活设备, 活跃设备, 启动次数]",
        "key": "model",
        "desc": "决策支持>>设备分析>>型号列表"
    },
    {
        "args": "[{name=appid, required=true, example=app unique key, 32字符, 例:37a4c0f4cc0810ccd34c61edb409c6e4}, {name=startdate, required=true, example=起始日期, 例:2016-12-01}, {name=enddate, required=true, example=结束日期, 例:2016-12-07}, {name=iscache, required=false, example=是否需要缓存, 1为是，0为不缓存，默认1}]",
        "reportname": "device_byos",
        "datasource": "mysql",
        "column": "[os_v, num_ins, dau, num_startup]",
        "name": "[系统版本, 激活设备, 活跃设备, 启动次数]",
        "key": "os_v",
        "desc": "决策支持>>设备分析>>系统列表"
    },
    {
        "args": "[{name=appid, required=true, example=app unique key, 32字符, 例:37a4c0f4cc0810ccd34c61edb409c6e4}, {name=startdate, required=true, example=起始日期, 例:2016-12-01}, {name=enddate, required=true, example=结束日期, 例:2016-12-07}, {name=campaignid, required=true, example=推广活动unique key, 32位, 例：37a4c0f4cc0810ccd34c61edb409c6e4}, {name=creative, required=false, example=创意id, 例：23}, {name=iscache, required=false, example=是否需要缓存, 1为是，0为不缓存，默认1}, {name=orderby, required=false, example=排序字段}]",
        "reportname": "bd_bykwid",
        "datasource": "mysql",
        "column": "[kwid, num_click_total, num_click, dupnum_click_all, num_ins, rate_install, dupnum_reg, amt_pay_new, num_pay_new]",
        "name": "[关键字, 点击总数, 有效点击总数, 子活动排重点击数, 排重激活设备数, 激活率, 排重注册设备数, 新增付费金额, 新增付费设备数]",
        "key": "kwid",
        "desc": "来源分析>>推广活动详情>>百度关键词"
    },
    {
        "args": "[{name=appid, required=true, example=app unique key, 32字符, 例:37a4c0f4cc0810ccd34c61edb409c6e4}, {name=startdate, required=true, example=起始日期, 例:2016-12-01}, {name=enddate, required=true, example=结束日期, 例:2016-12-07}, {name=iscache, required=false, example=是否需要缓存, 1为是，0为不缓存，默认1}, {name=campaignid, required=false, example=推广活动 唯一键, 32位字符, 例:37a4c0f4cc0810ccd34c61edb409c6e4}, {name=isnature, required=false, example=是否展现自然量数据, 1为是，0为不显示，默认1}]",
        "reportname": "income_byhour",
        "datasource": "mysql",
        "column": "[hours, amt_income_cam, amt_income_def]",
        "name": "[小时, 推广量, 自然量]",
        "key": "hours",
        "desc": "仪表盘>>收入趋势（按小时）"
    },
    {
        "args": "[{name=appid, required=true, example=app unique key, 32字符, 例:37a4c0f4cc0810ccd34c61edb409c6e4}, {name=startdate, required=true, example=起始日期, 例:2016-12-01}, {name=enddate, required=true, example=结束日期, 例:2016-12-07}, {name=iscache, required=false, example=是否需要缓存, 1为是，0为不缓存，默认1}]",
        "reportname": "device_bycarrier",
        "datasource": "mysql",
        "column": "[carrier, num_ins, dau, num_startup]",
        "name": "[运营商, 激活设备, 活跃设备, 启动次数]",
        "key": "carrier",
        "desc": "决策支持>>设备分析>>运营商列表"
    },
    {
        "args": "[{name=appid, required=true, example=app unique key, 32字符, 例:37a4c0f4cc0810ccd34c61edb409c6e4}, {name=startdate, required=true, example=起始日期, 例:2016-12-01}, {name=enddate, required=true, example=结束日期, 例:2016-12-07}, {name=iscache, required=false, example=是否需要缓存, 1为是，0为不缓存，默认1}, {name=campaignid, required=false, example=推广活动 唯一键, 32位字符, 例:37a4c0f4cc0810ccd34c61edb409c6e4}, {name=isnature, required=false, example=是否展现自然量数据, 1为是，0为不显示，默认1}]",
        "reportname": "rate_retentiond1_byds",
        "datasource": "mysql",
        "column": "[ds, rate_retentiond1_cam, rate_retentiond1_def, rate_std]",
        "name": "[日期, 推广量, 自然量, 行业中位数]",
        "key": "ds",
        "desc": "仪表盘>>次日留存趋势（按天）"
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
        "args": "[{name=appid, required=true, example=app unique key, 32字符, 例:37a4c0f4cc0810ccd34c61edb409c6e4}, {name=startdate, required=true, example=起始日期, 例:2016-12-01}, {name=enddate, required=true, example=结束日期, 例:2016-12-07}, {name=iscache, required=false, example=ds\n            是否需要缓存, 1为是，0为不缓存，默认1}]",
        "reportname": "decision_payment_rmb_byds",
        "datasource": "mysql",
        "column": "[num_high_rmb, num_medium_rmb, num_low_rmb]",
        "name": "[大R, 中R, 小R]",
        "key": "ds",
        "desc": "决策支持>>付费洞察>>新用户付费分布"
    },
    {
        "args": "[{name=appid, required=true, example=app unique key, 32字符, 例:37a4c0f4cc0810ccd34c61edb409c6e4}, {name=startdate, required=true, example=起始日期, 例:2016-12-01}, {name=enddate, required=true, example=结束日期, 例:2016-12-07}, {name=campaignid, required=false, example=推广活动unique key, 32位, 例：37a4c0f4cc0810ccd34c61edb409c6e4}, {name=iscache, required=false, example=是否需要缓存, 1为是，0为不缓存，默认1}]",
        "reportname": "campaigninfo_h5_bycampaign",
        "datasource": "mysql",
        "column": "[campaignid, num_click, num_dis_ip, num_register, rate_reged_h5, num_loggin, num_pv, num_uv, num_finishload, num_finishload_uv, num_download, num_order, num_amout, num_payers]",
        "name": "[推广活动, 点击总数, 排重点击IP数, 注册总数, 注册率, 登陆总数, PV, UV, 页面加载完成数, 页面加载完成UV, 下载总数, 订单总数, 付费总金额, 付费总人数]",
        "key": "campaignid",
        "desc": "来源分析>>推广活动详情>>推广活动>>H5监测数据"
    },
    {
        "args": "[{name=appid, required=true, example=app unique key, 32字符, 例:37a4c0f4cc0810ccd34c61edb409c6e4}]",
        "reportname": "sdk_debug_device_count",
        "datasource": "mysql",
        "column": "[appid, deviceid, num, os, campaignid]",
        "name": "[AppKey, 设备ID, 日志数量, 操作系统, 分包渠道]",
        "key": "appid",
        "desc": "新建APP>>数据测试>>调试设备列表"
    },
    {
        "args": "[{name=appid, required=true, example=app unique key, 32字符, 例:37a4c0f4cc0810ccd34c61edb409c6e4}, {name=startdate, required=true, example=起始日期, 例:2016-12-01}, {name=enddate, required=true, example=结束日期, 例:2016-12-07}, {name=iscache, required=false, example=是否需要缓存, 1为是，0为不缓存，默认1}]",
        "reportname": "click_byhour",
        "datasource": "mysql",
        "column": "[hours, num_click]",
        "name": "[小时, 点击量]",
        "key": "hours",
        "desc": "仪表盘>>点击量趋势（按小时）"
    },
    {
        "args": "[{name=appid, required=true, example=app unique key, 32字符, 例:37a4c0f4cc0810ccd34c61edb409c6e4}, {name=startdate, required=true, example=起始日期, 例:2016-12-01}, {name=enddate, required=true, example=结束日期, 例:2016-12-07}, {name=campaignid, required=true, example=推广活动unique key, 32位, 例：37a4c0f4cc0810ccd34c61edb409c6e4}, {name=iscache, required=false, example=是否需要缓存, 1为是，0为不缓存，默认1}]",
        "reportname": "bd_bycampaign_count",
        "datasource": "mysql",
        "column": "[number]",
        "name": "[推广活动总数]",
        "key": "",
        "desc": "来源分析>>推广活动详情>>百度关键词"
    },
    {
        "args": "[{name=appid, required=true, example=app unique key, 32字符, 例:37a4c0f4cc0810ccd34c61edb409c6e4}, {name=startdate, required=true, example=起始日期, 例:2016-12-01}, {name=enddate, required=true, example=结束日期, 例:2016-12-07}, {name=cid, required=false, example=渠道id, 例：23}, {name=iscache, required=false, example=是否需要缓存, 1为是，0为不缓存，默认1}]",
        "reportname": "channelinfo_reged_top5_byds",
        "datasource": "mysql",
        "column": "[ds, dupnum_reged_day]",
        "name": "[日期, 注册量]",
        "key": "ds",
        "desc": "来源分析>>渠道效果对比>>注册趋势TOP5"
    },
    {
        "args": "[{name=appid, required=true, example=app unique key, 32字符, 例:37a4c0f4cc0810ccd34c61edb409c6e4}, {name=startdate, required=true, example=起始日期, 例:2016-12-01}, {name=enddate, required=true, example=结束日期, 例:2016-12-07}, {name=campaignid, required=true, example=推广活动unique key, 32位, 例：37a4c0f4cc0810ccd34c61edb409c6e4}, {name=kwid, required=false, example=关键词id, 例：23}, {name=iscache, required=false, example=是否需要缓存, 1为是，0为不缓存，默认1}]",
        "reportname": "bd_bycreative",
        "datasource": "mysql",
        "column": "[creative, num_click_total, num_click, dupnum_click_all, num_ins, rate_install, dupnum_reg, amt_pay_new, num_pay_new]",
        "name": "[创意, 点击总数, 有效点击总数, 子活动排重点击数, 排重激活设备数, 激活率, 排重注册设备数, 新增付费金额, 新增付费设备数]",
        "key": "creative",
        "desc": "来源分析>>推广活动详情>>百度关键词"
    },
    {
        "args": "[{name=appid, required=true, example=app unique key, 32字符, 例:37a4c0f4cc0810ccd34c61edb409c6e4}, {name=startdate, required=true, example=起始周第一天, 例:2016-12-01}, {name=enddate, required=true, example=结束周第一天, 例:2016-12-07}, {name=usergroupsql, required=true, example=用户组sql，如果没有用户组筛选，就传空字符串}, {name=iscache, required=false, example=是否需要缓存, 1为是，0为不缓存，默认1}]",
        "reportname": "retention_dau_dau_byweek",
        "datasource": "presto",
        "column": "[ds, init, retention1, retention2, retention3, retention4, retention5, retention6, retention7, retention8]",
        "name": "[日期, 初始人数, 1周后, 2周后, 3周后, 4周后, 5周后, 6周后, 7周后, 8周后]",
        "key": "",
        "desc": "活跃活跃周留存"
    },
    {
        "args": "[{name=appid, required=true, example=app unique key, 32字符, 例:37a4c0f4cc0810ccd34c61edb409c6e4}, {name=startdate, required=true, example=起始日期, 例:2016-12-01}, {name=enddate, required=true, example=结束日期, 例:2016-12-07}, {name=dupnum_click_day, required=false, example=按天排重点击数, 例：true}, {name=rate_install, required=false, example=激活率, 例：true}, {name=dupnum_reged_day, required=false, example=按天排重注册设备数, 例：true}, {name=dupnum_reged_mon, required=false, example=排重注册设备数, 例：true}, {name=rate_reged, required=false, example=注册率, 例：true}, {name=rate_retentiond1, required=false, example=D1留存, 例：true}, {name=rate_retentiond3, required=false, example=D3留存, 例：true}, {name=rate_retentiond7, required=false, example=D7留存, 例：true}, {name=rate_retentiond30, required=false, example=D30留存, 例：true}, {name=amt_ltv0, required=false, example=LTV0, 例：true}, {name=amt_ltv7, required=false, example=LTV7, 例：true}, {name=amt_ltv30, required=false, example=LTV30, 例：true}, {name=amt_income_region, required=false, example=区间付费, 例：true}, {name=amt_income_new_user, required=false, example=新增付费, 例：true}, {name=num_payer_new_user, required=false, example=新增付费设备数, 例：true}, {name=amt_income_all_user, required=false, example=总付费, 例：true}, {name=num_payer_all_user, required=false, example=总付费设备数, 例：true}, {name=num_click_fake, required=false, example=异常点击总数, 例：true}, {name=rate_click_fake, required=false, example=异常点击率, 例：true}, {name=num_install_fake, required=false, example=异常激活设备数, 例：true}, {name=rate_install_fake, required=false, example=异常激活率, 例：true}, {name=cid, required=false, example=渠道id, 例：23}, {name=campaignid, required=false, example=推广活动unique key, 32位, 例：37a4c0f4cc0810ccd34c61edb409c6e4}, {name=iscache, required=false, example=是否需要缓存, 1为是，0为不缓存，默认1}]",
        "reportname": "campaigninfo_bycampaign",
        "datasource": "mysql",
        "column": "[campaignid, num_click, dupnum_click_all, dupnum_click_day, num_install, rate_install, dupnum_reged_day, dupnum_reged_mon, rate_reged, rate_retentiond1, rate_retentiond3, rate_retentiond7, rate_retentiond30, amt_ltv0, amt_ltv7, amt_ltv30, amt_income_region, amt_income_new_user, num_payer_new_user, amt_income_all_user, num_payer_all_user, num_click_fake, rate_click_fake, num_install_fake, rate_install_fake]",
        "name": "[推广活动, 点击总数, 排重点击数, 按天排重点击, 排重激活设备数, 激活率, 按天排重注册设备数, 排重注册设备数, 注册率, D1留存, D3留存, D7留存, D30留存, LTV0, LTV7, LTV30, 区间付费, 新增付费, 新增付费设备, 总付费, 总付费设备, 异常点击总数, 异常点击率, 异常激活设备总数, 异常激活率]",
        "key": "campaignid",
        "desc": "来源分析>>推广活动详情>>推广活动"
    },
    {
        "args": "[{name=appid, required=true, example=app unique key, 32字符, 例:37a4c0f4cc0810ccd34c61edb409c6e4}, {name=startdate, required=true, example=起始日期, 例:2016-12-01}, {name=enddate, required=true, example=结束日期, 例:2016-12-07}, {name=cid, required=false, example=渠道id, 例：23}, {name=iscache, required=false, example=是否需要缓存, 1为是，0为不缓存，默认1}, {name=orderby, required=true, example=排序指标, 例:rate_install}]",
        "reportname": "rate_channelinfo_install_top5_bychannel",
        "datasource": "mysql",
        "column": "[cid, rate_install, rate_std]",
        "name": "[渠道, 激活率, 行业中位数]",
        "key": "cid",
        "desc": "来源分析>>渠道效果对比>>激活率top5（有实时）"
    },
    {
        "args": "[{name=appid, required=true, example=app unique key, 32字符, 例:37a4c0f4cc0810ccd34c61edb409c6e4}, {name=categoryid, required=true, example=分类id, 例:2016}, {name=startdate, required=true, example=起始日期, 例:2016-12-01}, {name=enddate, required=true, example=结束日期, 例:2016-12-07}, {name=iscache, required=false, example=是否需要缓存, 1为是，0为不缓存，默认1}]",
        "reportname": "decision_potencial_top10_bychannel",
        "datasource": "mysql",
        "column": "[num_potencial]",
        "name": "[用户数]",
        "key": "cid",
        "desc": "决策支持>>潜在用户群>>潜在用户推广来源top10"
    },
    {
        "args": "[{name=appid, required=true, example=app unique key, 32字符, 例:37a4c0f4cc0810ccd34c61edb409c6e4}, {name=startdate, required=true, example=起始日期, 例:2016-12-01}, {name=enddate, required=true, example=结束日期, 例:2016-12-07}, {name=cid, required=false, example=渠道id, 例：23}, {name=iscache, required=false, example=是否需要缓存, 1为是，0为不缓存，默认1}]",
        "reportname": "rate_channelinfo_install_top5_byds",
        "datasource": "mysql",
        "column": "[ds, rate_install]",
        "name": "[日期, 激活率]",
        "key": "ds",
        "desc": "来源分析>>渠道效果对比>>点击趋势TOP5"
    },
    {
        "args": "[{name=appid, required=true, example=app unique key, 32字符, 例:37a4c0f4cc0810ccd34c61edb409c6e4}, {name=startdate, required=true, example=起始日期, 例:2016-12-01}, {name=enddate, required=true, example=结束日期, 例:2016-12-07}, {name=cid, required=false, example=渠道id, 例：23}, {name=iscache, required=false, example=是否需要缓存, 1为是，0为不缓存，默认1}]",
        "reportname": "channelinfo_click_top5_byhour",
        "datasource": "mysql",
        "column": "[hours, num_click]",
        "name": "[小时, 点击量]",
        "key": "hours",
        "desc": "来源分析>>渠道效果对比>>点击趋势TOP5"
    },
    {
        "args": "[{name=startdate, required=true, example=起始日期, 例:2016-12-01}, {name=enddate, required=true, example=结束日期, 例:2016-12-07}]",
        "reportname": "home_dau_bygeo",
        "datasource": "mysql",
        "column": "[shortname, lon, lat, dau]",
        "name": "[地区, 经度, 纬度, dau]",
        "key": "shortname",
        "desc": "门户地图报表"
    },
    {
        "args": "[{name=appid, required=true, example=app unique key, 32字符, 例:37a4c0f4cc0810ccd34c61edb409c6e4}, {name=startdate, required=true, example=起始日期, 例:2016-12-01}, {name=enddate, required=true, example=结束日期, 例:2016-12-07}, {name=cid, required=false, example=渠道id, 例：23}, {name=iscache, required=false, example=是否需要缓存, 1为是，0为不缓存，默认1}]",
        "reportname": "channelinfo_payer_top5_byhour",
        "datasource": "mysql",
        "column": "[hours, num_payer_all_user]",
        "name": "[小时, 付费设备数]",
        "key": "hours",
        "desc": "来源分析>>渠道效果对比>>付费设备趋势TOP5"
    },
    {
        "args": "[{name=appid, required=true, example=app unique key, 32字符, 例:37a4c0f4cc0810ccd34c61edb409c6e4}, {name=startdate, required=true, example=起始日期, 例:2016-12-01}, {name=enddate, required=true, example=结束日期, 例:2016-12-07}, {name=cid, required=true, example=渠道id, 例：23}, {name=iscache, required=false, example=是否需要缓存, 1为是，0为不缓存，默认1}]",
        "reportname": "subchannel_bycampaign",
        "datasource": "mysql",
        "column": "[campaignid, num_click_total, num_click, dupnum_click_all, num_ins, dupnum_reg, rate_install]",
        "name": "[推广活动, 点击总数, 有效点击总数, 排重点击数, 排重激活设备数, 排重注册设备数, 激活率]",
        "key": "campaignid",
        "desc": "来源分析>>推广活动详情>>子渠道"
    },
    {
        "args": "[{name=appid, required=true, example=app unique key, 32字符, 例:37a4c0f4cc0810ccd34c61edb409c6e4}, {name=startdate, required=true, example=起始日期, 例:2016-12-01}, {name=enddate, required=true, example=结束日期, 例:2016-12-07}, {name=iscache, required=false, example=是否需要缓存, 1为是，0为不缓存，默认1}]",
        "reportname": "dau_byds",
        "datasource": "mysql",
        "column": "[ds, dau]",
        "name": "[日期, DAU]",
        "key": "ds",
        "desc": "仪表盘>>DAU趋势（按天）"
    },
    {
        "args": "[{name=appid, required=true, example=app unique key, 32字符, 例:37a4c0f4cc0810ccd34c61edb409c6e4}, {name=startdate, required=true, example=起始日期, 例:2016-12-01}, {name=enddate, required=true, example=结束日期, 例:2016-12-07}, {name=iscache, required=false, example=是否需要缓存, 1为是，0为不缓存，默认1}]",
        "reportname": "channelclick_top10_bychannel",
        "datasource": "mysql",
        "column": "[cid, num_click]",
        "name": "[渠道, 点击量]",
        "key": "cid",
        "desc": "仪表盘>>渠道点击top10"
    },
    {
        "args": "[{name=appid, required=true, example=app unique key, 32字符, 例:37a4c0f4cc0810ccd34c61edb409c6e4}, {name=startdate, required=true, example=起始日期, 例:2016-12-01}, {name=enddate, required=true, example=结束日期, 例:2016-12-07}, {name=iscache, required=false, example=是否需要缓存, 1为是，0为不缓存，默认1}, {name=campaignid, required=false, example=推广活动 唯一键, 32位字符, 例:37a4c0f4cc0810ccd34c61edb409c6e4}, {name=isnature, required=false, example=是否展现自然量数据, 1为是，0为不显示，默认1}]",
        "reportname": "reged_byhour",
        "datasource": "mysql",
        "column": "[hours, num_reged_cam, num_reged_def]",
        "name": "[小时, 推广量, 自然量]",
        "key": "hours",
        "desc": "仪表盘>>注册量趋势（按小时）"
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
        "args": "[{name=appid, required=true, example=app unique key, 32字符, 例:37a4c0f4cc0810ccd34c61edb409c6e4}, {name=startdate, required=true, example=起始月的1号, 例:2016-12-01}, {name=enddate, required=true, example=结束月的1号, 例:2017-02-01}, {name=usergroupsql, required=true, example=用户组sql，如果没有用户组筛选，就传空字符串}, {name=iscache, required=false, example=是否需要缓存, 1为是，0为不缓存，默认1}]",
        "reportname": "retention_install_dau_bymonth",
        "datasource": "presto",
        "column": "[ds, init, retention1, retention2, retention3]",
        "name": "[日期, 初始人数, 1月后, 2月后, 3月后]",
        "key": "",
        "desc": "新增活跃月留存"
    },
    {
        "args": "[{name=appid, required=true, example=app unique key, 32字符, 例:37a4c0f4cc0810ccd34c61edb409c6e4}, {name=startdate, required=true, example=起始日期, 例:2016-12-01}, {name=enddate, required=true, example=结束日期, 例:2016-12-07}, {name=iscache, required=false, example=是否需要缓存, 1为是，0为不缓存，默认1}]",
        "reportname": "delay_install_bycampaign",
        "datasource": "mysql",
        "column": "[campaignid, num_install, num_clk_d0, num_clk_d1, num_clk_d2, num_clk_d3, num_clk_d4, num_clk_d5, num_clk_d6, num_clk_d7, num_clk_d8_14, num_clk_d15]",
        "name": "[推广活动, 排重激活设备数, 当日点击, 前1日点击, 前2日点击, 前3日点击, 前4日点击, 前5日点击, 前6日点击, 前7日点击, 前8-14日点击, 15日前点击]",
        "key": "campaignid",
        "desc": "归因分析>>激活延迟分析>>按激活"
    },
    {
        "args": "[{name=appid, required=true, example=app unique key, 32字符, 例:37a4c0f4cc0810ccd34c61edb409c6e4}, {name=startdate, required=true, example=起始日期, 例:2016-12-01}, {name=enddate, required=true, example=结束日期, 例:2016-12-07}, {name=iscache, required=false, example=是否需要缓存, 1为是，0为不缓存，默认1}]",
        "reportname": "delay_click_bycampaign",
        "datasource": "mysql",
        "column": "[campaignid, num_click, dupnum_click_all, dupnum_click_day, num_ins_d0, num_ins_d1, num_ins_d2, num_ins_d3, num_ins_d4, num_ins_d5, num_ins_d6, num_ins_d7, num_ins_d8_14, num_ins_d15]",
        "name": "[推广活动, 有效点击总数, 排重点击数, 按天排重点击数, 当日激活, 后1日激活, 后2日激活, 后3日激活, 后4日激活, 后5日激活, 后6日激活, 后7日激活, 后8-14日激活, 15日后激活]",
        "key": "campaignid",
        "desc": "归因分析>>激活延迟分析>>按点击"
    },
    {
        "args": "[{name=appid, required=true, example=app unique key, 32字符, 例:37a4c0f4cc0810ccd34c61edb409c6e4}]",
        "reportname": "app_install_register_byappids",
        "datasource": "mysql",
        "column": "[cum_num_install, cum_dupnum_reged_mon]",
        "name": "[激活, 注册]",
        "key": "appid",
        "desc": "APP/H5>>APP列表>>激活注册数"
    },
    {
        "args": "[{name=appid, required=true, example=app unique key, 32字符, 例:37a4c0f4cc0810ccd34c61edb409c6e4}, {name=startdate, required=true, example=起始月的1号, 例:2016-12-01}, {name=enddate, required=true, example=结束月的1号, 例:2017-02-01}, {name=usergroupsql, required=true, example=用户组sql，如果没有用户组筛选，就传空字符串}, {name=iscache, required=false, example=是否需要缓存, 1为是，0为不缓存，默认1}]",
        "reportname": "retention_install_dau_bymonth",
        "datasource": "presto",
        "column": "[ds, init, retention1, retention2, retention3]",
        "name": "[日期, 初始人数, 1月后, 2月后, 3月后]",
        "key": "",
        "desc": "新增活跃月留存"
    },
    {
        "args": "[{name=appid, required=true, example=app unique key, 32字符, 例:37a4c0f4cc0810ccd34c61edb409c6e4}, {name=startdate, required=true, example=起始日期, 例:2016-12-01}, {name=enddate, required=true, example=结束日期, 例:2016-12-07}, {name=cid, required=false, example=渠道id, 例：23}, {name=iscache, required=false, example=是否需要缓存, 1为是，0为不缓存，默认1}]",
        "reportname": "channelinfo_amount_top5_byds",
        "datasource": "mysql",
        "column": "[ds, amt_income_all_user]",
        "name": "[日期, 付费设备数]",
        "key": "ds",
        "desc": "来源分析>>渠道效果对比>>收入趋势TOP5"
    },
    {
        "args": "[{name=appid, required=true, example=app unique key, 32字符, 例:37a4c0f4cc0810ccd34c61edb409c6e4}, {name=startdate, required=true, example=起始日期, 例:2016-12-01}, {name=enddate, required=true, example=结束日期, 例:2016-12-07}, {name=iscache, required=false, example=是否需要缓存, 1为是，0为不缓存，默认1}]",
        "reportname": "device_byregion",
        "datasource": "mysql",
        "column": "[region, num_ins, dau, num_startup]",
        "name": "[地域, 激活设备, 活跃设备, 启动次数]",
        "key": "region",
        "desc": "决策支持>>设备分析>>地域列表"
    },
    {
        "args": "[{name=appid, required=true, example=app unique key, 32字符, 例:37a4c0f4cc0810ccd34c61edb409c6e4}, {name=startdate, required=true, example=起始周第一天, 例:2016-12-01}, {name=enddate, required=true, example=结束周第一天, 例:2016-12-07}, {name=usergroupsql, required=true, example=用户组sql，如果没有用户组筛选，就传空字符串}, {name=iscache, required=false, example=是否需要缓存, 1为是，0为不缓存，默认1}]",
        "reportname": "retention_dau_dau_byweek",
        "datasource": "presto",
        "column": "[ds, init, retention1, retention2, retention3, retention4, retention5, retention6, retention7, retention8]",
        "name": "[日期, 初始人数, 1周后, 2周后, 3周后, 4周后, 5周后, 6周后, 7周后, 8周后]",
        "key": "",
        "desc": "活跃活跃周留存"
    },
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