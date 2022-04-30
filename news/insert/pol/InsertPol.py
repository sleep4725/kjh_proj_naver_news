import dataclasses
import os

from ast import literal_eval
from bs4 import BeautifulSoup
from requests import head 
PROJ_ROOT_PATH = os.path.dirname(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
# ~/Desktop/cllct/naver/news/cllct
print("--------------------------------------")
print(f"* a) root-path-[Pol] : {PROJ_ROOT_PATH}")
print("--------------------------------------")

import json
from multiprocessing import Pool
import sys
sys.path.append(PROJ_ROOT_PATH)

try:
    import requests    
    from config.pol.Pol import Pol 
    from config.util.UtilTime import UtilTime
    from config.common.Template import Template
    from es.ElasticClient import ElasticClient
except ModuleNotFoundError as err:
    print(err)

'''
@author JunHyeon.Kim
'''
def getContent(url):
    '''
    '''
    global pol
    global esObject
    global actions
    
    print(url["url"])
    response = requests.get(url["url"], headers=pol.reqHeader)
    if response.status_code == 200:
        doc = Template(news_body="", news_cllct_time="", news_press="", news_title="", news_url="")
    
        #print(f"** req : url{url['url']} status_code: 200")
        bsObject = BeautifulSoup(response.text, "html.parser")
        newsct = bsObject.select_one("div#ct.newsct")
        head = newsct.select_one("div.media_end_head.go_trans")
        
        # 1. news press
        newsPress = head.select_one("div.media_end_head_top > a.media_end_head_top_logo > img")
        doc.news_press = newsPress.attrs["title"]
        
        # 2. news title
        newsHeadline = head.select_one("div.media_end_head_title > h2.media_end_head_headline")
        newsHeadline = newsHeadline.string
        doc.news_title = newsHeadline
        
        # 3. news body 
        bsObject.select_one("#dic_area")
        newsBody = newsct.select_one("div#contents.newsct_body > \
            div#newsct_article.newsct_article._article_body > \
            div#dic_area")
        doc.news_body = str(newsBody.text).strip("\n").replace("\n", " ").replace('"', ' ')
        
        # 4
        doc.news_url = url['url']
        doc.news_cllct_time = UtilTime.getFileGenTime()
        # 5
        actions.append({
            "_index": esObject.index,
            "_source": doc.ret() 
        })
        print(len(actions))
    response.close()
    
def fileRead():
    '''
    '''
    global urlList, pol
    
    tmpList = []
    result = os.path.isdir(pol.jsonFilePath)
    
    if result:
        for file in os.listdir(pol.jsonFilePath):
            fileAbstractPath = pol.jsonFilePath + f"/{file}"
            
            if os.path.exists(fileAbstractPath):
                with open(fileAbstractPath, "r", encoding="utf-8") as fr:
                    # string_to_dict = json.loads(strings.replace("'", "\""))
                    tmpList.extend([json.loads(e.replace("'", "\"").rstrip("\n")) for e in fr.readlines()])
                    if tmpList[0]['flag'] == "start" and tmpList[-1]['flag'] == "end":
                        # 파일의 처음 부분과 끝 부분이 정상적으로 처리가 되어 졌다면
                        urlList.extend(tmpList[1: len(tmpList)-1])
                    else:
                        ''' File make error
                        '''
                    
                    fr.close()
            else:
                raise FileNotFoundError
                    
if __name__ == "__main__":
    urlList = []
    actions = []
    esObject = ElasticClient()
    pol = Pol()
    fileRead()
    
    for u in urlList:
        getContent(u)
    
    esObject.bulkInsert(actions)