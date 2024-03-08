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
    “不加修饰”也通过愉悦的视角，赋予了多元化设计许多可能性。1.2 “Pardon"这一命名本身便蕴含着幽默，虽是表达歉意的单词，但这款字体本身却相当坚持个性。人民币小幅贬值：人民币即期汇率收于7.1984（+57pips)
    """

    sentences = sc.cut_sentences(paragraph)
    print('number of sentences:', len(sentences))
    for sentence in sentences:
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