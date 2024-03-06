# -*- encoding: utf-8 -*-
from sps import SemanticParagraphSplitter
from sentence_cutter import SentenceCutter
from passage_merger import PassageMerger


class ParagraphCutter:
    def __init__(self):
        self.semantic_paragraph_splitter = SemanticParagraphSplitter()
        self.sentence_cutter = SentenceCutter()
        self.passage_merger = PassageMerger()
        pass

    def cut_paragraph(self, text):
        sentences = self.sentence_cutter.cut_sentences(text)
        passages = self.passage_merger.merge_by_dict(sentences)
        chunks = self.semantic_paragraph_splitter.split_passages(passages)
        return chunks


if __name__ == '__main__':
    pc = ParagraphCutter()
    #paragraph = "today is a very nice day, i'm feeling good. how about you?"
    paragraph = """
    1月M2增速为什么快速下滑？。
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
DR007与DR001利差扩张后收窄至10BP。
"""

    result = pc.cut_paragraph(paragraph)
    for chunk in result:
        print('==============')
        print(chunk)