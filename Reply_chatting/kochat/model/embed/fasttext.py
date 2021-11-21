from gensim.models import FastText
# FastText를 사용한다면 단어들을 벡터로 표현하는 것과 , 문장분류에 효율적인 학습을 보여줍니다
from decorators import gensim
#decorators를 사용 하여 기존코드에 기능을 추가 한다. 


@gensim
class FastText(FastText): #FastText 클래스 생성 

    def __init__(self):

        super().__init__(size=self.vector_size,
                         window=self.window_size,
                         workers=self.workers,
                         min_count=self.min_count,
                         iter=self.iter)
        #size = 워드 벡터의 특징 값. 즉, 임베딩 된 벡터의 차원.
        #window = 컨텍스트 윈도우 크기
        #min_count = 단어 최소 빈도 수 제한 (빈도가 적은 단어들은 학습하지 않는다.)
        #workers = 학습을 위한 프로세스 수
        #sg = 0은 CBOW, 1은 Skip-gram.
