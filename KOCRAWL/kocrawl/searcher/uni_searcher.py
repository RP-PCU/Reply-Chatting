from kocrawl.searcher.base_searcher import BaseSearcher
import re

class UniSercher(BaseSearcher):
    
    def __init__(self):
        self.data_dict = {
            'thumUrl': [], 'category':[],
            'address':[],  
        }
        
    def _make_query(self, location: str, place: str):
        query = ' '.join([location, place])
        return query
    
    def search_naver_map(self, location: str, place: str) -> str:
        query = self._make_query(location, travel)
        result = self._json(url=self.url['naver_map'],
                            query=query)
        
        result = result['result']['place']['list']
        one_result = result[1]
        
        self.data_dict['category'].append(one_result['category'])
        self.data_dict['address'].append(one_result['address'])
        self.data_dict['thumUrl'].append(one_result['thumUrl'])
        self.data_dict = self._flatten_dicts(self.data_dict)
        return self.data_dict