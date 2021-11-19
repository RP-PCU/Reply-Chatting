
from Reply_Chatting.app import Scenario
from kocrawl.map import MapCrawler

# 장소
Place = Scenario(
    intent='information',
    api=MapCrawler().request,
    scenario={
        'PLACE': []
    }
)

university = Scenario(
    intent='university',
    api=MapCrawler().request,
    scenario={
        'LOCATION': [],
        'PLACE': ['맛집']
    }
)

professor = Scenario(
    intent='professor',
    api=DustCrawler().request,
    scenario={
        'LOCATION': [],
        'DATE': ['오늘']
    }
)


