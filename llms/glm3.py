#!/usr/bin/python
# -*- coding: utf-8 -*-


class ChatGlm3:
    def __init__(self,api_base):
        self.api_base = api_base

    def generate(self,msg):
        import openai

        openai.api_base = self.api_base
        openai.api_key = "none"
        openai.api_type = "open_ai"
        model = ""

        completion = openai.ChatCompletion.create(
            model=model,
            messages=[{"role": "user", "content": msg}],
            temperature=0,
            top_p=0,
            max_tokens=8192,
        )
        message = completion.choices[0].message.content
        return message


if __name__ == '__main__':
    obj = ChatGlm3()

    query_list = [
        "饮用水行业中，天猫销售额超过五百万中销量排名前三的品牌是哪些",
        "乳制品行业中，天猫销售额超过两千万且销量排名前三的品牌是什么",
        "天猫均价1000元以上，销售额最高且超过三千万的户外服饰品牌是什么",
        "京东香水行业销售额超过五百万时，均价最高的前三个品牌是什么",
        "护肤行业京东客单价在90~120元之间，销售额最高的前三个品牌有哪些",
        "潮玩动漫行业京东客单价超过一百块，销售额最高的前两个品牌",
        "天猫销售额在两千万以上且销售额同比增长超过20%的前五个户外服饰品牌有哪些",
        "办公设备行业销售额在三千万到四千万之间，销售额同比增速最快的品牌",
        "线上平台销售额最高的五个品牌中，销售额环比增速最快的前两个品牌",
        "线上平台销售额超过一亿且环比且环比增速最快的3个国产白酒品牌",
        "葡萄酒行业线上销售额销售额大于一千万时，其增速最快的前三个品牌",
        "啤酒行业线上销售额前三中，销售额增速最快的品牌是什么？",
        "2023年7月蜜雪冰城租金是多少",
        "自然堂 Chando上海坪效",
        "名创优品 Miniso西北地区租金",
        "昌盛大药房全国新关门店数",
        "23H1金六福珠宝重庆闭店率",
        "22Q4斯凯奇 Skechers全国二线城市新开门店数",
        "22年上半年阿迪达斯 Adidas华东地区门店面积",
        "博士眼镜新开门店数同比变化",
        "舞东风门店总数同比变化",
        "2022下半年唇笔抖音均价环比增长是多少",
        "足浴剂最近一年线上销量是多少",
        "2023年9月抖音平台女装配饰在CR5集中度环比？",
        "2023年上半年京东平台婴幼儿牛奶粉在CR10集中度是多少？",
        "2023Q3年京东平台纸尿裤在CR5的集中度同比增速？",
        "女装23年9月天猫折扣率是多少",
        "鞋柜23年Q3天猫销量同比增长",
        "蜂花22年抖音销售额是多少",
        "护手霜京东均价是多少",
        "2023年Q1弹拨乐器在天猫的折扣率是多少？",
        "2022敦煌乐器的销售量同比增速为？",
        "苹果 Apple天猫销售额",
        "魅族 Meizu天猫销量",
        "联想 Lenovo天猫均价增速如何",
        "华硕 Asus天猫销量增速如何",
        "华硕 Asus天猫销量增速如何",
        "华硕 Asus天猫销量增速如何",
        "惠普 Hp天猫销售额同比变化是什么",
        "三只松鼠 Three Squirrels京东销售额同比增长多少",
        "开心果京东集中度",
        "食品饮料中月饼京东均价",
        "2023Q2王小卤京东销量",
        "22年农夫山泉天猫销售额同比增速是多少",
        "22年农夫山泉天猫销量同比增速是多少",
        "22年H2农夫山泉天猫销售额环比增速是多少",
        "22年H2农夫山泉天猫销量环比增速是多少",
        "23年上半年烘干机京东销量是多少",
        "烘干机京东销量变化了多少",
        "烘干机京东销售额变化了多少",
        "吹风机京东销量变化了多少",
        "吹风机京东销售额变化了多少",
        "23年Q3烘干机京东销售额环比变化了多少",
        "23年9月吹风机京东销量同比变化了多少",
        "苏泊尔 Supor天猫销售额",
        "优衣库 Uniqlo天猫销量",
        "南极人 Nanjiren天猫均价",
        "西门子 Siemens天猫销量",
        "索尼 Sony京东销售额",
        "晨光文具 M&g京东销量",
        "23年Q1无人机京东客单价",
        "哈曼·卡顿 Harman kardon京东销量环比",
        "领带京东销量",
        "电动鼻毛修剪器京东均价",
        "调味品京东销售额",
        "22年Q3苏泊尔 Supor天猫销售额",
        "22年Q4优衣库 Uniqlo天猫销量",
        "22年Q1南极人 Nanjiren天猫均价",
        "22年西门子 Siemens天猫销量",
        "23年Q2苏泊尔 Supor天猫销售额同比变化是多少",
        "23年Q2优衣库 Uniqlo天猫销量环比变化是多少",
        "22年Q1南极人 Nanjiren天猫均价环比变化是多少",
        "23年西门子 Siemens天猫销售额同比变化是多少",
        "23Q3调味品京东销售额同比变化了多少",
        "百丽天猫销售额",
        "百丽京东销量",
        "江中食疗京东销售额变化",
        "五谷磨房天猫销量变化",
        "电热水器天猫销售额",
        "成人奶粉京东均价",
        "2023年Q2未来式天猫市占率",
        "22年Q4优勤天猫销量",
        "2023年帘香客天猫销售额同比变化",
        "2023年益伟京东销量同比变化",
        "2023年9月保暖内衣京东销售额",
        "2022年Q4睡裙京东睡裙的均价",
        "帽子京东销售额同比变化是什么",
        "布艺沙发京东均价同比变化",
        "2022Q4马丁靴京东集中度环比是什么",
        "2023年高帮鞋京东销量环比变化",
        "2023Q2年松糕鞋京东集中度环比变化",
        "2023年皮布沙发京东销售额环比变化",
        "23年班亚奴京东市占率同比变化是什么",
        "23年Q3汤丽柏琦京东市占率环比变化是什么",
        "海康威视销售额",
        "珈柔销售额",
        "朝宇销售额",
        "尚纸坊销售额",
        "按摩椅销售额",
        "按摩披肩销售额",
    ]

    for query in query_list:
        _msg = f'''
        请根据Query判断是否存在多个条件或限制
        [Query] = [{query}]
        你只需要回答 true 或者 false, 不需要回答其他额外的内容
        '''
        print(obj.generate(_msg))
