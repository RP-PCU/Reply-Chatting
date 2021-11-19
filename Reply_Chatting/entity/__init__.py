from entity import LSTM #entity 파일에서 LSTM 불러오기

__ALL__= [LSTM]
#특정 디렉터리의 모듈을 *를 이용하여 import할 때에 
#해당 디렉터리의 __init__.py 파일에 __all__이라는 변수를 설정하고 import할 수 있는 모듈을 정의
#_all__로 정의하지 않으면 인식하지 X