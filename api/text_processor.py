import nltk
from nltk.corpus import stopwords
from bs4 import BeautifulSoup
import re


class TextPreprocessor:
    REPLACE_BY_SPACE_RE = re.compile('[/(){}\[\]\|@,;]')
    BAD_SYMBOLS_RE = re.compile('[^0-9a-z #+_]')
    STOPWORDS = None

    @staticmethod
    def init():
        nltk.download('stopwords')
        TextPreprocessor.STOPWORDS = set(stopwords.words('english'))

    @staticmethod
    def clean_text(text):
        text = BeautifulSoup(text, "lxml").text # HTML decoding
        text = text.lower() # lowercase text
        text = re.sub(r'\d+', '', text) # remove digits
        text = TextPreprocessor.REPLACE_BY_SPACE_RE.sub(' ', text) # replace REPLACE_BY_SPACE_RE symbols by space in text
        text = TextPreprocessor.BAD_SYMBOLS_RE.sub('', text) # delete symbols which are in BAD_SYMBOLS_RE from text
        text = ' '.join(word for word in text.split() if word not in TextPreprocessor.STOPWORDS) # delete stopwors from text
        text = re.sub('<code>(.|\n)*?<\/code>', '', text)
        return text