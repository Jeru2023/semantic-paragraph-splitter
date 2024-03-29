# -*- encoding: utf-8 -*-
from sps import SemanticParagraphSplitter
from passage_merger import PassageMerger
from tag_extractor import TagExtractor
from my_utils import timer
import json


class EmbeddingCutter:
    def __init__(self, text):
        self.semantic_paragraph_splitter = SemanticParagraphSplitter()
        self.tag_extractor = TagExtractor()
        self.passage_merger = PassageMerger(text)
        pass

    @timer
    def cut_paragraph(self, with_tags=True):
        passages = self.passage_merger.merge()
        chunks = self.semantic_paragraph_splitter.split_passages(passages)

        result = []
        for chunk in chunks:
            para_dict = {}
            para_dict["paragraph"] = chunk

            if with_tags:
                tags = self.tag_extractor.extract(chunk)
                para_dict["tags"] = tags

            result.append(para_dict)

        json_str = json.dumps(result, ensure_ascii=False, indent=4)
        return json_str


if __name__ == '__main__':
    #paragraph = "today is a very nice day, i'm feeling good. how about you?"
    content = """
    估值体系切换，消费价值重估。
本文是“消费前瞻专题系列”的第五篇，我们希望用长周期的视角，对中国大消费产业的发展趋势进行前瞻性研究。2022年底本系列推出至今，先从消费宏观周期分析居民去杠杆和人口拐点，判断消费降速和估值调整，此后聚焦商品VS服务的需求结构变迁。随着基本面变革逐步兑现，板块估值亦有明显下行，或许需要重估大消费板块价值。本文结合实际案例讨论消费估值体系，提出估值技术应与产业生命周期相适配，并探讨当前大消费估值水平和投资机会。
匹配产业周期，估值体系切换。证券估值是““二次映射”，次映射定从公司经营到财务表现，一次映射则是市场对基本面的定价。大消费步入成熟阶段，适用的估值体系也将发生变化。我们基于消费投资思考，以：①行业渗透率；净利润增速双重指标刻画产业生命周期，提出与之相结合的估值体系，并以真实案例验证有效性。导入期一一PEG：为成长定价，给梦想买单。导入期企业成长性极强，新产品/新模式/新格局等商业创新引爆渗透率0-1突破，净利润增速可达三位数以上，例如连锁咖啡/医美/MR内容等新兴赛道。买成长股即是买未来，常用PEG方法为成长定价，核心思路是在PE估值中反映成长性，以PEG=1为國值。以2006-2013年的格力电器为例，空调销量在住宅销售增长带动下强劲增长，公司净利润增速平均维持在40%以上，期间最高PE估值突破40X。本文推理了PEG合理性，若业绩符合预期，只要复合增速大于30%（导入期门槛），利润增长将消化估值。成长型标的高风险高收益，难点是准确预测未来增速并承受波动，需紧密跟踪业绩兑现情况，应对市场预期博羿。
一发展期一一PE：长坡+厚雪，复利成长之源。发展期公司已初具规模，行业渗透率提升至30%以上，财务角度看：①净利润增速下滑，15-30%区间，向R0E靠拢；派息率提升，开始稳定分红，例如高端白酒/运动服饰等赛道的龙头白马公司。由“高速成长”转变为“稳健成长”，估值水平会有下调，但复利效应开始显现。稳健成长公司依然有成长，可借鉴PEG思路，以“PE=G=R0E”估值。以2015-2022年的泸州老窖为例，2015年公司开启内部改革、布局高端化，净利润年化复合增速约32%，PE中枢也为30X，利润增长推动市值提升。稳健成长公司风险较导入期明显下降，贯彻“长坡厚雪”理念长期持有收益表现突出，期间需关注行业增长何时见顶及竞争格局。2成熟期一一DDM：类债券估值，高股息收益。当行业走向成熟，渗透率接近100%、市场规模见顶、竞争格局稳固，常见于乳制品/白电/生活用纸/大众服饰等发展较早的行业，随着大消费增速下滑此类赛道大概率增多。主业再投资机会减少时，若公司加大现金分红，财务特征上：①派息率超60%；净利润增速降至10%以下。此时投资回报主要由分红贡献，自由现金流稳定的公司具有类似债券的属性，建议使用DDM方法估值，公司价值是其分红现金流的折现额。以2015年至今的伊利股份为例，作为乳制品绝对龙头，长期维持近25%的R0E。2015年随着行业见顶公司派息率达60%，此后分红现金流稳定，估值随折现率变动，DDM估值结果与股价走势基本一致。成敦公司求长地求限，纪权地杭报丝业纯+现金政求投资口报，扰以公经币投资，报他了具东验作址丝低风验加会。
消费已经低估，存系统性机会。当前市场交易价所反映的增长预期已经低于潜在长期增速，2023年底中证必选、?中证可选隐含长期增速g分别为3.2%、1.0%，明显低于3.1%的长期增速水平，大消费板块整体处于低估区间。风险机遇并存，关注两条主线。悲观情绪导致的低估值是机会根源，风险与机遇并存。建议区分市场波动和估值中枢下行，重点关注错误定价机会：1）估值修复，超跌的龙头公司；2）价值发现，稳健高股息标的。
风险提示2市场波动风险、消费需求增长不及预期、公司经营风险。
国金证券三口LINK SECURITIES扫码获取更多服务。
中国消费行业已迈过高速成长期进入高质量发展阶段，我们2022年底开始在消费前瞻系列专题中对需求端的周期切换已多有论述。随着基本面角度成长性减弱，消费板块估值体系或将发生变化。塞斯·卡拉曼曾说：“价值投资是一门以低于当前潜在价值买入证券，并持有至价格反映价值时的学科”。我们认为万物都应该有一个合理价，尽管其多数时间隐藏在幕后，但刻画价值线可以为投资提供一个相对客观、外在的“锚”。
本文重点讨论消费板块估值体系，提出估值技术使用应与产业生命周期相适配，结合历史案例讨论三类估值方法，并分析当前大消费估值合理性和投资机会。
1、消费需求展望，去杠杆的中场。
证券估值本质要解决的是“二次映射”的问题，其中一次映射是从公司经营到财务表现，二次映射则是市场对基本面的定价。基本面分析是估值的起点，对于中国消费板块而言，过去十余年最大的趋势是“消费升级”，居民部门在经济增长、地产繁荣驱动下扩大需求，成就了一批大牛股。然而，基本面变化往往也是估值方法切换的动因，既有2016年后消费白马为代表的核心资产崛起，也有2021年后整体增速中枢下滑后的向下调整。
我们在2022年12月4日发布的《消费前瞻专题（一)：从杠杆率趋势看消费周期如何演绎》中曾经判断，参考日本历史经验，若中国也开启缩表周期，或将面临：5-10年维度的消费市场“新常态”，反映为社零增速中枢的趋势性下调。
市场中长期预期调整带来的估值中枢调整。
站在当前时点，上述判读均已兑现。一方面消费增速已经下一台阶，社零从10%进入5%时代。另一方面板块估值水平也有明显回落，中证消费指数、中证可选指数PETTM分别从2023年初的40X、20X回落到2024年初的25X、15X。
现在的问题在于，估值调整是否准确反映了基本面的变化？我们首先分别从基本面的宏观微观角度分析，结合2023年的新变化，展望未来趋势。
1.1、宏观：楼市依然疲软，去杠杆或难返收入+房价双升，购买力提升根源。消费升级趋势的核心在于居民购买力提升，有钱了自然扩大消费、追求质量。而居民购买力在2010年后的提升原因有二，其一是经济增长带动的居民收入水平提升，其二则是房价上涨带来的财富效应，并且楼市繁荣还会带动居民购房行为和上下游产业链，进一步反映在收入提升之中。
对比社零和居民可支配收入可以看到，2013-2020年期间社零增速明显高于收入增速，而2021年开始则发生逆转。根本变化在于房地产作为居民家庭持有的主要资产，其财富效应在2020年前后由正向扩大转为负向压制。居民加杠杆时代，住房价格稳步上升，创造资本性收入，因此消费总需求加速上升。而到了去杠杆的偿债阶段，部分收入用于还贷，压缩消费需求。
由于中国经济发展过去对地产依赖度较高，因此在分析未来消费需求变化时也应关注地产相关债务带来的影响。
杠杆率高位震荡，扩表意愿未反转。我们曾对走过相似道路的日本1990s进行历史复盘分析债务驱动下的经济模式，并提炼出杠杆率、新增信贷量作为观测指标（具体分析详见我们的《消费前瞻专题系列》)。回到中国，我们可以看到2023年中国居民杠杆率整体维持2020年以来的高位，小幅上升至63%左右的水平。尽管政府已相继出台降低存款利率、放开限购等信贷支持政策，居民贷款买房意愿依然较为低迷，2023全年仅1-3月、9月中长期贷款出现明显环比多增，单月绝对值依然低于公共卫生事件前水平。
住房信贷的疲软，同步反映在楼市。2023全年中国住房销售9.5亿平方米，同比下滑17.3%，已显著低于公共卫生事件前年均15亿平方米的水平。若沿着房地产行业“短期看金融，中期看土地，长期看人口”，长期展望又如何呢？可以看到2023年中国出生率继续下探到6.39%0，年度总人口下滑208万，均为历年来最低水平。新生人口是未来的购房主力，若生育率持续下滑，远期楼市需求也将面临较大压力。
综合来看，除了债务周期正在迈过拐点，中国似乎也迎来了人口拐点，少子化、老龄化的预期或许也在逐步兑现（详见我们的《消费前瞻专题（二)：从人口结构展望消费需求变迁》)。中国消费市场近年来面临的是综合性问题，加杠杆模式见顶、人口红利开始消退，从量、价层面看需求进一步扩张的动能都有所减退。其他诸如通胀率、消费意愿、PMI等指标也都显示出短期内消费动力不足的信号。
但值得强调的是，增速放缓不意味着不增长。相比日本1990s的情况，我国当前人均收入水平、经济总量都还有较大增长空间。经济模式的相似性使得两国阶段性呈现相似特征，但中日之间在资源票赋、产业链完整度、全球地位上有明显不同，展望长期美国或许才是更好的对照组。
消费增速放缓，寻找新的未来中枢。结合前文判断，我们认为2024年往后5-10年，中国消费增速会在下一台阶后进入新一轮稳定增长期，但新的增速中枢尚未探明，或许会落到3-4%左右。
1长期视角下，增速中枢下降已成定局。回顾过去，2010年之前社零平均增速在15%以上，2013年后逐渐进入10%时代，而2020年后已进入5%时代。增速降档既有周期切换的原因，也是行业走向成熟必然会经历的过程。
眼下的关键，是确定新的中枢是多少？对需求降速的“方向”预判已经被市场定价，而“幅度”的预判还不清楚，这也是决定消费板块市场底的关键。我们逐月计算了2021-2023年单月社零年化复合增速来辅助判断新中枢水平。2023年年初和8月曾触及高点5%，而11月则触底达到1.7%，相应带动了市场预期的大幅起落。整体来看，全年累计增速约3.4%。
考虑到2023年是公共卫生事件放开后第一年，居民消费意愿、市场预期出现大幅扭转，可能会过度反应，因此新中枢或许会略高一些，我们大胆预计在4%左右。
宏观消费需求的变化，在微观行业上也能找到对应线索。消费升级时代，全民购买力提升扩大消费需求，真正在起作用的是“价”而非“量”。随着周期逆转进入偏紧缩阶段，“性价比”偏好流行，消费品和服务的提价空间大幅减小，相应的企业毛利率承压、销售费用增加，最终会导致未来盈利预测下调。
对于未来3-5年的中期展望，在最终买单的消费者未能修复其消费能力之前，我们判断消费品企业利润率可能不会有明显提升。部分议价能力强的企业或许可以通过产业链利润调节向下游经销商要利润，但多数企业的价格竞争压力在存量市场会加剧。
量：渗透率早已打满，2013年接近顶峰从历史复盘角度看，尽管2013年是“全国城乡住户调查一体化”的第一年，城乡统筹发展和收入分配改革开始推进，消费升级浪潮也逐步启动，但主要消费品的产业销量渗透率实际已经打满。
必选消费板块，2013年白酒、啤酒、乳制品、调味品的理论渗透率分别达到了90%、100%、87%、约80%，普及和市场教育在2000s已经完成，其中酒精消费在此后甚至出现了持续下滑，可见“年轻人都不喝酒”或许并非空穴来风。
可选消费板块，整体渗透率达峰更早，1990s彩电、冰箱、洗衣机均已达到80%+，2013年均已达到100%。发展稍晚的空调、汽车则在2017年相继达到100%的渗透率。
由此可见，量的作用并非是推动消费升级的核心。当然其中需要排除：1）新兴品类（小家电、新式茶饮、潮玩等）开拓出的蓝海市场；2）个别公司通过市占率提升也能实现量价齐升，但那更多是来自于竞争格局层面的变化。
一价：利润率水平提升，公司盈利增长之矛社零一般被视作观察消费景气度的核心指标，但对消费板块基本面的解释力在过去十年存在一些问题。例如2014-2017年社零增速不断下滑，但中证消费指数净利润增速持续改善，社零并未及时反映出基本面向好的变化，在增速变动方向、幅度上都不一致。
其中问题在于社零更多是作为大消费行业终端销售指标，而忽略了：1）渠道库存；2）利润率对上市公司报表端的影响。
消费升级带来的最大变化反映在消费品企业利润率的改善，必选消费品纷纷开启提价高端化，而可选消费品随着国货崛起由代工转向做品牌（具体分析详见我们的行业联合专题《国货崛起下半场，寻找未来冠军品牌》)。2014年开始，中证消费指数净利润率进入提升通道，从7.9%一路提升至2020年的15.7%。
我们对社零指标结合利润率指标进行修正，得到如下图所示新的景气变动指标，可以更好的拟合消费行业景气的变化。在考虑了净利率变化后，模拟值与行业真实净利润增速在方向变化上已经高度一致，并且2016-2020年在增速绝对值上也相当接近。剩余的差异主要由行业渠道库存波动所导致，例如2013-2015年行业库存去化压力较大，因此模拟出的净利润增速高于真实净利润增速。
综合以上对量价维度的分析可以看到，利润率改善是大消费板块过去盈利高增长的核心驱动。而在当前时点，宏观层面居民购买力承压和信心不足已经传导至微观，价格压力较大、消费者信心不足，因此消费升级趋势短期内或许趋缓。
2、适应时代变迁，估值体系切换。
证券估值的第二步，在于从基本面信息给出估值数字。长期跟踪一个公司，可能见证其“导入-发展-成熟-衰退”的生命周期。这种由新兴到成熟的发展规律不会变，但不同阶段公司的成长速度、发展特征都有很大差异。终局揭晓之前未来晦暗不明，适用的估值方法也应有所不同。此外市场预期的波动也会带来对终局展望的变化，放大短期波动。在估值体系切换的边际时点，市场对同一家公司的定价可能发生巨大变化。因此识别产业周期、选择最合适的估值技巧是证券估值的重点。
如果把中国大消费看作一个行业，自1978年改革开放以来已有46年，居民消费总额从不足2000亿元上升至2023年的近47万亿元，增速也从早期的双位数逐步回落至个位数，画出一条完美的行业增长曲线。日本战国大名织田信长常颂：“人生五十年，如梦又似幻。一度得生者，岂有不灭者乎？”。2024年起消费行业整体已经进入成熟发展阶段，增速下行大势所趋，因此适用的估值体系也势必发生变化。
下面我们将基于消费投资思考和真实案例，提出与产业生命周期相结合的估值理论体系。
2.1、估值方法纵览，匹配产亚周期估值是一门艺术，但也有部分科学的成分。要选择最合适的估值方法，首先需要划分公司/行业所处发展阶段。我们以一个理想化的、只经营单一业务的初创公司/行业为例，大致可分为：导入期：新技术/新模式等商业创新引爆行业渗透率完成0-1的突破，其净利润增速开始大幅增长，平均增速在高双位数至三位数，吸引高风险偏好的新资本进入，例如连锁咖啡/医美/MR内容等新兴赛道。
口发展期：行业渗透率已经超过30%，但需求依然旺盛，具有较大发展空间。公司已经具有可考证的历史财务数据，机构投资者大举进入，持续跟踪行业发展动态。当行业渗透率迈过50%大关，渗透率和业绩增速的二阶导转负，平均增速回落至15-30%区间，市场预期和公司业绩开始颠簸。期间若选对有能力维持长期增长的白马股，例如高端白酒/运动服饰等赛道的龙头公司，长期持有能享受复利回报。
口成熟期：所有讲过的故事基本兑现，行业增速集体下行，进入存量竞争时代，龙头公司继续巩固自身优势。投资者回报开始由前期的股权增值转为现金分红为主，上市公司再投资空间受限转而提高分红比例，低风险偏好、长久期资金可能更为偏好。常见于乳制品/白电/生活用纸/大众服饰等发展较早的行业，随着大消费增速下滑此类赛道大概率增多。
1衰退期：若替代性产品/技术路线出现，行业成为明日黄花开始走下坡路，业绩持续下滑，例如胶卷/罐头食品等。龙头公司谋求多元化或退出市场，资本市场兴趣不再。
在实际应用中，我们建议以①行业渗透率+净利润增速双重指标进行产业生命周期划分，前者逻辑清晰但往往是后验的，后者能看到边际变化但波动性更大。估值的艺术性也隐含在对产业周期的判断上，教条的数字阈值不重要，对行业发展阶段的感知更重要。
问题的关键是，不同阶段公司到底该怎么估值？历数估值技术工具箱，可以分为：1）相对估值；2）绝对估值两大类，二者侧重点不同。2相对估值的核心逻辑在于“appletoapple”的横向比较，根据可比公司估值水平判断目标公司的价值。但其存在两个最大的问题：1）可比公司是否真正“可比”；2)可比估值无法避免随波逐流的问题，板块系统性的高估或者低估可能带来“互相为锚”的问题。
绝对估值以DCF折现为代表，在测算流程上更为精准，也是学术界的主流。但也存在一些缺陷：1）受制于未来的不确定性和信息有限，容易出现“garbagein，garbage out”的问题；2）估值结果敏感性太强，受关键假设影响过大。
估值最终要刻画价值线，相比绝对估值法，可比估值无法摆脱行业β影响的缺陷更大，此估值体系还是应以绝对估值理念为主。为了解决DCF固有的问题，我们采纳其核心理念，谋求有限信息下的“局部次优解”。并结合经验主义的PEG方法，赋予处于不同产业阶段的公司不同的估值方法。
值得提示的是，本文中讨论的公司估值均指长期持有下（至少3年)所能反映的内在价值，隐含“价值回归”假设。中短期内市场交易价格可能偏离内在价值，我们也没有办法对股价走势进行预判，贵贱可以判断，涨跌无法预测。
2.2、PEG：为成长定价，给梦想买单。
处于导入期的企业具有极强的成长性，过往的财务数据参考价值较低，美好的未来蓝图和无限的增长潜力才是市场关注的焦点。大消费板块的高成长企业由于行业属性所致，一般都已实现盈利，因此不需要使用P/S、P/GMV等另类指标。在对成长性定价的估值技巧中，主要有PEG、DCF两大方法。由于成长初期公司未来还停留在想象层面，可参考的财务历史和第三方数据也不足，因此DCF估值的偏差可能较大，更多作为乐观情况下估值上限的参考，PEG相对更为常用。
PEG方法最早由英国投资大师史莱特在《祖鲁法则》中提出，并由传奇基金经理彼得林奇发扬光大。其核心逻辑是对于高成长型公司，合理PE水平应与预期未来增速相关联，从而反映公司成长性。当PEG=1时公司定价相对合理，PEG=0.5时属于低估区间。
PEG方法最重要的贡献是提出“对于成长股，PE应当反映未来成长性”，这与DCF估值中对未来现金流预测后再折现的理念不谋而合。买成长股是买未来，必须考虑未来成长空间。
但是PEG方法给出的估值参考值0.5、1.0并未有严格的数学证明，因此也常被垢病。我们认为其隐含了两个关键假设：1）公司将在3年后进入成熟发展阶段。2）成熟期合理PE估值在15XPE左右。
若增速G代表预期未来3年复合净利润增速，当下按照PEG=1.0进行估值，且未来3年实际净利润增速符合预期。则对于不同的增速G，只要G大于30%（导入期的门槛水平），3年后公司利润增长消化当前高估值，公司的动态PE都会回落至接近15X的水平。
假如PEG=1.0得到的估值结果是正确的，当目前市值计算出的PEG小于1时则为低估，存在获利空间，其隐含的三年期收益率如下图所示。对于PEG=0.5，其隐含的收益率水平约为年化26%。
由此可知，若上述关键假设成立，且增速G兑现，则PEG估值方法给出的结果是有一定合理性的。实际上PEG可以理解为对成长股估值的一种特例，公司成熟期未必是3年、成熟后合理PE也未必是15X。适用性更强的方法应该是预计未来公司市值，再结合当前市值进行判断，达到成熟期的时间、成熟后的估值都是其中的一个参数而已。
结合A股实际案例来看，PEG的隐含假设其实也是有一定依据的。多数行业的高速增长一般很难维持3年以上，可能是产业规律使然，高成长就会吸引新资本进入走向供给过剩。以大消费行业为例，纵览72个细分赛道，能同时满足：1）过去3年净利润年化复合增速大于30%；2）过去3年单年净利润增速都大于10%并不多见。除了化妆品、厨电、白酒、空调等行业能在特定阶段实现长期增长，其他行业多数是昙花一现。增速筛选标准达标的赛道数量占比一般在10%以下，并且每次达标的赛道也不同。
经典案例：2006-2013年的格力电器消费板块成长股投资的一个经典案例是2006-2013年的格力电器，2006年四季度公司单季度净利润同比增速录得141%，开启了从5亿元迈向100亿元的高速成长期。
期间公司净利润增速平均维持在40%以上，估值水平相应也有显著抬升，可以适用PEG估值方法。
从基本面角度分析，格力电器的高增长受益于行业整体上行。2006-2013年，中国空调销量从3000万台/年上升至接近6000万台/年，年均复合增速达到约13%。空调作为地产后周期品种，其爆发与住宅销售的增长高度相关。2006-2013年，中国新房住宅销售面积从5.5亿平米上升至9.8亿平米，同样接近翻倍，年化复合增速约10%。叠加居民收入水平提升和空调家庭渗透率的提升，空调行业高速增长。
根据PEG估值方法，我们分别以：1）当年Wind一致预期；2）后验的真实净利润复合增速作为增速G的模拟，展望时间为3年，每年年末作为交易时点，刻画价值线并进行历史表现回测。
若以PEG=0.5为买入信号，PEG=1.0为卖出信号，可以看到该策略受到增速G的预测质量影响较大：1）基于Wind一致预期情况下，由于市场预期持续性低于成长期格力的真实业绩，始终没有出现PEG=0.5的买入信号，该估值方法低估了格力电器的内在价值。若将买入信号上调至PEG=1.0,2008年、2011年底分别指示买入，持有1年后收益率分别为+123%、-5%。但2008年的买入点是1664点的历史大底附近，且错过了格力2006年开始市值从100亿元上升至500亿元的成长机会。
2）基于真实业绩，策略有效性显著提升。2006年底行业基本面变化时能准确反映公司内在价值的提升，当时格力电器市值96亿元，而PEG方法预测三年后合理市值290亿元，存在3倍空间。2007年年底上证指数从6124的历史高点回落，估值接近PEG=1.0的高点，指示卖出；而到了2008年底公司股价再次跌破PEG=0.5的合理价，指示买入，精准把握了波段机会。2009年末股价回到PEG=0.72的水平，继续持有；2010-2012年公司市值均低于PEG=0.5的水平，可以加仓或者继续持有；2013年末，公司PEG=0.69格力电器增速预期开始下滑，不再符合PEG估值使用条件。
国金证券V LINK SECURITIES扫码获取更多服务。
即便以一年交易一次的低换手率，严格按照PEG估值方法操作，在2006年底到2013计涨幅也有接近17倍，7年复合年化收益率50.4%。同期格力电器市值从2006年底的96亿元上涨至2013年底的982亿元，接近10倍。可见PEG估值方法不仅可以抓住成长股的机会，波段操作也能放大收益。
因此合理估值有赖于对公司业绩增速的准确判断，这也是成长股投资中最难把握的点但若反过来，按照市场估值倒推隐含的增速G的预期，或许能帮助看清当前估值水平。
2）PEG只适用于成长股，即利润增速应大于30%。前文对PEG赋值讨论时已提到，PEG通过高成长消化高估值，若净利润增速低于30%则无法使用，例如不能生搬硬套给5%利润增速的公司5XPE。
对于格力电器而言，PEG估值合理性在2013年后显著下降，根本原因在于公司滚动3年预期净利润复合增速已经显著下滑，2013-2017年均复合增速约20%，2017年后下滑至10%以下。而2013-2017年公司市值从982亿元上升至2629亿元，但按照PEG估值方法并未给出买入信号。
2.3、PE：长坡+厚雪，复利成长之源。
经过高成长期的迅速发展，公司已初具规模，产品得到认可、商业模式跑通、建立起稳定的管理体系。行业渗透率显著提升后，公司的风险收益特征随之发生改变，相应的市场关注重点会逐步从短期业绩增速超预期幅度向成长期持续时间的超预期转变。财务角度看，主要有两点变化：1）净利润增速下滑，15-30%区间，逐步向R0E靠拢；2）公司派息率提升，20-50%区间，开始有稳定分红。在此阶段，公司由“高速成长”转变为“稳健成长”，尽管增速下滑带动估值水平相较于前期有所下调，但净利润持续成长带来的复利效应使得Buyandhold策略下能收获大量回报，往往这也是盛产投资大师的阶段。常说的“长坡厚雪”选股标准即是寻找能将复利效应发挥到极致的赛道，其中“长坡”是指成长性持续时间要长，“厚雪”则是公司ROE或行业规模天花板要高。
稳健成长期公司的投资回报主要由股价增长提供，因此估值也聚焦在股权定价。假定PE估值水平不变，股价涨幅相当于净利润增速。关键问题在于，一方面成长持续时间较难预测，需要结合行业渗透率展望市场“终局”；另一方面，公司PE水平即便已经回落，但依然需要给出一个具体数字才能完成绝对估值。
在极端假设下，如果公司净利润不增长，持有股权的隐含收益率近似于市盈率的倒数(1/PE)。从机会成本角度看，长周期维度下，所有股票的收益率都应该逐步趋同而没有套利空间，即PE估值水平都会趋于一致。瑞士信贷（CreditSussie）曾统计全球资本市场1900年至2022年的长期表现，复合收益率约为5.0%、算术平均收益率约6.5%，对应PE估值则为15-20XPE。我们认为这一水平与市场经验相一致，对于稳健成长阶段的公司，其PE估值也应在此基础上进行调整。
结合A股市场实际情况看，不同公司之间的净利润增速、ROE水平存在显著分化。V2018-2022年为统计区间，全市场R0E在0-50%之间的公司有4458家，加权平均R0E约13.9%，标准差为8.4%。考虑到公司之间成长性存在差异，因此不能简单的赋予所有稳健成长型企业相同的PE估值，而必须进行合理调整。
稳健成长型公司依然有着成长属性，因此在估值方法上仍可借鉴PEG思路，在模型使用上有两点调整：1增速G=ROE。正如“树不会长到天上去”，30%以上的高净利润增速不可长期持续，但高ROE可以维持。当公司进入稳定成长期后，在没有额外融资情况下净利润增速会朝着ROE回归，并在此水平波动。在估值时我们先判断公司未来能维持的ROE水平，并以此作为预期增速中枢。
2）增速G=PE。为了在估值中体现出不同公司成长性因素差异，将增速G与PE水平挂钩，高增速公司给更高的估值水平。此项类似于选择PEG=1.0作为合理估值的國值，由于稳健成长期企业风险水平相较于高速发展期已有显著下降，因此不再以PEG=0.5为买入水平。
综合来看，我们以“PE=G=ROE”作为关键公式，对稳健成长型公司进行估值。
回顾泸州老窖净利润增速的变化，自2015年实现底部反转后，2016年起增速下滑至30左右，向ROE水平靠拢。得益于净利率持续提升，公司稳态ROE水平不断上升，因此推动稳态净利润增速上升，直至2020年基本达到增速G=R0E的水平。
在此期间，公司一直维持了接近30XPE的估值水平，股价年化涨幅35.2%，而净利润年化增速约32.1%。若对股价增长进行归因拆分，公司在7年间净利润持续增长带来的复利效应是主要驱动因素，这与上文我们对稳健增长型企业的投资价值判断相一致。
同样的我们利用同一估值技巧，分别基于Wind一致预期和公司真实业绩对泸州老窖进行估值，以PE=ROE（即PEG=1.O）为买入信号，卖出信号定为PEG=2.0，在市场过度高估前一直持有公司以享受复利回报。
在稳健增长型公司估值中，对未来的判断依然会影响估值结果准确性，这与公司的成长属性相关：1）基于Wind一致预期情况下，我们以滚动三年ROE作为对增速G的预期，相信公司3年后净利润增速将与稳态R0E相靠拢。结果显示除了2014年底给出买入信号、2015年提示卖出外，期间收益率32.8%，此后该估值方法下并未提示买入。而泸州老窖的市值从2014年底的286亿元上升至2022年底的3301亿元，错过了十倍股的机会。2）基于实际业绩情况下，我们以4年后的ROE水平作为对增速G的预期，回测表现显著提升。按照估值结果显示，分别在2014、2018年底两次提示买入加仓，期间一直建议持有，直至2020年底首次触发卖出信号，并在2021年继续保持卖出信号躲开了抱团破灭的下杀。若按照模型提示交易，则2014-2020年底实现累计上涨10.6倍，年化收益率约50.4%。
可以看到对未来终局展望的准确性会影响稳健增长型企业估值结果，Wind一致预期低估了泸州老窖未来成长空间，给出过低的估值因而错过了十倍股的买入机会。
上述“PE=G=ROE”的估值方法同样有其局限性：1）要求有成长性，不适用于低增速公司。稳健成长型企业依然带有成长属性，持续增长带来的复利效应是投资追求的核心，而当增速过低时则无法满足这一条件。理论状态下，公司ROE趋于稳定时的净利润稳态增速G为ROE*（1-派息率)。要维持一定净利润增速，必须有较高的ROE或限制派息率水平，因此对适用公司的范围也做出限制。
2）忽视分红收益，未完全反映公司价值。股票投资回报由股权增值和现金分红两部分构成，当公司处于高速成长期往往不会分红，稳健成长期的分红回报相比于股权增值也不够突出。但是当公司增速放缓，尤其是开始提高派息率后，现金分红的重要性不容忽视。在对公司成长性进行估值的体系中，并未考虑分红收益以及分红再投资收益，未完全反映公司价值。
经我们测算，当派息率超过60%后，即便高R0E的成长型企业其投资回报也开始以现金分红为主，因此不再适用该估值方法。
花有重开日，人无再少年。当行业走向成熟，市场规模达到顶峰、竞争格局稳固，公司讲过的故事都已兑现。终局到来最大的影响是“再投资”机会减少，上市公司无法在传统市场中找到新的机会，此时面临三种选择：1）跨行业投资，走多元化路线，但要承担跨界的风险；2）投资于金融理财产品，收益率较低往往会导致资源低效配置，拖累公司ROE水平；3）现金分红/股份回购，将多余的现金返还给股东。
是否分红并不意味着对股东的好与坏，而体现公司管理层资源配置的能力。从利润最大化角度考量，若不能维持原有ROE水平则应将现金返还给股东。若公司选择了提高现金分红或股份回购，则财务特征角度可以看到：1）派息率显著提升，往往到60%以上；2）净利润增速放缓，一般在10%以下。
此时持有公司的投资回报主要由现金分红所贡献，由于净利润增速放缓、股票估值水平一般较低使得股权增值空间有限。相比成长阶段，公司在成熟期的业绩可预测性和经营风险已经显著下滑，因此公司未来自由现金流相对比较稳定。对于消费品公司而言，已经筑起竞争壁垒的龙头公司股票在现金流特征上已经具有类似债券的属性：1）现金流可预测性较强；2）“违约风险”远低于成长期公司股票；3）股价波动率显著收窄。
买入成熟期公司，相当于买入一个稳定的现金流。对于此类公司，我们建议使用DDM方法进行估值，公司价值主要是其创造的分红现金流的折现金额。相比DCF方法，DDM的估值结果更为保守，因为自由现金流FCFE/FCFF还包含了公司留存的部分，但二者对于成熟期公司差别不明显，并且分红稳定政策下分红现金流的可预测性相对更强。因此DDM的估值结果可以作为价值评判的下限，而DCF的估值结果可以视作上限。
在应用层面，需要从两个层面思考：）现金流，公司创造。重点关注公司的ROE和派息率（Payoutratio)，决定了公司创造现金流的能力。公司ROE越高，代表其竞争力越强，更能创造现金流，但要关注后续是否会出现调整。派息率则决定了公司现金流分布，派息率越高则更多的利润以现金形式返还给了投资者。
在对现金流进行估计时，我们预测未来十年的表现，而对永续增长部分假定增长率为2%，与通胀水平相近。
2）折现率，随波逐流。公司价值由现金流折现得到，我们采用CAPM模型估计公司的股权资金成本，Re=Rf+β*(Rm-Rf)。从概念上理解，折现率又可以拆解为无风险利率、市场风险溢价和风险偏好三部分，折现率和公司价值反向变动。
经典案例：2015年至今的伊利股份成熟价值股的代表是2015年之后的伊利股份，作为中国乳制品行业的绝对龙头，公司建立了从供应链、产品到渠道的全面优势，长期维持接近25%的净资产收益率。但由于乳制品行业经过长期发展后迎来天花板，公司在2010年起就逐步提高了派息率，到2015年已经达到60%,2017年至今维持70%的水平。因此公司净利润增速与R0E出现背离，2015-2022年净利润复合增速约10.7%。
伊利股份的发展受制于中国乳制品行业整体的进程，2015年前乳制品行业规模维持双位数增长，乳品消费习惯普及带来量增驱动。而随着人均消费量在2015年达到20.1千克/年的高点，行业理论渗透率已经达到91%的高位，行业迎来拐点。价格层面，乳制品提价空间一般，2015-2019年乳制品均价由13.2元/千克提升至15.6元/千克，年化涨幅约6.8%因此伊利股份的净利率也长期维持在8-9%左右。
由于公司已经进入成熟期，其经营相对稳定，因此股利现金流可以较为准确的预测。基2015年底视角，我们不妨假设公司未来R0E均值25%、派息率70%，预测未来现金股利现金流。从事后检验来看，预测值与伊利股份实际派发的股利基本一致。这再次证明了当公司走向成熟期，其“类债券”的属性越发凸显，背后是行业规模见顶和竞争格局趋于稳固。
我们基于历史数据对DDM估值有效性进行回测，其中：>）股权折现率基于CAPM得到。以十年期国债收益率为无风险利率、万得全A指数为市场参考、B值以过去3年周度回报率测算。
2）公司股利现金流基于公司实际ROE和派息率预测。由于成熟期公司业绩波动较小，Wind一致预期ROE和实际ROE接近，因此不再分别回测。
从估值结果上可以看到，2015年以来市场对伊利股份的定价一定程度反映出DCF估值理念，DDM估值结果与市场实际成交价走势基本一致。若按照模型结果进行交易，2016年买入、2017年卖出，此后在2018年买入并持有至2021年卖出，2022年无买入信号。期间累计上涨3.5倍，2015-2021年的年化复合收益率约23.2%。
同时有别于成长股能走出独立行情的特征，伊利股份的估值更多呈现“随波逐流”的特征当无风险利率下行或市场整体回报率下行时，公司理论估值水平抬升，股息率下行。由于折现率中市场回报率影响更大，因此可以简化理解成熟型公司为市场整体表现的反向指标“牛市”市场回报率高-折现率高-成熟公司估值低；“熊市”市场回报率低-折现率低-成熟公司估值高。
从资产配置角度看，成熟公司由于业绩确定性强、以现金形式分红，因而具有较强防御性。
当市场整体表现较好时，不仅合理估值下行，随着资金流向高收益投资标的，高分红公司往往会进入低估，反映为实际股息率高于理论股息率；而当行情逆转时，对安全性的追求导致该类公司快速实现价值修复并达到高估状态，股息率也会显著低于合理水平。
当然DDM估值同样存在一些缺陷，可能会影响其应用有效性：>）现金流层面，DDM只对分红现金流进行了估值，默认公司留存部分都是非自由的必要开支，可能会低估公司价值。此外若公司ROE、派息率出现中枢性调整，需要及时调整。
2折现率层面，存在的问题更多。在测算公司股权回报率时，选用不同指数作为市场回报率参考，测算出的市场平均回报和公司β会有较大差异。例如我们分别选择万得全A和沪深300指数进行测算，伊利股份的折现率就会有显著差异，进而影响估值结果。
3、投资建议：低增速时代，消费有机会吗？。
常言道为人有三思，思危、思退、思变。对大消费板块投资而言，2020年板块估值冲顶时应有“思危”意识，关注风险累积；2021-2023年起抱团瓦解、景气下行则应“思退”，降低风险口。而到当前位置，当市场情绪、估值水平再次达到底部则应开始“思变”。
口什么在变？我们认为中国居民消费需求从双位数中高增速向中低增速的切换已成定局，大消费行业已经逐步走向成熟，迈过人口周期、债务周期拐点。反映到行业微观层面，能实现高净利润增速（年均30%+）的企业数量或变得更为有限，多数赛道的渗透率已经进入产业发展的中后段，公司的财务特征将会朝着：1）提高分红；2）增速降低转变。此外随着竞争加剧，市场份额可能会洗牌，需要关注未来能胜出的龙头公司。
什么不变？其一，基本面角度看。中国消费者对美好生活的需求没有变，只是扩容速度会略放缓，消费需求的韧性是确定的。此外龙头公司建立起的品牌、渠道、供应链等竞争优势也不会变，将继续支持其维持较高的ROE水平。其二，估值角度看。大消费板块经历了估值从高点滑落，当前已经处于低估状态。估值的周期摆动是市场常态，最终会回到合理水平。
3.1、消费已经低估，存系统性机会讨论高估or低估时，必须围绕合理估值展开。我们认为大消费板块存在系统性机会，主要因为估值调整已经过度反映增速下行预期，当前市场交易价所反映的增长预期已经低于潜在长期增速。通过拆解主要消费指数的PE估值决定因素，可以更清楚的看到这一点。
根据DCF估值理念，公司的价值是其未来自由现金流的折现金额。我们作出两点简化假设，以便后续分析：1）长周期视角下，每股自由现金流FCF会和净利润EPS接近；2）公司的自由现金流可以近似为一个以恒定的“全生命周期增速g”持续成长的现金流。
如果把大消费行业看作一个“公司”，则其当前价值可用GordonGrowth模型计算，简单变换后即可得到：PE=1／（r-g)。因此消费行业指数的PE估值仅由：1）当期折现率r;2)全生命周期增速g两个因素决定。
我们基于历史数据和国家政策规划指引，以2050年为行业走向彻底成熟的时点，取2%）永续增长率，大致估算了2001年以来的消费行业全生命周期增速变化。可以看到随着行业日益发展，增速g开始下行，不断逼近永续增长水平。
拆解隐含增速假设，消费板块整体低估。以市场交易价格反映的PE为起点，倒推隐含的长期增速g假设，将之与我们测算的真实长期增速g对比，可以更清楚的看到板块估值水平高低。我们分别选取中证必选、中证可选指数为参考，可以看到历史上2014-2015年、2021-2022年的隐含消费长期增速均显著高于真实水平，相应的消费板块处于牛市；反之2018年隐含增速预期明显偏低，接近零增长或负增长，板块悲观情绪演绎到极致。
从当前水平看，截至2023年底中证必选、中证可选所隐含的长期增速g分别为3.2%、1.0%，前者已接近合理中枢，而后者已经明显低于3.1%的长期增速水平。如果相信常识、相信估值，则大消费板块当前整体处于低估区间，存在左侧机会。
战略层面看，大消费左侧布局机会已经出现；战术层面看，要寻找整体估值调整后的错误定价机会。值得注意的是，2021年开始的估值下调反映的是消费整体增速的下行，该趋势已经明确，当前尚未完全见底，因此基本面不是带来投资机会的核心。相反在不断调整中放大的悲观情绪导致的低估值是机会的根源，因此大消费处于风险与机遇并存的状态，考验投资者的定价能力。
风险：估值体系切换，切忌刻舟求剑公司估值水平变化可能来自于：1）市场波动影响；2）估值体系切换，前者可能在特定时间内围绕估值中枢周期循环，而后者则会导致中枢性下调。所以当前投资消费股最大的风险之一即判断“低估值”到底是来自于市场错误定价还是本身估值就该出现下行，不能简单的拿过去3/5年的PE分位数来断言是否低估。
上文我们分别以格力电器、伊利股份作为案例论述PEG估值、DDM估值有效性。这两家公司历史上都曾随着产业走向成熟，经历过估值体系的切换：1）格力电器在2013年后由于行业销量逐步见顶，业绩增速放缓，估值方法从PEG切到PE，因此PETTM在2013年开始从20X下行到10X；2）伊利股份2015年之前仍处于稳健成长期，适用PE估值，因此PETTM一直维持在25X左右，而2015年后随着派息率大幅提升开始适用DDM估值，合理估值水平反而出现了抬升，与净利润增速开始脱钩。
机遇：龙头估值修复，红利价值发现尽管大消费所处产业生命周期发生了变化，但中国消费者的整体消费规模依然庞大且不断扩张，优秀消费企业的品牌、渠道等综合竞争优势依然稳固。因此只要估值调整到位，依然具有投资价值。过去一段时间估值水平伴随市场情绪恶化一路下调，让部分公司已经进入“击球区”，我们重点建议关注两条投资主线：1）线索一：估值修复，超跌的龙头公司消费行业诸多子行业都已诞生具备强大竞争优势的龙头公司，以白酒板块的贵州茅台为代表，一众“消费茅”企业共同构成板块核心资产。前期机构抱团导致估值突破历史高点，而随着抱团瓦解，部分标的估值已经显著回落。
尽管消费需求增速下行，但以消费50为代表的龙头公司业绩依旧稳健，净资产收益率维持在15%左右，并且市场预期2024-2025年净利润仍有双位数增长。估值下行而业绩继续稳健，超跌的龙头公司存在估值修复机会。
2）线索二：价值发现，稳健高股息标的消费行业走向成熟的另一个特征是公司派息率提升，投资回报中现金分红/回购占比持续提升，高股息标的涌现。在中国经济经历转型，整体增速下行导致利率下行的环境中，高股息资产同样有较好的配置价值。尽管成长性一般，但业绩确定性、现金分红的安全性使其风险收益比表现突出。并且随着成长性机会减少，机会成本角度看高股息标的也会受青睐。
2021年开始，A股红利策略实现明显超额收益，过去3年分别为9.0%、18.3%、11.5%。
我们认为在较早进入成熟期的家电、纺服、轻工行业有大量符合标准的高股息标的，其价值可根据DDM估值方法进行重估。
    """
    ec = EmbeddingCutter(content)
    result = ec.cut_paragraph()
    print(result)
