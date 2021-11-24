import gensim
#gesim의 Word2Vec 사용
#gesim 사용 하기 위해서 cmd에 pip install gensim 
from gensim.models import Word2Vec 
from kochat.decorators import gensim
@gensim
class Word2Vec(Word2Vec): #Word2Vec 클래스 생성 
    def __init__(self):   #함수 생성, 클래스의 함수를 생성 할떄에는 'self'를 항상 처음에 사용 해야함 

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