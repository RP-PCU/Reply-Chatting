import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
import sys

#접속할 url
url = 'https://www.pcu.ac.kr/kor/28/addressBook'

response = requests.get(url)


    
#크롬 웹 드라이버의 경로를 설정합니다.
#경로 오류나면 이것과 같이 정방향 슬래쉬로 설정    
path = "C:/Reply-Chatting/chromedriver_win32/chromedriver.exe"
driver = webdriver.Chrome(path)

#접속 시도
driver.get(url)
#웹페이지가 로딩되기까지 시간이 필요해서 sleep을 이용해 기다림
time.sleep(2) #1.5초

query_txt = input('교수님 성함을 입력해주세요!:')
# 사용자에게 검색어 입력

element = driver.find_element(By.ID, "searchKeyword")
element.send_keys(query_txt)  #검색어입력하게 하는 부분
element.send_keys("\n")  #엔터효과
#검색창의 이름을 찾아서 검색어를 입력


html = response.text
soup = BeautifulSoup(html, 'html.parser')
tbody = soup.select_one('#addrdss_list > table > tbody')
trs = soup.select('tr')

professor = driver.find_element(By.CLASS_NAME,"table").text
sys.stdout = open('professor_info.txt','a')
print(professor)

"""
professor_list = []
professor_list.append(professor)
"""