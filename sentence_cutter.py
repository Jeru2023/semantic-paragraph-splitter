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
        cuter = StateMachine(long_short_cuter(hard_max=128, max_len=128, min_len=15))
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
        """1月M2增速为什么快速下滑？。
核心观点：2024年1月M2同比增长8.7%，增速回落1pct，处于历史较低水平。M2当月新增5.35万亿元，同比少增约2万亿元，带来M2增速快速下滑。为什么会出现同比大幅少增的现象，首先要拆解M2从何处派生。
M2从何处派生？1月M2同比少增主要由于银行购买资管产品项目派生货币减少。
因此，2024年1月出现M2增速的快速下滑，主要是由于去年的高基数，而高基数是由于银行购买资管产品项目派生的广义货币超出历史平均水平带来的，单月的快速下滑不必过度解读，M2增速可能在2月出现回升。
本周市场观察（2月18日-2月23日）：公开市场操作：逆回购净回笼8410亿元，MLF净投放10亿元。
货币市场利率春节后回落，后半周临近月末季节性上行：SHIBOR007和DR007分别收于1.8160%（-4BP）、1.8425%（-1BP）。GC007收于2.21%（+17BP）。R007收于2.1247%（+27BP），与DR007利差快速扩大。
银行间质押式回购日成交量快速上升：从上周的约4.6万亿上升至约6.3万亿。
5年期LPR调降25BP，国债收益率曲线下移，期限利差扩大：10年期中债国债收益率收于2.40%（-3BP），1年期收于1.77%（-16BP）同业存单发行利率继续回落：1年期国有银行同业存单发行利率回落至2.25%（-7BP）；股份制银行收于2.27%（-3BP）。
美元指数回落至104下方，非美货币涨跌互现，人民币小幅贬值：人民币即期汇率收于7.1984（+57pips），日元-0.22%、韩元+0.33%、欧元+0.42%、加元+0.06%、澳元+0.83%、英榜+0.43%。
融高频数据周报（2024年2月19日。
1.政策理解不到位的风险2.央行货币政策超预期的风险3.政府债券发行超预期的风险4.经济超预期下行的风险5.美联储紧缩周期超预期加长的风险。
DR007与DR001利差扩张后收窄至10BP。"""
    ]
    # result = [sc.cut_sentences(para) for para in paragraph]
    # print('# of sents ', len(result[0]))
    # for chunk in result[0]:
    #     print('----------------')
    #     print(chunk)

    # split first element in paragraph by \n
    paras = paragraph[0].split('\n')
    print(len(paras))
    for para in paras:
        print('----------------')
        print(para)