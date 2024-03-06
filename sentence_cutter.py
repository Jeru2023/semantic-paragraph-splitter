# -*- encoding: utf-8 -*-
from langdetect import detect
#from langdetect import detect_langs
from sentence_spliter import spliter
from sentence_spliter.logic_graph_en import long_cuter_en
from sentence_spliter.automata.state_machine import StateMachine
from sentence_spliter.automata.sequence import EnSequence
from sentence_spliter.logic_graph import long_short_cuter
from sentence_spliter.automata.sequence import StrSequence
import spacy


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
        cuter = StateMachine(long_short_cuter(hard_max=500, max_len=500, min_len=15))
        sequence = cuter.run(StrSequence(text))
        sentences = sequence.sentence_list()
        return sentences

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

        """政府工作报告有何细节？。
经济增长、通胀、就业等目标均符合预期，量化的能耗指标重新出现：（1）“5%左右”的国内生产总值增长自标与去年保持一致，也符合前期预期和各地两会所传达的信息；（2）城镇新增就业由去年的“1200方人左右”调整为“1200万人以上”，城镇调查失业率5.5%左右，与去年相同；（3）居民消费价格涨幅3%左右、居民收入增长和经济增长同步、国际收支保持基本平衡、粮食产量1.3万亿斤以上等表态也基本和去年一致，但值得注意的是，本次政府工作报告提出“单位国内生产总值能耗降低2.5%左右”，去年没有相应量化目标，而是提出“单位国内生产总值能耗和主要污染物排放量继续下降”，这一变化可能与当下对推动先进产能比重持续提升的追求有关。
财政加力将成为增长目标实现的重要支撑：（1）在存在超长期建设国债（专项用于国家重大战略实施和重点领域安全能力建设）的背景下，即使赤字率保持在3%（低于去年3.8%的最终水平），财政加力也得到充分体现，且本次会议不仅公布了今年即将发行的1万亿超长期特别国债，也预告了未来拟连续几年发行，充分体现出“稳定透明可预期”的特点；（2）财政力度来看，赤字规模4.06万亿，比上年年初预算增加1800亿元，在此基础上一般公共预算支出规模28.5万亿，比上年增加1.1万亿，这一水平高于去年（2023年的预算相比2022年来说增加8000余亿元），但增速下降（今年增速3.6%左右，去年预算报告公布的增速为5.6%）。此外专项债3.9万亿元，比上年增加1000亿元。
货币政策方面，“避免资金沉淀空转”出现在本次报告中，这一表态自十八大以来未曾在两会政府工作报告中出现（2019年有“不能让资金空转或脱实向虚”，含义与当前略有不同），体现出了决策层对货币政策传导机制和金融体系运转的重视。实际上从去年下半年开始，央行、金融监管总局都已经针对这一问题多有表态（如2023年8月4日央行金融数据发布会等），可见相应措施与政策考量尚未结束。此外“五篇大文章”在本次报告中也有所体现。
重视两会政府工作报告所传达的改革信号，具体包括：（1）对外开放方面，全面取消制造业领域外资准入限制措施，放宽电信、医疗等服务业市场准入，保障外资企业依法平等参与政府采购、招标投标、标准制定，推动解决数据跨境流动等问题。与去年相比，今年的亮点在于制造业的全面准入放开，同时现代服务业的开放也更有针对性（具体到医疗和电信行业），制度型开放有望更进一步；（2）通过改革红利进一步改善农民收入，启动第二轮土地承包到期后再延长30年整省试点，深化集体产权、集体林权、农垦、供销社等改革，预计当前农村收入增速好于城镇的局面还会延续，这可能会对人口与就业带来深远影响；（3）针对地方保护、市场分割、招商引资不当竞争等突出问题开展的专项治理预计是今年全国统一大市场建设的重点，叠加专项债额度分配向项目准备充分、投资效率较高的地区倾斜，市场与效率将在政府间资源配置中扮演更加决定性的作用，区域发展可能也会因此开启新篇章。
"""
    ]

    result = [sc.cut_sentences(para) for para in paragraph]
    print('# of sents ', len(result[0]))
    for chunk in result[0]:
        print('----------------')
        print(chunk)

    # split first element in paragraph by \n
    # paras = paragraph[0].split('\n')
    # print(len(paras))
    # for para in paras:
    #     print('----------------')
    #     print(para)
