#os(Operating System)모듈은 운영체제에서 제공되는 여러 기능을 파이썬에서 수행할 수 있게 해줍니다
import os
#time모듈을 사용함으로서 시간 데이터를 다룰수 있습니다.     
from time import time

#딥러닝 도구로서 numpy와 효율적으로 연동을 지원하는 편리한 도구 
import torch
import numpy as np

from gensim.models.base_any2vec import BaseWordEmbeddingsModel
# training중 특정 단계에서 실행/실행해야 하는 callback 목록을 위하여 사용 
from gensim.models.callbacks import CallbackAny2Vec
from torch import Tensor

from kochat.decorators import gensim
#구조 클래스를 처리할 수 있는 클래스에 필요한 구현을 나타내는 추상클래스를 위하여 사용합니다.
from kochat.proc.base_processor import BaseProcessor


@gensim
class GensimEmbedder(BaseProcessor):

    def __init__(self, model: BaseWordEmbeddingsModel): #Gensim 모델의 Training, Inference 등을 관장하는 프로세서 클래스
        super().__init__(model)
        self.callback = self.GensimLogger(
            name=self.__class__.__name__,
            logging=self._print
        )  # 학습 진행사항 출력 콜백

    def fit(self, dataset: list): #데이터셋으로 Vocabulary를 생성하고 모델을 학습 및 저장
        self.model.build_vocab(dataset)
        self.model.train(
            sentences=dataset,
            total_examples=self.model.corpus_count,
            epochs=self.model.epochs + 1,
            callbacks=[self.callback]
        )

        self._save_model()

    #사용자의 입력을 임베딩하며. ,param sequence: 입력 시퀀스 , return: 임베딩 벡터 반환
    def predict(self, sequence: str) -> Tensor:  
        self._load_model()
        return self._forward(self.model, sequence)

    def _load_model(self): # 저장된 모델을 불러오기 위하여 사용 

        if not os.path.exists(self.model_dir):
            raise Exception("모델을 불러올 수 없습니다.")

        if not self.model_loaded:
            self.model_loaded = True
            self.model = self.model.__class__.load(self.model_file + '.gensim')

    def _save_model(self): #모델을 저장장치에 저장 

        if not os.path.exists(self.model_dir):
            os.makedirs(self.model_dir)

        self.model.save(self.model_file + '.gensim')

    def _forward(self, model, sequence: str) -> Tensor:
        sentence_vector = []

        for word in sequence:
            try:
                word_vector = torch.tensor(model.wv[word])
            except KeyError as _:
                word_vector = torch.ones(self.vector_size) * self.OOV

            sentence_vector.append(word_vector.unsqueeze(dim=0))

        return torch.cat(sentence_vector, dim=0)

    class GensimLogger(CallbackAny2Vec):

        def __init__(self, name: str, logging): # Gensim 모델의 학습 과정을 디버깅하기 위한 callback, param name: 모델 이름, 
                                                #param print: base processor의 print 함수를 전달받습니다.
            self.epoch, self.eta = 0, 0
            self.name = name
            self.logging = logging

        def on_epoch_begin(self, model: BaseWordEmbeddingsModel): #epoch 시작시에 시간 측정을 시작합니다.
                                                                  #param model: 학습할 모델
            self.eta = time()

        def on_epoch_end(self, model: BaseWordEmbeddingsModel): #epoch 종료시에 걸린 시간을 체크하여 출력합니다.
                                                                #param model: 학습할 모델

            self.logging(
                name=self.name,
                msg='Epoch : {epoch}, ETA : {sec} sec'
                    .format(epoch=self.epoch, sec=round(time() - self.eta, 4))
            )

            self.epoch += 1
