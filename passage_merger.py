from sentence_cutter import SentenceCutter
# merge QA pair
# merge according to dictionary
# merge according to grammar dependency

# 如果一句话中出现以下词语, 则向上合并
MERGE_DICT = ["因此", "因为", "并且", "所以", "但是", "而且", "然而", "可是", "另外", "此外"]


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

        return merged_sentences

    def merge(self):
        passages = self.merge_by_dict()
        return passages


if __name__ == '__main__':
    content = "今天天气很好天气很好天气很好. 但是没有风天气很好天气很好天气很好天气很好天气很好. 我很开心天气很好天气很好天气很好天气很好天气很好. 心情也不错. 因为我不想吹风"
    pm = PassageMerger(content)

    passages = pm.merge()
    print(passages)
