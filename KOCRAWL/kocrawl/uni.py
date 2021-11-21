from kocrawl.answerer.university_answerer import UniAnswerer
from kocrawl.editor.uni_editor import UniEditor
from kocrawl.searcher.uni_searcher import UniSercher
from kocrawl.base import BaseCrawler

class UniCrawler(BaseCrawler):
    
    def request(self, location: str, place: str) -> str:
        """
        :param location: 지역
        :param place: 장소
        :return: 해당지역 장소
        """

        try:
            return self.request_debug(location, place)[0]
        except Exception:
            return UniAnswerer().sorry(
                "해당 지역은 알 수 없습니다."
            )
    
    def request_dict(self, location: str, place: str):
        """
        지도를 크롤링합니다.
        (try-catch로 에러가 나지 않는 함수)

        :param location: 지역
        :param place: 장소
        :return: 해당지역 장소
        """

        try:
            return self.request_debug(location, place)[1]
        except Exception:
            return UniAnswerer().sorry(
                "해당 지역은 알 수 없습니다."
            )

    def request_debug(self, location: str, place: str) -> tuple:
        """
        지도를 크롤링합니다.
        (에러가 나는 디버깅용 함수)

        :param location: 지역
        :param place: 장소
        :return: 해당지역 장소
        """

        result_dict = UniAnswerer().search_naver_map(location, place)
        result = UniAnswerer().edit_map(location, place, result_dict)
        result = UniAnswerer().map_form(location, place, result)
        return result, result_dict
