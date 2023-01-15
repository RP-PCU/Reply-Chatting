# Reply-Chatting(배재대학교 챗봇)

## 실행 화면 
<img src="https://user-images.githubusercontent.com/83768386/212528748-882118f9-2e56-4ceb-8fbe-a9ec3fce55eb.mp4">

## 프로젝트 주제
* 해당 프로젝트의 주제를 정했을 때에 covid-19가 가장 큰 이슈 였습니다. 그래서 저희 팀은 코로나와 학교를 연관지어서 생각을 해보니 이번에 코로나로 인해서 대학교의 수업을 비대면으로 듣다 보니까 이미 2학년임에도 불구하고 학교에 대해서 아는 점이 미비하고 신입생 또한 대학교에 관해서 궁금한 점이 많이 있을 거로 생각하여 신입생 및 코로나로 인해서 학교주변 맛집과 교수님 정보, 수업을 듣는 건물들을 쉽게 찾을 수 있도록 도움을 주기 위하여 구현 하였습니다.

## 프로젝트 서론
* "배재대학교 챗봇"이라는 웹 애플리케이션을 프론트엔드 부분은 HTML5, CSS3, JavaScript, Jquery, BootStrap을 사용 하여 구현 하였으며, 백엔드 부분은 "kochat"이라는 오픈소스를 참고하여 구현, DB는 MySQL을 사용했으며 서버는 "REST API"오픈소스를 사용 하였습니다. 사용한 기능으로는 학교에 관련된 데이터와 주변 맛집을 찾는 기능을 사용 하기 위해서 Selenium을 활용해 데이터를 크롤링 하여 DB에 저장 했으며, 오픈소스로 가져온 "REST full API"가 작동될 경우 embed, intent, entity순서대로 추가한 초기 데이터를 가지고 학습을 하도록 구현 하여 사용자가 질문을 했을 경우에 그에 맞는 답변을 해주도록 구현 하였음

## 개발 담당
* FrontEnd 웹 구현 30%
* Selenium을 사용한 웹 데이터 크롤링 100%
* 데이터 DB 저장 및 DB테이블 구성 100%
* Entity 구현 70%

## 개발환경
* Visual Studio Code
* Virtual Env
* GitHub

## 사용기술
### Back End
* Python 
* Pandas
* Gensim
* Numpy
* Torch
* Selenium

### DataBase
* MySQL

### Front End
* BootStrap CSS framework
* HTML5, CSS3, JavaScript
* Jquery
* AJAX

## 주요키워드
* REST API
* Cache
* HTTP 통신
* 웹 데이터 크롤링
* Entity(개체명 인식)
* Embed(메시지 전송)
* Intent(의도 파악)
* Git버전관리
