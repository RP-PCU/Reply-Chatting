from kocrawl.answerer.base_answerer import BaseAnswerer

#TODO배재대학교 건물 출력 포맷
class UniAnswerer(BaseAnswerer):
    
    def Uni_form(self, location: str,place: str, result: dict) -> str:
        """
        배재대학교 건물  출력 포맷 
        
        :param location: 학교
        :param place: 장소
        :param result: 데이터 딕셔너리
        :return: 출력 메시지
        """
        
        msg = self.uni_init_format(palce=place)
        msg += '{location} 의'

        msg = self._add_msg_from_dict(result, 'category', msg, '{category}')
        msg = self._add_msg_from_dict(result, 'address', msg, '주소는 {address}입니다.')
        msg = self._add_msg_from_dict(result, 'thumUrl', msg, '> 사진보기 : {thumUrl}')
        msg = msg.format(location=location, category=result['category'],address=result['address'], 
                         thumUrl=result['thumUrl'])

        return msg