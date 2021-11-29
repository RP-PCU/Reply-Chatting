from os import terminal_size
from numpy.lib.shape_base import column_stack
import pandas as pd
from pandas._config.config import reset_option
from pandas.core.frame import DataFrame 

def Hcrawl(user):
    # professor.txt의 
    csv_p = pd.read_csv('professor_info.txt', encoding = 'euc-kr', sep=" ")
    # data 데이터프레임 형식으로 변환 
    df = pd.DataFrame(csv_p)
    # df의 컬럼의 이름을 변경 
    df.rename(columns={"성명":"name"}, inplace=True)
    # "user"에게 받은 교수님의 성함을 입력받아서 교수님의 정보를 가진 행을 찾기
    answer = df["name"] == user
    result = df[answer]
    print(result)
    
    if __name__ == '__main__':
        Hcrawl()

"""
user = input("찾으실 교수님 성함을 입력하세요")
Hcrawl(user)
"""
"""
    (불필요한 데이터를 삭제하는 코드)
    with open('professor_info.txt', "r") as f:
        lines = f.readlines()
    with open('professor_info.txt', "w") as f:
        for line in lines:
            if line.strip("\n") != "":
                f.write(line)
"""