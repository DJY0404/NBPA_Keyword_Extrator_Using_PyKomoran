# https://github.com/lovit/textrank.git 과 PYKOMORAN 문서를 참고함

#PyKomoran을 반드시 다운받을 것! 자바 버전은 1.8이상 일 것. 
#전처리기
from PyKomoran import *
komoran = Komoran(DEFAULT_MODEL['LIGHT'])
#str_to_analyze() =  문장 분석 후 단어 나누고 요소를 붙여준다. 단어/NN 이런식으로.
#txt파일 넣고 전처리하는 부분.
"""with open('./message.txt', encoding='utf-8') as f:
    sents = [sent.strip() for sent in f]
    print(sents)
"""
#txt파일 말고 문장 입력 후 전처리하는 부분.
sents=""# 여기에 글 넣으면됨
a = (komoran.get_plain_text(sents))
file = open('문서이름.txt','w')
file.write(a)
file.close()