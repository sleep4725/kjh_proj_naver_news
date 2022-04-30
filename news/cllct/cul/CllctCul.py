import os 
PROJ_ROOT_PATH = os.path.dirname(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
# ~/Desktop/cllct/naver/news/cllct
print("--------------------------------------")
print(f"* a) root-path-[Cul] : {PROJ_ROOT_PATH}")
print("--------------------------------------")

import sys
sys.path.append(PROJ_ROOT_PATH)
import requests
import json 
from bs4 import BeautifulSoup 

try:
    
    from config.cul.Cul import Cul 
    from config.util.UtilTime import UtilTime
except ModuleNotFoundError as err:
    print(err)
    
'''
    Cul
    @author JunHyeon.Kim
    @date 20220428
'''
class CllctCul(Cul):
    
    def __init__(self) -> None:
        Cul.__init__(self)
        
    def getUrl(self):
        '''
        :param:
        :return:
        '''
        sid1 = [k for k in self.sid1.keys()][0] 
        
        for sid2 in self.sid2.keys():
            for page in range(1, 11):
                reqUrl = self.reqUrl + f"&sid1={sid1}" + f"&sid2={sid2}" + f"&date={UtilTime.getCllctTime()}" +\
                    f"&page={page}"
                
                print(f"* requUrl: {reqUrl}")
                try:
                    
                    response = requests.get(reqUrl, headers=self.reqHeader)
                except requests.exceptions.ConnectionError as err:
                    print(err)
                else:
                    if response.status_code == 200:
                        bsObject = BeautifulSoup(response.text, "html.parser")
                        headline = bsObject.select_one("ul.type06_headline")
                        for n, l in enumerate(headline.select("li")):
                            aTag = l.select_one("dl > dt > a")
                            href = aTag.attrs["href"]
                            
                            self.totalUrlList.append(
                                {
                                    "url": href 
                                    , "sid1": sid1
                                    , "sid1_kor": self.sid1[sid1]
                                    , "sid2": sid2
                                    , "sid2_kor": self.sid2[sid2]
                                    , "no": n+1 
                                }
                            )
    
    def makeUrlFile(self):
        '''
        https://news.naver.com/main/list.naver?mode=LS2D&mid=shm&sid1=100&sid2=264&date=20220428&page=1
        :param:
        :return:
        '''
        try:
            logFile = self.jsonFilePath + "/" + self.fileName
            with open(logFile, "a", encoding="utf-8") as fw:
                
                fw.write('{"flag": "start"}\n') # start flag
                for u in self.totalUrlList:
                    fw.write(json.dumps(u, ensure_ascii=False) + "\n")
                fw.write('{"flag": "end"}\n')   # end flag
                fw.close()
        except:
            print(f"file {logFile} create fail!!")
        else:
            print(f"file {logFile} create success !!")
            
if __name__ == "__main__":
    o = CllctCul()
    o.getUrl()
    o.makeUrlFile()
