from kocrawl.editor.base_editor import BaseEditor
import re

#TODO uni_editor 
class UniEditor(BaseEditor):
    
    def edit_map(self, location: str, place: str, result: dict) -> dict:
        """
        :param location: 지역
        :param place: 장소
        :param result: 데이터 딕셔너리
        :return: 수정된 딕셔너리
        """
        result = self.join_dict(result, 'context')
        result = self.join_dict(result, 'category')
        result = self.join_dict(result, 'address')
        result = self.join_dict(result, 'thumUrl')
        
        if isinstance(result['context'], str):
            result['context'] = re.sub(' ', ', ', result['context'])

        return result