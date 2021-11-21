
from Reply_Chatting.app import Scenario
from kocrawl.map import MapCrawler
from KOCRAWL.kocrawl.uni import UniCrawler


# 건물
university = Scenario(
    intent='university',
    api=UniCrawler().request,
    scenario={
        'PLACE': []
    }
)

# 맛집
restaurnt = Scenario(
    intent='restaurnt',
    api=MapCrawler().request,
    scenario={
        'LOCATION': [],
        'PLACE': ['맛집']
    }
)

