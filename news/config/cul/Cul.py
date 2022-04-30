import os 
PROJ_ROOT_PATH = os.path.dirname(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
import sys
sys.path.append(PROJ_ROOT_PATH)
try:
    
    from config.common.Url import Url
    from config.util.UtilTime import UtilTime
except ModuleNotFoundError as err:
    print(err)

'''
    @author: JunHyeon.Kim
    @date: 20220428
    https://news.naver.com/main/main.naver?mode=LSD&mid=shm&sid1=101
'''
class Cul:
    
    FLAG = "cul"
    
    def __init__(self) -> None:
        global PROJ_ROOT_PATH
        self.jsonFilePath = f"{PROJ_ROOT_PATH}/file/{Cul.FLAG}"
        self.fileName = f"{Cul.FLAG}-naver-news-{UtilTime.getFileGenTime()}.txt"
        Cul.isDirectory(filePath= self.jsonFilePath)
        self.reqUrl = Url.REQ_URL
        self.reqHeader = Url.REQ_HEADER
        self.sid1 = {103: "생활/문화"}
        self.sid2 = {
            241: "건강정보",
            239: "자동차/시승기",
            240: "도로/교통",
            237: "여행/레저",
            238: "음식/맛집",
            376: "패션/뷰티",
            242: "공연/전시",
            243: "책",
            244: "종교",
            248: "날씨"
        }
        self.totalUrlList = []
    
    @classmethod
    def isDirectory(cls, filePath: str):
        '''
        :param: filePath
        :return:
        '''
        print("----------------------------------------")
        print(f"* b) {Cul.FLAG} - jsonFilePath: {filePath}")
        print("----------------------------------------")
        result = os.path.isdir(filePath)
        if not result:
            raise FileNotFoundError
