

from kocrawl.dust import DustCrawler
from kocrawl.weather import WeatherCrawler
from kochat.app import Scenario
from kocrawl.map import MapCrawler

"""from hocrawl_test.hyocrawl import Hcrawl

professor = Scenario(
    intent='NAME',
    api=Hcrawl().request,
    scenario={
        'NAME': []
    }
    
    
)"""


restaurant = Scenario(
    intent='restaurant',
    api=MapCrawler().request,
    scenario={
        'LOCATION': [],
        'PLACE': ['맛집']
    }
)

travel = Scenario(
    intent='travel',
    api=MapCrawler().request,
    scenario={
        'LOCATION': [],
        'PLACE': ['관광지']
    }
)