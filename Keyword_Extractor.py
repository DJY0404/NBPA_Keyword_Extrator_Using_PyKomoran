import textrank
from Preprocessor import preprocess

# # Komoran tokenized La La Land review
# with open('./tutorial/lalaland_komoran.txt', encoding='utf-8') as f:
#     sents = [sent.strip() for sent in f]

# with open('./tutorial/lalaland_komoran.txt', encoding='utf-8') as f:
#     texts = [sent.strip() for sent in f]

# print(len(sents), len(texts))

#N=명사류. 명사류만 추출하는 코드
from textrank import KeywordSummarizer

def komoran_tokenize(sent):
    words = sent.split()
    words = [w for w in words if ('/N' in w )]
    return words

def analyze_keywords(sents):
    
    preprocessed_sents = preprocess(sents)

    sents_arr = []
    for sent in preprocessed_sents.split('\n'):
        sents_arr.append(sent.strip())

    keyword_extractor = KeywordSummarizer(
        tokenize = komoran_tokenize,
        window = -1,
        verbose = False
    )
    #명사류 추출하고 출현빈도 랭크까지 출력.
    print('-------------- 명사 키워드 추출 ------------')
    keywords = keyword_extractor.summarize(sents_arr, topk=50)
    for word, rank in keywords:
        if len(word)>5:
            print('{} ({:.3})'.format(word, rank))

    print('-------------- 모든 키워드 추출 ------------')


    keyword_extractor = KeywordSummarizer(
        tokenize = komoran_tokenize,
        window = 2,
        verbose = False
    )
    keywords = keyword_extractor.summarize(sents_arr, topk=30)
    for word, rank in keywords:
        print('{} ({:.3})'.format(word, rank))

    print('')
    return keywords