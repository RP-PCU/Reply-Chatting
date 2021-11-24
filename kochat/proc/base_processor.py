from abc import abstractmethod
from typing import Any

from kochat.decorators import proc
#from * import @  => *에서 @ 불러오기

@proc
class BaseProcessor:
    def __init__(self, model: Any):
        """
        모든 프로세서의 부모클래스입니다.
        모델들의 이름과 파일 주소를 가지고 있고, 다양한 추상 메소드를 가지고 있습니다.
        학습 및 검증 등의 메소드의 이름은 sklearn과 동일하게 설정했습니다.
        :param model: 학습할 모델
        """

        super().__init__()
        self.train_data, self.test_data = None, None
        self.ood_train, self.ood_test = None, None
        self.model = model
        self.model_loaded = False

        # /saved/CLASS_NAME/
        self.model_dir = self.model_dir + \
                         self.__class__.__name__ + \
                         self.delimeter
        #모델의 따라 실제 모델 저장 위치를 제공한다. +\ 줄바꿈을 한다.
        
        # /saved/CLASS_NAME/CLASS_NAME.xxx
        self.model_file = self.model_dir + \
                          self.__class__.__name__

    @abstractmethod   #추상메서드를 나타내는 데코레이터
    def fit(self, *args, **kwargs):
        raise NotImplementedError
    #*args는 여러 개(복수개의)의 인자를 함수로 받고자 할때 쓰임(튜플형식)
    #**kwargs는 딕셔너리 형태로 {'키워드':'특정 값'} 이렇게 함수 내부로 전달됩니다.
    #raise 키워드와 미구현 상태를 표현하는 NotImplementedError 조합해 사용하면
    # "아직 구현하지 않은 부분입니다" 라는 오류를 강제로 발생 시킬 수 있다.

    @abstractmethod
    def predict(self, *args, **kwargs):
        raise NotImplementedError

    @abstractmethod
    def _load_model(self):
        raise NotImplementedError

    @abstractmethod
    def _save_model(self):
        raise NotImplementedError

    def _print(self, msg: str, name: str = None):
        """
        Processor는 내용 출력시 반드시 자신의 이름을 출력해야합니다.
        :param msg: 출력할 메시지
        :return: [XXProcessor] message
        """

        if name is None:
            name = self.__class__.__name__

        print('[{name}] {msg}'.format(name=name, msg=msg))
        #name, msg를 포맷팅해준다.format함수는 인자를 값으로 넣어준다.