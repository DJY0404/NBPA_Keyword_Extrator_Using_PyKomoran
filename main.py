from Keyword_Extractor import analyze_keywords

sample_text = """ 오늘부터 콘센트가 잘 안동작하기 시작했다.
콘센트를 살펴보니 접지가 잘 안되는 것 같다.
그래서 철물점에 가보니 콘센트를 고칠 수 있다고 한다.
"""

def simple_task():
    while(True):
        print('[간단한 키워드 추출 메소드]')
        print('0. 간단한 예제 텍스트 돌려보기')
        print('1. 문장 직접 입력하기')
        print('2. 텍스트파일 지정하기')
        print('q. 종료')
        
        try:
            user_input = input('선택 : ')

            if user_input == 'q':
                return
            
            if user_input == '0':
                sents = sample_text
                keywords = analyze_keywords(sents)

            elif user_input == '1':
                line_cnt = input('몇줄짜리 글입니까? : ')
                print('글을 입력하세요 : ')
                sents = ""
                for s in range(int(line_cnt)):
                    sents += input() + '\n'
                keywords = analyze_keywords(sents)

            elif user_input == '2':
                user_input = input('텍스트 경로를 입력하세요 : ')
                with open(user_input, encoding='utf-8') as f:
                    sents = ""
                    for sent in f:
                        sents += sent + '\n'
                    keywords = analyze_keywords(sents)
        
        except Exception as e:
            print(e)



if __name__ == '__main__':
    simple_task()