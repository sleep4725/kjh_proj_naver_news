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
    https://news.naver.com/main/main.naver?mode=LSD&mid=shm&sid1=100
'''
class Pol:
    
    FLAG = "pol"
    
    def __init__(self) -> None:
        global PROJ_ROOT_PATH
        self.jsonFilePath = f"{PROJ_ROOT_PATH}/file/{Pol.FLAG}"
        self.fileName = f"{Pol.FLAG}-naver-news-{UtilTime.getFileGenTime()}.txt"
        Pol.isDirectory(filePath= self.jsonFilePath)
        self.reqUrl = Url.REQ_URL
        self.reqHeader = Url.REQ_HEADER
        self.sid1 = {100: "정치"}
        self.sid2 = {
            264: "청와대",
            265: "국회/정당",
            268: "북한",
            266: "행정",
            267: "국방외교"
        }
        self.totalUrlList = []
    
    @classmethod
    def isDirectory(cls, filePath: str):
        '''
        :param: filePath
        :return:
        '''
        print("----------------------------------------")
        print(f"* b) {Pol.FLAG} - jsonFilePath: {filePath}")
        print("----------------------------------------")
        result = os.path.isdir(filePath)
        if not result:
            raise FileNotFoundError