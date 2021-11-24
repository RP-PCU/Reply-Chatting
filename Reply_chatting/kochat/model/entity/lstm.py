import torch
#torch 사용하기 위해 cmd에 pip install torch
#torch에서 nn, autograd, Tensor 사용
from torch import nn, autograd
from torch import Tensor
from kochat.decorators import entity

@entity
class LSTM(nn.Module):  #LSTM 모델 클래스 생성

    def __init__(self, label_dict: dict, bidirectional: bool = True): 
        """
        Entity Recognition을 위한 LSTM 모델 클래스입니다.
        :param label_dict: 라벨 딕셔너리
        :param bidirectional: Bidirectional 여부
        """

        super().__init__()
        self.label_dict = label_dict
        self.direction = 2 if bidirectional else 1   #if가 bidirectional(양방향)일때 참이면 2 else면 1
        self.lstm = nn.LSTM(input_size=self.vector_size,
                            hidden_size=self.d_model,
                            num_layers=self.layers,
                            batch_first=True,
                            bidirectional=bidirectional)
        #input_size: input의 사이즈에 해당 하는 수를 입력
        #hidden_size:은닉층의 사이즈에 해당 하는 수를 입력
        #num_layers: RNN의 은닉층 레이어 갯수를 나타냅니다. 기본값은 1
        #batch_first:True일 시, output 값의 사이즈는 (batch,seq,feature)가 됩니다. 기본 값은 False
        #bidrectional:True일 시, 양방향 RNN이 됩니다. 기본값은 False

    def init_hidden(self, batch_size: int) -> autograd.Variable:
        param1 = torch.randn(self.layers * self.direction, batch_size, self.d_model).to(self.device)
        param2 = torch.randn(self.layers * self.direction, batch_size, self.d_model).to(self.device)
        return torch.autograd.Variable(param1), torch.autograd.Variable(param2)
        #param1과 param2에 정규분포 형식의 난수값으로 받아 이 장치의 모델로(nn.LSTM) 변환한다.
        #자동미분을 해준다.
    def forward(self, x: Tensor) -> Tensor:    #순전파 단계에서는 입력텐서로부터 출력텐서를 계산
        b, l, v = x.size()
        out, _ = self.lstm(x, self.init_hidden(b)) #최종 예측 최종 출력 층

        # size = [batch_size, max_len, -1] 
        return out