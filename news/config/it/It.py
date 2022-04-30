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
    ITandSci
    @author: JunHyeon.Kim
    @date: 20220428
    https://news.naver.com/main/main.naver?mode=LSD&mid=shm&sid1=105
'''
class It:
    
    FLAG = "it"
    
    def __init__(self) -> None:
        global PROJ_ROOT_PATH
        self.jsonFilePath = f"{PROJ_ROOT_PATH}/file/{It.FLAG}"
        self.fileName = f"{It.FLAG}-naver-news-{UtilTime.getFileGenTime()}.txt"
        It.isDirectory(filePath= self.jsonFilePath)
        self.reqUrl = Url.REQ_URL
        self.reqHeader = Url.REQ_HEADER
        self.sid1 = {105: "IT/과학"}
        self.sid2 = {
            731: "모바일",
            226: "인터넷/SNS",
            227: "통신/뉴미디어",
            230: "IT일반",
            732: "보안/해킹",
            283: "컴퓨터",
            229: "게임/리뷰"
        }
        self.totalUrlList = []
    
    @classmethod
    def isDirectory(cls, filePath: str):
        '''
        :param: filePath
        :return:
        '''
        print("----------------------------------------")
        print(f"* b) {It.FLAG} - jsonFilePath: {filePath}")
        print("----------------------------------------")
        result = os.path.isdir(filePath)
        if not result:
            raise FileNotFoundError
