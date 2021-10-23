import gensim
#gesim의 Word2Vec 사용
#gesim 사용 하기 위해서 cmd에 pip install gensim 
from gensim.models import Word2Vec 

@gensim
class Word2Vec(Word2Vec): #Word2Vec 클래스 생성 
    def __init__(self):   #함수 생성, 클래스의 함수를 생성 할떄에는 'self'를 항상 처음에 사용 해야함 

        super().__init__(size=self.vector_size,
                         window=self.window_size,
                         workers=self.workers,
                         min_count=self.min_count,
                         iter=self.iter)