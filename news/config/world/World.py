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
    World
    @author: JunHyeon.Kim
    @date: 20220428
    https://news.naver.com/main/main.naver?mode=LSD&mid=shm&sid1=104
'''
class World:
    
    FLAG = "world"
    
    def __init__(self) -> None:
        global PROJ_ROOT_PATH
        self.jsonFilePath = f"{PROJ_ROOT_PATH}/file/{World.FLAG}"
        self.fileName = f"{World.FLAG}-naver-news-{UtilTime.getFileGenTime()}.txt"
        World.isDirectory(filePath= self.jsonFilePath)
        self.reqUrl = Url.REQ_URL
        self.reqHeader = Url.REQ_HEADER
        self.sid1 = {104: "세계"}
        self.sid2 = {
            231: "아시아/호주",
            232: "미국/중남미",
            233: "유럽",
            234: "중동/아프리카"
        }
        self.totalUrlList = []
    
    @classmethod
    def isDirectory(cls, filePath: str):
        '''
        :param: filePath
        :return:
        '''
        print("----------------------------------------")
        print(f"* b) {World.FLAG} - jsonFilePath: {filePath}")
        print("----------------------------------------")
        result = os.path.isdir(filePath)
        if not result:
            raise FileNotFoundError
