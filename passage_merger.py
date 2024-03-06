from sentence_cutter import SentenceCutter
import re
# merge QA pair
# merge according to grammar dependency

# 如果一句话中出现以下词语, 则向上合并
MERGE_DICT = ["因此", "因为", "并且", "所以", "但是", "而且", "然而", "可是", "另外", "此外", "其中", "比如", "例如", "上述"]
RE_SHORT_TITLE = re.compile(r'^[\d.]')
SMALL_PARAGRAPH_LENGTH = 500
LEN_SHORT_TITLE = 30


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
                    prev_index = title_index-1

                    new_sentence = reversed_sentences[title_index] + reversed_sentences[prev_index]

                    del reversed_sentences[title_index]
                    del reversed_sentences[prev_index]
                    reversed_sentences.insert(prev_index, new_sentence)

        self.sentences = list(reversed(reversed_sentences))

    def merge_by_small_paragraph(self, passages):
        # 根据换行符拆分
        paras = self.content.split(' ')

        for index, para in enumerate(paras, start=0):
            para = para.strip()
            if len(para) <= SMALL_PARAGRAPH_LENGTH:
                para_sentences = self.sentence_cutter.cut_sentences(para)

                first_sentence = para_sentences[0]
                last_sentence = para_sentences[-1]

                first_sentence_index = passages.index(first_sentence)
                last_sentence_index = passages.index(last_sentence)

                del passages[first_sentence_index:last_sentence_index]
                passages.insert(first_sentence_index, para)

        return passages

    def merge(self):
        self.merge_by_dict()
        self.merge_short_title()
        return self.sentences


if __name__ == '__main__':
    content = "今天天气很好天气很好天气很好. 但是没有风天气很好天气很好天气很好天气很好天气很好. 我很开心天气很好天气很好天气很好天气很好天气很好. 心情也不错. 因为我不想吹风"
    pm = PassageMerger(content)

    passages = pm.merge()
    print(passages)
