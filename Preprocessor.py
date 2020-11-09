# https://github.com/lovit/textrank.git 과 PYKOMORAN 문서를 참고함

#PyKomoran을 반드시 다운받을 것! 자바 버전은 1.8이상 일 것. 
#전처리기
from PyKomoran import *
komoran = Komoran(DEFAULT_MODEL['LIGHT'])

"""with open('./message.txt', encoding='utf-8') as f:
    sents = [sent.strip() for sent in f]
    print(sents)
"""

def preprocess(sents):
    komoran = Komoran(DEFAULT_MODEL['LIGHT'])
    a = (komoran.get_plain_text(sents))
    return a