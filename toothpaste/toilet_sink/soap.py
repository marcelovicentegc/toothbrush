import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import matplotlib.pyplot as plt 
import json


class ToiletSink:
    stp = stopwords.words('portuguese')

    def preprocess(self, text):
        tokens = word_tokenize(text)
        tokens = [w.lower() for w in tokens]
        return tokens

    def brushing_teeth(self, text):
        wordsFiltered = []
        for w in text:
            if w not in self.stp:
                wordsFiltered.append(w)
            else:
                pass
        return wordsFiltered

    def lexical_diversity(self, text):
        textFiltered = self.brushing_teeth(text)
        result = (len(textFiltered) / len(set(textFiltered)))
        return result

    def word_weight(self, text, word):
        textFiltered = self.brushing_teeth(text)
        wrd = [w for w in textFiltered]
        result = (wrd.count(word) / len(set(textFiltered)))
        return result

    def frequency_distribution(self, text, most_common_amount):
        # most_common_amount = user input
        fdist = nltk.FreqDist(self.brushing_teeth(text))
        fdist_most_common = fdist.most_common(most_common_amount)
        return fdist_most_common
        
    def jasonfy(self, python_object):
        # python_object = fdist_most_common
        js_on = json.dumps(python_object)
        return js_on




    



