from elasticsearch import Elasticsearch
from elasticsearch.helpers import bulk 
'''
'''
class ElasticClient:
    
    def __init__(self) -> None:
        self.index = "naver_news"
        self.esClient = ElasticClient.getElasticClient()
   
    def bulkInsert(self, action):
        '''
        '''
        #try:
            
        bulk(self.esClient, actions= action) 
        #except:
        #    print("bulk insert fail !!")
        #else:
        #    print("bulk insert success !!")
     
    @classmethod 
    def getElasticClient(cls)-> Elasticsearch:
       '''
       :param
       :return
       '''
       client = Elasticsearch(hosts=["http://localhost:9200"])
       return client 