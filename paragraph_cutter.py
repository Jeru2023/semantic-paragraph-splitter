# -*- encoding: utf-8 -*-
from sps import SemanticParagraphSplitter
from passage_merger import PassageMerger


class ParagraphCutter:
    def __init__(self, text):
        self.semantic_paragraph_splitter = SemanticParagraphSplitter()
        self.passage_merger = PassageMerger(text)
        pass

    def cut_paragraph(self):
        passages = self.passage_merger.merge()
        chunks = self.semantic_paragraph_splitter.split_passages(passages)
        return chunks


if __name__ == '__main__':

    #paragraph = "today is a very nice day, i'm feeling good. how about you?"
    paragraph = """
    亚里士多德是古希腊的百科全书，号称万王之王。
他可以说是物理学和许多自然科学学科的开山鼻祖，前人虽然也有研究过这些问题，但亚里士多德最早将对大自然发生的现象和规律的研究变成一些独立的学科，并且将它们从传统的“知识”(哲学)中分离出来。
亚里士多德将过去广义上的哲学分为三个大的领域:
1. 理论的科学，即我们现在常说的理工科，比如数学和自然科学。
2. 实用的科学，即我们现在常说的文科，比如经济学，政治学，战略学和修辞写作。
3. 创造的科学，即诗歌，艺术。

毕达哥拉斯和欧几里得通过演绎法建立起几何学，而亚里士多德则开创了通过归纳法研究科学的先河。但由于认知的局限性，亚里士多德对科学的大多数结论都是定性而非定量的，而且他在物理学上的很多结论都是错的。

完成物理学从定性研究到定量研究这一飞跃的，是阿基米德。
阿基米德被誉为世界三大数学家之一(另两个是高斯和牛顿)，但是他对物理学的贡献和影响其实更加深远。
他的主要发明贡献有浮力定律，杠杆原理(投石机和起重机)，螺旋抽水机
阿基米德发明的超级武器帮助叙拉古对抗罗马军队，但最终被围城后弹尽粮绝，死于罗马士兵之手
    """
    pc = ParagraphCutter(paragraph)
    result = pc.cut_paragraph()
    for index, chunk in enumerate(result, start=0):  # Python indexes start at zero
        print('==============')
        print(index, chunk)
