# -*- encoding: utf-8 -*-
from ltp import StnSplit
from sentence_transformers import SentenceTransformer
import numpy as np
from sentence_cutter import SentenceCutter

BGE_LARGE = 'BAAI/bge-large-zh-v1.5'
BGE_M3 = 'BAAI/bge-m3'
LOCAL = '/Users/liujeru/.cache/huggingface/hub/models--BAAI--bge-m3/snapshots/3641912a2b1366e8ee92fbdad6aa2abd45234114/'
ACGE_LARGE = 'aspire/acge-large-zh'
M3E_SMALL = 'moka-ai/m3e-base'
# If you want more chunks, lower the threshold
THRESHOLD = 95


class SemanticParagraphSplitter:
    def __init__(self, threshold=THRESHOLD, model_path=LOCAL):
        self.threshold = threshold
        self.model = SentenceTransformer(model_path)
        self.sentence_cutter = SentenceCutter()

    @staticmethod
    def combine_sentences(sentences, buffer_size=1):
        # Go through each sentence dict
        for i in range(len(sentences)):

            # Create a string that will hold the sentences which are joined
            combined_sentence = ''

            current_length = len(sentences[i]['sentence'])
            # Add sentences before the current one, based on the buffer size.
            for j in range(i - buffer_size, i):
                # Check if the index j is not negative (to avoid index out of range like on the first one)
                if j >= 0:
                    # Add the sentence at index j to the combined_sentence string
                    combined_sentence += sentences[j]['sentence'][-current_length:] + ' '

            # Add the current sentence
            combined_sentence += sentences[i]['sentence']
            print('----------')
            print(current_length)
            print(combined_sentence)

            # Add sentences after the current one, based on the buffer size
            for j in range(i + 1, i + 1 + buffer_size):
                # Check if the index j is within the range of the sentences list
                if j < len(sentences):
                    # Add the sentence at index j to the combined_sentence string
                    combined_sentence += ' ' + sentences[j]['sentence'][:current_length]

            # Then add the whole thing to your dict
            # Store the combined sentence in the current sentence dict
            sentences[i]['combined_sentence'] = combined_sentence

        return sentences

    def build_sentences_dict(self, sentences):
        indexed_sentences = [{'sentence': x.strip(), 'index': i} for i, x in enumerate(sentences)]
        combined_sentences = self.combine_sentences(indexed_sentences)

        embeddings = self.model.encode([x['combined_sentence'] for x in combined_sentences], normalize_embeddings=True)

        for i, sentence in enumerate(combined_sentences):
            sentence['combined_sentence_embedding'] = embeddings[i]

        return combined_sentences

    @staticmethod
    def calculate_cosine_distances(sentences):
        distances = []
        for i in range(len(sentences) - 1):
            embedding_current = sentences[i]['combined_sentence_embedding']
            embedding_next = sentences[i + 1]['combined_sentence_embedding']

            # Calculate cosine similarity
            # similarity = cosine_similarity([embedding_current], [embedding_next])[0][0]
            similarity = embedding_current @ embedding_next.T
            # Convert to cosine distance
            distance = 1 - similarity

            # Append cosine distance to the list
            distances.append(distance)

            # Store distance in the dictionary
            sentences[i]['distance_to_next'] = distance

        # Optionally handle the last sentence
        # sentences[-1]['distance_to_next'] = None  # or a default value

        return distances, sentences

    def calculate_indices_above_thresh(self, distances):
        breakpoint_distance_threshold = np.percentile(distances, self.threshold)
        # The indices of those breakpoints on your list
        indices_above_thresh = [i for i, x in enumerate(distances) if x > breakpoint_distance_threshold]
        print('indices above thresh', indices_above_thresh)
        return indices_above_thresh

    @staticmethod
    def cut_chunks(indices_above_thresh, sentences):
        # Initialize the start index
        start_index = 0

        # Create a list to hold the grouped sentences
        chunks = []

        # Iterate through the breakpoints to slice the sentences
        for index in indices_above_thresh:
            # The end index is the current breakpoint
            end_index = index

            # Slice the sentence_dicts from the current start index to the end index
            group = sentences[start_index:end_index + 1]
            combined_text = ' '.join([d['sentence'] for d in group])
            chunks.append(combined_text)

            # Update the start index for the next group
            start_index = index + 1

        # The last group, if any sentences remain
        if start_index < len(sentences):
            combined_text = ' '.join([d['sentence'] for d in sentences[start_index:]])
            chunks.append(combined_text)

        return chunks

    def split(self, text):
        single_sentences = self.sentence_cutter.cut_sentences(text)
        print(f"{len(single_sentences)} single sentences were found")
        chunks = self.split_passages(single_sentences)
        return chunks

    def split_passages(self, passages):
        combined_sentences = self.build_sentences_dict(passages)
        distances, sentences = self.calculate_cosine_distances(combined_sentences)

        indices_above_thresh = self.calculate_indices_above_thresh(distances)
        chunks = self.cut_chunks(indices_above_thresh, sentences)
        return chunks


if __name__ == '__main__':
    content = """
    拥抱创新升级、新兴应用及出口市场。 拥抱创新升级、新兴应用及出口市场。 ·自上而下精选优质个股，拥抱创新升级、增量应用及出口市场分子端决定中期方向，港股市场中资股盈利前景背靠中国经济体。 中国经济正在筑底，补库存最大制约为居民部门和企业部门上杠杆意愿弱，复苏力度仍需要观察。 分母端由于海外及本港投资者占据香港市场的主流，港股市场估值定价整体跟踪美联储加息节奏。 美国通胀下行有望放缓，经济韧性可能超预期。
当前政策下的5.25%-5.5%利率区间可能继续维持，我们预计2024年内开启降息周期。 ·互联网存量竞争下布局出海及AI应用，计算机延续AI及华为鸿蒙主线（1）互联网行业基本面兑现稳健，决定互联网板块行情的首要变量仍是宏观环境。 流量见顶背景下，线上广告、电商、本地生活等场景受益顺周期复苏，叠加降本增效释放利润空间。
存量竞争下格局稳定和壁垒较强的公司业绩确定性更强，中长期增量来自出海及AI应用。 推荐拼多多；受益标的腾讯控股。 （2）SaaS作为长久期资产，有望受益于美债利率下行、享受板块性估值显著扩张。 AI及华为鸿蒙生态有望延续主线行情，以AI办公工具为代表的AI应用生态逐步繁荣，AI办公工具进入商业化初期，有望提升付费用户渗透率及ARPU。 推荐金山软件、浪潮数字企业；受益标的金蝶国际、中国软件国际、美图公司、阜博集团。 ·汽车销售回暖叠加新车周期驱动板块估值修复，拥抱汽车智能化及汽车出口2023Q4各家车企陆续发布无图ADAS，2024年由小鹏汽车率先实现国内城市NGP更新，有望带来ADAS在用户端形成正向反馈，从而驱动智驾版车型销量提升、以及软件订阅利润提升。 2024年中国新能源汽车销量增速或放缓，竞争格局持续胶着，各家车企加速汽车出口战略，零跑汽车和Stellantis合作的海外出口轻资产模式较佳，有望复用Stellantis渠道资源及品牌影响力助其加速海外拓展。 2024年3月国内汽车销售有望逐步回暖、配合新车产品周期启动，驱动整车板块整体估值修复，推荐理想汽车、小鹏汽车；受益标的零跑汽车。 电子：半导体关注格局更优环节，消费电子布局AI、XR、钛合金等创新升级（1）半导体行业仍处在基本面复苏的起点，下游IC设计客户处在低库存状态，晶圆厂产能稼动率有望逐步企稳。
先进制程产能具备稀缺性，成熟制程业务或呈现量增价减趋势。 建议关注中芯国际、华虹半导体。 （2）手机及PC行业目前已基本完成去库存，后续有赖于AI、钛合金及XR等创新升级驱动更大业绩弹性。 PC和手机终端下一个创新周期集中于AI，AI手机短期内缺乏创新切实应用，我们预计苹果iOS生态的AI交互体验有望更优；而AIPC创新应用关注办公软件及AIPC本地化AI模型进展能否激活PC换机周期。 推荐联想集团、比亚迪电子、高伟电子，建议关注小米集团。"""

    sps = SemanticParagraphSplitter(threshold=95)
    #print(sps.cut_sentences(content))

    chunks = sps.split(content)

    for i, chunk in enumerate(chunks):
        print(f"Chunk #{i}")
        print(chunk.strip())

    print('end')
