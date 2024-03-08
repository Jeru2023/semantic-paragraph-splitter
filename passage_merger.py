from sentence_cutter import SentenceCutter
import re
from my_utils import timer
# merge QA pair
# merge according to grammar dependency

# 如果一句话中出现以下词语, 则向上合并
MERGE_DICT = ["因此", "因为", "并且", "所以", "但是", "而且", "然而", "可是", "另外", "此外", "其中", "比如", "例如", "上述", "期间"]
RE_SHORT_TITLE = re.compile(r'^[\d.]')
LEN_SHORT_TITLE = 30
SMALL_PARAGRAPH_LENGTH = 300  # 定义短段落字数
SMALL_PARAGRAPH_SENTENCE_COUNT_LIMIT = 3  # 定义短段落句子数量
SMALL_PARAGRAPH_RE_SPLIT = re.compile(r'(?<=\n)')
SMALL_PARAGRAPH_END_SYMBOLS = re.compile(r'(?<=[?\!…;？！。]|\.(?!\d))')


class PassageMerger:
    def __init__(self, content):
        self.content = content
        self.sentence_cutter = SentenceCutter()
        self.sentences = self.sentence_cutter.cut_sentences(content)

    def merge_by_dict(self):
        sentences = self.sentences
        merged_sentences = []
        current_sentence = sentences[0]

        for i in range(1, len(sentences)):
            sentence = sentences[i]
            if any(word in sentence for word in MERGE_DICT):
                current_sentence += " " + sentence
            else:
                merged_sentences.append(current_sentence)
                current_sentence = sentence

        merged_sentences.append(current_sentence)

        self.sentences = merged_sentences

    def merge_short_title(self):
        """
        以数字开头的小标题，向下合并
        """
        reversed_sentences = list(reversed(self.sentences))

        for index, sentence in enumerate(reversed_sentences, start=0):
            if len(sentence) < LEN_SHORT_TITLE:
                clean_sentence = sentence.strip()
                if RE_SHORT_TITLE.match(clean_sentence):
                    title_index = reversed_sentences.index(sentence)
                    prev_index = title_index - 1

                    new_sentence = reversed_sentences[title_index] + reversed_sentences[prev_index]

                    del reversed_sentences[title_index]
                    del reversed_sentences[prev_index]
                    reversed_sentences.insert(prev_index, new_sentence)

        self.sentences = list(reversed(reversed_sentences))

    def merge_by_small_paragraph(self):
        """
        根据换行符对原content进行拆分成段落列表paragraph_content
        将sentence_cutter之后的sentence与paragraph_content比较，做一下处理：
            paragraph_content小于等于：SMALL_PARAGRAPH_LENGTH或SMALL_PARAGRAPH_SENTENCE_COUNT_LIMIT
            paragraph_content中的sentence，需要进行合并

        本方法主要作用是，对于小段落中的sentences提前进行合并
        """
        content = self.content
        paragraph_content = SMALL_PARAGRAPH_RE_SPLIT.split(content)
        sentences = self.sentences
        merged_sentences = []

        for sentence in sentences:
            if content.strip().startswith(sentence.strip()):
                pass

        for para in paragraph_content:
            para_sent = SMALL_PARAGRAPH_END_SYMBOLS.split(para)
            if len(para) <= SMALL_PARAGRAPH_LENGTH:
                pass
                continue
            if len(para_sent) <= SMALL_PARAGRAPH_SENTENCE_COUNT_LIMIT:
                pass

        # paras = self.content.split(' ')

        # for index, para in enumerate(paras, start=0):
        #     para = para.strip()
        #     if len(para) <= SMALL_PARAGRAPH_LENGTH:
        #         para_sentences = self.sentence_cutter.cut_sentences(para)

        #         first_sentence = para_sentences[0]
        #         last_sentence = para_sentences[-1]

        #         first_sentence_index = passages.index(first_sentence)
        #         last_sentence_index = passages.index(last_sentence)

        #         del passages[first_sentence_index:last_sentence_index]
        #         passages.insert(first_sentence_index, para)

        self.sentences = merged_sentences

    @timer
    def merge(self):
        self.merge_by_dict()
        self.merge_short_title()
        return self.sentences


if __name__ == '__main__':
    content = """>1供给端：本周国内碳酸锂产量较假期有所增加，锂盐厂家陆续开工，治炼厂库存略有累积。多数检修的锂盐厂将于元宵节前后复工，但大部分停产的外购锂矿的中小型锂盐企业表示将根据市场行情择机恢复生产，初步预计2月碳酸锂产量将环比下滑23%至3.2万吨附近。中长期维度看，今明两年是上游锂矿和盐湖放量的大年，碳酸锂供应过剩的压力较大。消息面上，20日晚上市场有关于江西碳酸锂环保停产的传闻传出，后传闻的内容多数被证伪，但锂盐企业表示近期有相关环保回头看活动。周五上午，澳洲锂生产商ArcadiumLithium在财报中显示，因受成本压力影响，Mt Catt1in矿山在2024年的锂辉石精矿产量预期将从2023年的20.5万吨下降至13万吨（减产约9500吨LCE）。
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
本周碳酸锂合约期限结构为contango结构。远月与近月合约的价差整体较上月有所扩大。连一与近月合约的价差3500，较上周增加3150。01、02及03合约之间的价差较小。主力合约与近月合约的价差4200。"""
    pm = PassageMerger(content)

    passages = pm.merge()
    [print(pa_) for pa_ in passages]
