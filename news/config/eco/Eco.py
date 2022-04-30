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
class Eco:
    
    FLAG = "eco"
    
    def __init__(self) -> None:
        global PROJ_ROOT_PATH
        self.jsonFilePath = f"{PROJ_ROOT_PATH}/file/{Eco.FLAG}"
        self.fileName = f"{Eco.FLAG}-naver-news-{UtilTime.getFileGenTime()}.txt"
        Eco.isDirectory(filePath= self.jsonFilePath)
        self.reqUrl = Url.REQ_URL
        self.reqHeader = Url.REQ_HEADER
        self.sid1 = {101: "경제"}
        self.sid2 = {
            259: "금융",
            258: "증권",
            261: "산업/재계",
            771: "중기/벤처",
            260: "부동산",
            262: "글로벌경제",
            310: "생활경제"
        }
        self.totalUrlList = []
    
    @classmethod
    def isDirectory(cls, filePath: str):
        '''
        :param: filePath
        :return:
        '''
        print("----------------------------------------")
        print(f"* b) {Eco.FLAG} - jsonFilePath: {filePath}")
        print("----------------------------------------")
        result = os.path.isdir(filePath)
        if not result:
            raise FileNotFoundError