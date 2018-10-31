import io
from pdfminer.converter import TextConverter
from pdfminer.pdfinterp import PDFPageInterpreter, PDFResourceManager
from pdfminer.pdfpage import PDFPage
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import matplotlib.pyplot as plt 
import json
import magic
import langid
from xml.etree.cElementTree import XML
import zipfile


class ToiletSink:
    stp_source = ['\u0020', '\u0021', '\u0022', '\u0023', '\u0024', '\u0025', '\u0026', '\u0027', '\u0028', '\u0029', '\u002a', '\u002b', '\u002c', '\u002d', '\u002e', '\u002f', '\u0030' '\u0031', '\u0032', '\u0033', '\u0034', '\u0035', '\u0036', '\u0037', '\u0038', '\u0039', '\u003a', '\u003b', '\u003c', '\u003d', '\u003e', '\u003f', '\u0040', '\u0041', '\u0042', '\u0043', '\u0044', '\u0045', '\u0046', '\u0047', '\u0048', '\u0049', '\u004a', '\u004b', '\u004c', '\u004d', '\u004e', '\u004f', '\u0050', '\u0051', '\u0052', '\u0053', '\u0054', '\u0055', '\u0056', '\u0057', '\u0058', '\u0059', '\u005a', '\u005b', '\u005c', '\u005d', '\u005e', '\u005f', '\u0060', '\u0061', '\u0062', '\u0063', '\u0064', '\u0065', '\u0066', '\u0067', '\u0068', '\u0069', '\u006a', '\u006b', '\u006c', '\u006d', '\u006e', '\u006f', '\u0070', '\u0071', '\u0072', '\u0073', '\u0074', '\u0075', '\u0076', '\u0077', '\u0078', '\u0079', '\u007a', '\u007b', '\u007c', '\u007d', '\u007e']
    stp_universal = ["'", "''", '"', ',', '.', ';', ':', '!', '?', '..', '...', '*', '@', '#', '$', '%', '&', '(', ')', '[', ']', '-', '--', '~', '+', '=', '/', '<', '>', '<<', '>>', '[(', '])', '}', '{', '{[(', ')]}', '\u2019', '\u03b8', '\u03c3', '\u00e9', '\u00ab', '\u00bb', '\u00f3', '\u00e7', '\u00e3', '\u2212', '\u201d', '\u201c']
    stp_en = stopwords.words('english')
    stp_es = stopwords.words('spanish')
    stp_pt = stopwords.words('portuguese')
    stp_fr = stopwords.words('french')
    stp_de = stopwords.words('german')

    # Separate each word as a lowercased element in a list and returns the list.
    def preprocess(self, text):
        tokens = word_tokenize(text)
        tokens = [w.lower() for w in tokens]
        return tokens

    # Identifies the text language and returns its ISO 639-1.
    def identify_language(self, text):
        f = str(text)
        language = langid.classify(f)[0]
        return language

    # Excludes words that occur too frequently and eventual special characters
    # for a specific language.
    def brushing_teeth(self, text):
        wordsFiltered = []
        language = self.identify_language(text)
        if language == 'en':
            for w in text:
                if w not in self.stp_en + self.stp_universal + self.stp_source:
                    wordsFiltered.append(w)
        elif language == 'pt':
            for w in text:
                if w not in self.stp_pt + self.stp_universal + self.stp_source:
                    wordsFiltered.append(w)
        elif language == 'es':
            for w in text:
                if w not in self.stp_es + self.stp_universal + self.stp_source:
                    wordsFiltered.append(w)
        elif language == 'fr':
            for w in text:
                if w not in self.stp_fr + self.stp_universal + self.stp_source:
                    wordsFiltered.append(w) 
        elif language == 'de':
            for w in text:
                if w not in self.stp_de + self.stp_universal + self.stp_source:
                    wordsFiltered.append(w)
        else:
            for w in text:
                if w not in self.stp_universal + self.stp_source:
                    wordsFiltered.append(w)
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
        # In future: most_common_amount = user input
        fdist = nltk.FreqDist(self.brushing_teeth(text))
        fdist_most_common = fdist.most_common(most_common_amount)
        return fdist_most_common
        
    def jasonfy(self, python_object):
        js_on = json.dumps(python_object)
        return js_on

    # The last piece of pie
    def final_cut(self, text):
        # f = " ".join(str(i) for i in text) # This is used for handling txt files as objects as txt files
        f = text
        f = self.preprocess(f)
        f = self.frequency_distribution(f, 20)
        words = [i[0] for i in f]
        freqs = [i[1] for i in f]    
        f_dict = {
            'word': words,
            'freq': freqs
        }
        f = self.jasonfy(f_dict)
        return f

    # Text extraction functions
    def pdf_text_extractor(self, text):
        economist = PDFResourceManager()
        stream = io.StringIO()
        proselitic = TextConverter(economist,stream)
        hermes = PDFPageInterpreter(economist, proselitic)
        with open(text, 'rb') as f:
            for page in PDFPage.get_pages(f, caching=True, check_extractable=True):
                hermes.process_page(page)
            text = stream.getvalue()
        proselitic.close()
        stream.close()
        if text:
            return text

    def docx_text_extractor(self, text):
        WORD_NAMESPACE = '{http://schemas.openxmlformats.org/wordprocessingml/2006/main}'
        PARA = WORD_NAMESPACE + 'p'
        TEXT = WORD_NAMESPACE + 't'

        document = zipfile.ZipFile(text)
        xml_content = document.read('word/document.xml')
        document.close()
        tree = XML(xml_content)
        paragraphs = []
        for paragraph in tree.iter(PARA):
            texts = [node.text for node in paragraph.getiterator(TEXT) if node.text]
            if texts:
                paragraphs.append(''.join(texts))
        return '\n\n'.join(paragraphs)

    def text_extractor(self, text):
        file_type = magic.from_file(text, mime=True)
        if file_type == 'application/pdf':
            return self.pdf_text_extractor(text)
        elif file_type == 'application/msword' or 'application/vnd.openxmlformats-officedocument.wordprocessingml.document':
            return self.docx_text_extractor(text)
        else:
            pass


    



