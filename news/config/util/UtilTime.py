import time 

'''
    @author JunHyeon.Kim
'''
class UtilTime:
    
    @classmethod
    def getCllctTime(cls)-> str:
        '''
        :param:
        :return: yyyyMMdd 
        '''
        return time.strftime("%Y%m%d", time.localtime())
    
    @classmethod
    def getFileGenTime(cls)->str:
        '''
        :param:
        :return: yyyyMMddHHmm
        '''
        return time.strftime("%Y%m%d%H%M", time.localtime())
        