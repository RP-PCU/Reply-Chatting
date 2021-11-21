
from Reply_Chatting.app import Scenario
from kocrawl.map import MapCrawler
from KOCRAWL.kocrawl.uni import UniCrawler

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
    api=UniCrawler().request,
    scenario={
        'LOCATION': [],
        'PLACE': ['학교건물']
    }
)


