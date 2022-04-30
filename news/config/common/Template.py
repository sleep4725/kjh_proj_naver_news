'''
'''
class Template:
    
    def __init__(
            self, news_cllct_time, news_press, news_title, news_body, news_url
        ) -> None:
        self.news_cllct_time = news_cllct_time 
        self.news_press = news_press 
        self.news_title = news_title
        self.news_body = news_body
        self.news_url = news_url 
        
    def ret(self)-> dict:
        return {
           "news_cllct_time": self.news_cllct_time,
           "news_press": self.news_press,
           "news_title": self.news_title,
           "news_body": self.news_body,
           "news_url": self.news_url
        } 
    
    