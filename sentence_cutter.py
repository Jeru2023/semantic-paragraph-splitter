# -*- encoding: utf-8 -*-
from langdetect import detect
from sentence_spliter.logic_graph_en import long_cuter_en
from sentence_spliter.automata.state_machine import StateMachine
from sentence_spliter.automata.sequence import EnSequence
from sentence_spliter.logic_graph import long_short_cuter
from sentence_spliter.automata.sequence import StrSequence
import spacy
from my_utils import timer


class SentenceCutter:
    def __init__(self):
        self.nlp_en = spacy.load("en_core_web_sm")

    @staticmethod
    def cut_english_sentences(text):
        # 令句子长度不能小于5个单词
        long_machine_en = StateMachine(long_cuter_en(min_len=5))
        m_input = EnSequence(text)
        long_machine_en.run(m_input)
        sentences = m_input.sentence_list()
        return sentences

    @staticmethod
    def cut_chinese_sentences(text):
        # -- 初始化 状态机器 -- #
        cuter = StateMachine(long_short_cuter(hard_max=500, max_len=500, min_len=30))
        sequence = cuter.run(StrSequence(text))
        sentences = sequence.sentence_list()
        return sentences

    @timer
    def cut_sentences(self, text):
        lang = detect(text)
        #print(lang)
        if lang.startswith('zh'):
            # 中文切句调用 cut_to_sentences
            sentences = self.cut_chinese_sentences(text)
        elif lang == 'en':
            # 英文切句调用 split_sentences
            # sentences = self.cut_english_sentences(text)
            doc = self.nlp_en(text)
            sentences = [sent.text for sent in doc.sents]
        else:
            return []
        return sentences


if __name__ == '__main__':
    sc = SentenceCutter()
    paragraph = [
        # "在很久很久以前......。。... 有座山，山里有座庙啊!!!!!!!庙里竟然有个老和尚！？。。。。",
        # "A long time ago..... there is a mountain, and there is a temple in the mountain!!! And here is an old monk in the temple!?....",
        # "“我和你讨论的不是一个东西，死亡率与死亡比例是不同的”，“你知道么？CNN你们总是制造假新闻。。。”",
        # "张晓风笑着说道，“我们这些年可比过去强多了！“过去吃不起饭，穿不暖衣服。 现在呢？要啥有啥！",
        # "\"What would a stranger do here, Mrs. Price?\" he inquired angrily, remembering, with a pang, that certain new, unaccountable, engrossing emotions had quite banished Fiddy from his thoughts and notice, when he might have detected the signs of approaching illness, met them and vanquished them before their climax.",
        # "Notice that U.S.A. can also be written USA, but U.S. is better with the periods. Also, we can use U.S. as a modifier (the U.S. policy on immigration) but not as a noun (He left the U.S. U.S.A.).",
        # "万壑树参天，千山响杜鹃。山中一夜雨，树杪百重泉。汉女输橦布，巴人讼芋田。文翁翻教授，不敢倚先贤。",
        #"美元指数回落至104下方，非美货币涨跌互现，人民币小幅贬值：人民币即期汇率收于7.1984（+57pips），日元-0.22%、韩元+0.33%、欧元+0.42%、加元+0.06%、澳元+0.83%、英榜+0.43%。",

        """
        “不加修饰”也通过愉悦的视角，赋予了多元化设计许多可能性。1.2 “Pardon"这一命名本身便蕴含着幽默，虽是表达歉意的单词，但这款字体本身却相当坚持个性。人民币小幅贬值：人民币即期汇率收于7.1984（+57pips)
        """
    ]

    paragraph = """
        >1供给端：本周国内碳酸锂产量较假期有所增加，锂盐厂家陆续开工，治炼厂库存略有累积。多数检修的锂盐厂将于元宵节前后复工，但大部分停产的外购锂矿的中小型锂盐企业表示将根据市场行情择机恢复生产，初步预计2月碳酸锂产量将环比下滑23%至3.2万吨附近。中长期维度看，今明两年是上游锂矿和盐湖放量的大年，碳酸锂供应过剩的压力较大。消息面上，20日晚上市场有关于江西碳酸锂环保停产的传闻传出，后传闻的内容多数被证伪，但锂盐企业表示近期有相关环保回头看活动。周五上午，澳洲锂生产商ArcadiumLithium在财报中显示，因受成本压力影响，Mt Catt1in矿山在2024年的锂辉石精矿产量预期将从2023年的20.5万吨下降至13万吨（减产约9500吨LCE）。
    》需求端：本周需求端有小幅改善。正极等下游企业已经逐渐采购现货补充原料，但对当前价位的接受度不高。供需双方仍处于博弈中，需求主导价格走势。中游锂电逐渐进入排产旺李，但鉴于电池厂的高库存及订单前置，节后实际补库需求的强度仍需观察。终端市场方面，受节前促销活动刺激购车需求提前释放，春节期间消费者需求不振，且经销商库存仍需消耗，2月国内新能源汽车产销或将继续环比下滑。电动车价格战仍在持续，行业内卷加剧，对应车企降本压力较大。
    》成本端：本周国内锂精矿价格小幅下跌，锂盐生产企业对于原料的补库意愿不强，多持观望情绪。进口方面，由于锂盐厂持续的长单提货、非洲锂矿集中到港的影响，预计2月锂矿到港量仍处相对高位。》策略：本周受消息面影响，碳酸锂期货的价格震荡反弹。深层次原因是，经过前期的持续下跌后，市场对做空的因素已经演绎得比较充分。而随着需求旺季的到来，下游有一定的补库预期，叠加供应端出现的扰动，碳酸锂期货的价格短期可能仍有一定的上行动能。操作上，短期多空资金博弈加剧，消息面扰动较多，建议投资者暂时观望为主。
    2023年12月中国锂矿石进口数量为42.30万吨，环比增加14.07%，同比增加32.65%。其中从澳大利亚进口28.80万吨，环比增加36.4%，同比增加11.2%。自巴西进口1.09万吨，环比减少70.6%，同比减少4.6%。）由于锂盐厂持续的长单提货、非洲锂矿集中到港的影响，预计2月的到港量仍处相对高位，矿端供应偏宽松。雅化集团在津巴布韦自有矿山Kamativi首批5000吨锂精矿将陆续运达国内。目前项目一期采选生产规模年处理矿石量30万吨。二期采选生产规模年处理矿石量200万吨已同步启动建设，预计将于今年6月建成。一二期投产达标后项目年产锂精矿将达35万吨。
    》）本周锂精矿（6%）CIF中间价坏比下滑2.13%，锂云母（2-2.5%）精矿的价格环比持平。近期，锂矿跌势明显放缓。
    ）锂矿价格的下滑给碳酸锂的价格带来一定压力。矿山出于自身现金流、股价因素考虑，即使有一定成本倒挂影响，短期内的产量预计依旧较为稳定。港口矿库存仍在累积，近期部分企业争取到M+2的定价模式。
    锂云母精矿（2-2.5%Li）市场价。
    1月国内碳酸锂产量约4.2万吨，环比-5.6%，同比15.6%。分原料情况看，1月国内锂辉石、锂云母、盐湖产量15430吨、12280吨、7488吨，月度环比分别变化-5.8%、-7.4%、+4.1%。2多数检修的锂盐厂将于元宵节前后逐渐恢复生产，但大部分停产的外购锂矿的中小型锂盐企业表示将根据市场行情择机恢复生产，初步预计2月碳酸锂产量将环比下滑23%至3.2万吨附近。
    11+2023年1-12月国内累计进口碳酸锂15.8万吨，累计同比增长10.54%。其中，12月中国进口碳酸锂约2.03万吨，环比增长19.34%，同比增长86.9%。智利占据我国碳酸锂进口的绝对主导地位。智利1月出口至国内9818吨碳酸锂，处于近两年较低位置。
    一22023年1-12月中国碳酸锂出口数量为0.96万吨，同比减少8.08%。其中，12月中国碳酸锂出口数量为0.03万吨。
    本周电池级碳酸锂现货价格96000元/吨，较上周小幅下降0.5%。长协结清和套保机会使贸易商和锂盐生产商的出货压力有所下降，挺价意愿较强。下游厂家观望情绪较浓，对高价格的接受度不高。一本周工业级碳酸锂价格88500元/吨，较上周持平。
    》今年1月新能源汽车产销分别完成78.7万辆和72.9万辆，环比分别下降32.9%和38.8%，同比分别增长85.3%和78.8%，市场占有率达到29.9%，销售情况不及市场预期。受节前促销活动刺激购车需求提前释放，春节期间消费者需求不振，且经销商库存仍需消耗，2月国内新能源汽车产销或将继续环比下滑。
    电动车价格战仍在持续，2月19日比亚迪发文秦PLUS、驱逐舰05荣耀版上市，7.98万元起售。行业内卷加剧，对应车企降本压力较大。
    1月我国动力电池产量65.2GWh，同比增长68%，环比下降16.1%。1月我国动力电池装车量32.3GWh，同比增长?100.2%，环比下降32.6%。我国动力和其他电池出口量为8.4GWh，占当月销量的14.7%，其中动力电池出口量为8.2GWh，同比增长9%。
    1去年由于锂价高位回落叠加需求放缓，全年电池厂家及整车制造企业一直在主动去库，但去库效果不佳，库存下降比例仅20%左右。截止2023年12月底，中国动力电芯的库存为130.4GWh，高库存对2024年的销售端也将造。
    2023年1-12月我国智能手机累计产量10.3亿部，累计同比增长0.85%。12月智能手机产量1.3亿部，同比增长29.3%，增速较上月继续提升。12023年1-12月我国电子计算机整机累计产量3.1亿台，累计同比下降15.7%。12月电子计算机整机产量3256万台，同比下降5.6%，降幅较上月小幅扩大，电子计算机整机产量当月值。
    >）2023年1-12月我国太阳能发电累计装机容量6.1亿十瓦，同比增长55.2%。12月我国太阳能发电装机容量5186万千瓦，同比增长151.9%。
    >）据GGII调研统计，2023年前三李度中国储能锂电池出货量127GWh，同比增长44%。2023Q3中国储能锂电池出货量40GW，环比下降30%。具体领域看，工商业储能增长较快，电力储能/户用储能增速放缓，通信储能/便携式储能需求疲软。
    随着锂精矿价格的快速下行，锂盐厂的生产成本也有所下降。外购锂辉石加工的厂商的理论生产成本89472元/吨，环比下降1342元/吨。转变锂矿定价模式后，外购锂辉石加工的厂商亏损情况逐渐好转。对锂盐厂而言，矿价下跌对冲了大部分跌价损失，亏损变得可控，同时意味着锂盐厂形成减产联盟的难度倍增。外购锂辉石加工的厂商的理论生产毛利6027元/吨，环比增加342元/吨，理论生产毛利转正，本周三元材料企业的理论生产毛利1250元/吨，较上周增加4000。近期三元材料企业毛利持续回落，且处在近一较低水平。中游锂电处于排产淡季，正极企业的产能利用率仍在较低水平。1月三元材料企业的产能利用率41.8%，环比下滑3.2%，磷酸铁锂企业产能利用率30.8%，环比下滑6.2%。春节后，锂电逐渐进入排产旺季，预计排产将逐步回升。因正极厂进行了节前备库，对碳酸锂的补库影响可能要从3月开始显现。
    本周碳酸锂基差-1600，较上周环比下降5850。本周碳酸锂近月期货价格震荡走强至97600，而现货价格企稳，近月合约基差转负。电碳与工碳之间的价差环比小幅减少，减少500元/吨至7000元/吨。
    本周碳酸锂合约期限结构为contango结构。远月与近月合约的价差整体较上月有所扩大。连一与近月合约的价差3500，较上周增加3150。01、02及03合约之间的价差较小。主力合约与近月合约的价差4200。
        """

    paragraph = "一句话得分的咖啡快点放开对方的咖啡店看短发短发短发短发短发短发短发。\"接着说短发短发短发。"

    sentences = sc.cut_sentences(paragraph)
    print('number of sentences:', len(sentences))
    for sentence in sentences:
        print('----------------')
        print(sentence.strip())

    # sentences = [sc.cut_sentences(para) for para in paragraph]
    # print('# of sentences ', len(result[0]))
    # for chunk in result[0]:
    #     print(chunk.strip())

    # split first element in paragraph by \n
    # paras = paragraph[0].split('\n')
    # print(len(paras))
    # for para in paras:
    #     print('----------------')
    #     print(para)