from langdetect import detect
import spacy


class SentenceCutterSpacy:
    '''
    依赖spacy: pip install -i https://pypi.tuna.tsinghua.edu.cn/simple spacy
    中文model: python -m spacy download zh_core_web_sm
    英文model: python -m spacy download en_core_web_sm
    '''
    def __init__(self):
        self.nlp_en = spacy.load("en_core_web_sm")
        self.nlp_zh = spacy.load("zh_core_web_sm")

    def cut_sentences(self, text):
        lang = detect(text)
        if lang.startswith('zh'):
            doc = self.nlp_zh(text)
        elif lang == 'en':
            doc = self.nlp_en(text)
        else:
            return []
        return [sent.text for sent in doc.sents]


if __name__ == '__main__':
    # sc = SentenceCutter()
    sc_spacy = SentenceCutterSpacy()
    paragraph = [
        "在很久很久以前......。。... 有座山，山里有座庙啊!!!!!!!庙里竟然有个老和尚！？。。。。",
        "A long time ago..... there is a mountain, and there is a temple in the mountain!!! And here is an old monk in the temple!?....",
        "“我和你讨论的不是一个东西，死亡率与死亡比例是不同的”“你知道么？CNN你们总是制造假新闻。。。”",
        "张晓风笑着说道，“我们这些年可比过去强多了！“过去吃不起饭，穿不暖衣服。 现在呢？要啥有啥！",
        "\"What would a stranger do here, Mrs. Price?\" he inquired angrily, remembering, with a pang, that certain new, unaccountable, engrossing emotions had quite banished Fiddy from his thoughts and notice, when he might have detected the signs of approaching illness, met them and vanquished them before their climax.",
        "Notice that U.S.A. can also be written USA, but U.S. is better with the periods. Also, we can use U.S. as a modifier (the U.S. policy on immigration) but not as a noun (He left the U.S. U.S.A.).",
        "万壑树参天，千山响杜鹃。山中一夜雨，树杪百重泉。汉女输橦布，巴人讼芋田。文翁翻教授，不敢倚先贤。",
    ]
    result = [sc_spacy.cut_sentences(para) for para in paragraph]
    print(result)
