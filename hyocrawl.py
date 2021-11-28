# %%
import pandas as pd
from pandas._config.config import reset_option 



def crawl(user):
    
    data = pd.read_csv(r"C:\Reply-Chatting\test.csv", encoding='utf-8')
    # data 데이터프레임 형식으로 변환 
    df = pd.DataFrame(data)
    answer = df["name"] == user
    result = df[answer]
    print(result)
    

# %%
user = input("찾으실 교수님 성함을 입력하세요")
crawl(user)

# %%
df_t = pd.read_csv('tt.txt', sep=",")
print(df_t)