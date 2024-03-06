from langdetect import detect
from sentence_spliter import spliter
from sentence_spliter.logic_graph_en import long_cuter_en
from sentence_spliter.automata.state_machine import StateMachine
from sentence_spliter.automata.sequence import EnSequence
from sentence_spliter.logic_graph import long_short_cuter
from sentence_spliter.automata.sequence import StrSequence

class SentenceCutter:
    def __init__(self):
        pass

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
            sentences = self.cut_english_sentences(text)
        else:
            return []
        return sentences


if __name__ == '__main__':
    sc = SentenceCutter()
    paragraph = [
        "在很久很久以前......。。... 有座山，山里有座庙啊!!!!!!!庙里竟然有个老和尚！？。。。。",
        "A long time ago..... there is a mountain, and there is a temple in the mountain!!! And here is an old monk in the temple!?....",
        "“我和你讨论的不是一个东西，死亡率与死亡比例是不同的”“你知道么？CNN你们总是制造假新闻。。。”",
        "张晓风笑着说道，“我们这些年可比过去强多了！“过去吃不起饭，穿不暖衣服。 现在呢？要啥有啥！",
        "\"What would a stranger do here, Mrs. Price?\" he inquired angrily, remembering, with a pang, that certain new, unaccountable, engrossing emotions had quite banished Fiddy from his thoughts and notice, when he might have detected the signs of approaching illness, met them and vanquished them before their climax.",
        "Notice that U.S.A. can also be written USA, but U.S. is better with the periods. Also, we can use U.S. as a modifier (the U.S. policy on immigration) but not as a noun (He left the U.S. U.S.A.).",
        "万壑树参天，千山响杜鹃。山中一夜雨，树杪百重泉。汉女输橦布，巴人讼芋田。文翁翻教授，不敢倚先贤。",
    ]
    result = [sc.cut_sentences(para) for para in paragraph]
    print(result)
