# %%
from os import terminal_size
import pandas as pd
from pandas._config.config import reset_option
from pandas.core.frame import DataFrame 


# %%
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
user = input("찾으실 교수님 성함을 입력하세요")
df_t = pd.read_csv('professor_info.txt', encoding = 'euc-kr', sep=" ")
df = pd.DataFrame(df_t)
df.rename(columns={"성명":"name"}, inplace=True)
answer = df["name"] == user
result = df[answer]
print(result)

# %%
df_t = pd.read_csv('professor_info.txt', encoding = 'euc-kr', sep=" ") 
df = pd.DataFrame(df_t)
df.rename(columns={"성명":"name"}, inplace=True)
print(df.columns)

# %%
data = pd.read_csv(r"C:\Reply-Chatting\test.csv", encoding='utf-8')
    # data 데이터프레임 형식으로 변환 
df = pd.DataFrame(data)
df.rename(columns={"name":"성함"}, inplace=True)
print(df.columns)

# %%
with open('professor_info.txt', "r") as f:
    lines = f.readlines()
with open('professor_info.txt', "w") as f:
    for line in lines:
        if line.strip("\n") != "테이블 캡션":
            f.write(line)