from torch import Tensor
from torch import nn
from torchcrf import CRF

from decorators import entity
from loss.base_loss import BaseLoss
#from * import @  => *에서 @ 불러오기

@entity
class CRFLoss(BaseLoss):

    def __init__(self, label_dict: dict):
        """
        Conditional Random Field를 계산하여 Loss 함수로 활용합니다.
        :param label_dict: 라벨 딕셔너리
        """

        super().__init__()
        self.classes = len(label_dict)   #label_dict 길이를 받아온다.
        self.crf = CRF(self.classes, batch_first=True) #batch_first=True일 시 배치 차원를 맨앞으로 하여 데이터를 불러옴
    def decode(self, logits: Tensor, mask: nn.Module = None) -> list:
        """
        Viterbi Decoding의 구현체입니다.
        CRF 레이어의 출력을 prediction으로 변형합니다.
        :param logits: 모델의 출력 (로짓)
        :param mask: 마스킹 벡터
        :return: 모델의 예측 (prediction)
        """

        logits = logits.permute(0, 2, 1)
        return self.crf.decode(logits, mask)

    def compute_loss(self, label: Tensor, logits: Tensor, feats: Tensor, mask: nn.Module = None) -> Tensor:
        """
        학습을 위한 total loss를 계산합니다.
        :param label: label
        :param logits: logits
        :param feats: feature
        :param mask: mask vector
        :return: total loss
        """

        logits = logits.permute(0, 2, 1)
        #crf_loss 에 넣기 위해서 (T,N,C)로 변환 차원을 맞바꾸는 것인데 0번지의 차원,2번지의 차원, 1번지의 차원
        #transpose()와 비슷하지만 transpose()함수는 딱 두개의 차원을 맞교환할수있지만,
        #permute()함수는 모든 차원들을 맞교환할 수 있다.
        log_likelihood = self.crf(logits, label, mask=mask, reduction='mean')
        #reduction='mean'은 출력의 가중 평균이 취해짐, 기본값이 'mean'
        return - log_likelihood  # nll loss