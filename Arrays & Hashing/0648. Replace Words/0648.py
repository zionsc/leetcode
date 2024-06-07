class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        word_dict = set(dictionary)

        sentence_list = sentence.split(' ')
        for idx, word in enumerate(sentence_list):
            for j in range(len(word)):
                if word[:j+1] in word_dict:
                    sentence_list[idx] = word[:j+1]
                    break

        return " ".join(sentence_list)