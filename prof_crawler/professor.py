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


query_txt = ['강명숙','이현주','손의성','이성덕','박석준','백낙천','심혜령','지현숙','최정순','정순분','강수자','김우승',
'김정태','박윤기','손성태','안미진','유왕무','윤준','이상원','이영순','이창인','조영우','김동건','김종서',
'유진숙','김욱','오진석','이혁우','이혜경','임헌만','정연정','최호택','최애나','송진숙','이대균','이성희',
'이진화','강호정','김원겸','박현민','이정언','문창권','방용태','이신규','김범환','임광혁','김영태','박준용',
'유종서','정강환','곽용섭','서진욱','이성만','곽한식','김하근','이정기','이종수','이종수','이준원','최창원',
'서병기','전은미','김정현','김정우','이상수','차미경','채순기','류시현','이수진','정재길','김지훈','서성호',
'김용호','남승현','김성수','김영선','박종대','성수학','이규봉','이진걸','강미경','임거수','배선영','김청훈',
'김성숙','이철세','조창호','한규광','이경희','황상기','강보순','공현철','이도형','이범희','임유진','이경찬',
'차도완','김도완','김익상','류황','박두영','주기호','장종환','송정영','이창훈','정회경','김창수','고경민',
'김진홍','임선영','양승의','이성옥','김진수','이병엽','조인준','신영진','강아름','함형민','곽내정','안성옥',
'심윤식','이영호','박동원','김성수','김영백','민병진','윤인권','임대영','송정환','김종옥','김택남','박원규',
'오영기','이상범','이상범','이택혁','김종헌','박인규','이정우','이란표','차명열','이시영','강병호','임영호',
'구미지','김현숙','문희강','송경헌','이정임','권순환','문성준','이영우','김기탁','김한수','최웅재','이봉지',
'조태준','채경화','한기남','권순자','임종보','배희재','권우정','박은비','백종우','양승희','최도원','최진실']

"""
query_txt = input('교수님 성함을 입력해주세요!:')
# 사용자에게 검색어 입력
"""
for i in query_txt:
    element = driver.find_element(By.ID, "searchKeyword")
    element.send_keys(i)  #검색어입력하게 하는 부분
    element.send_keys("\n")  #엔터효과
    #검색창의 이름을 찾아서 검색어를 입력


    html = response.text
    soup = BeautifulSoup(html, 'html.parser')
    tbody = soup.select_one('#addrdss_list > table > tbody')
    trs = soup.select('tr')

    professor = driver.find_element(By.CLASS_NAME,"table").text
    sys.stdout = open('professor_info.txt','a')
    print(professor)
    
    element.clear() #검색창 클리어
    
    