import scrapy
import json


from weibo.items import WeiboItem

class WeiboSpider(scrapy.Spider):
    name = "weibo"
    allowed_domains = ["m.weibo.cn"]
    start_urls = ["https://m.weibo.cn/api/container/getIndex?containerid=231051_-_fans_-_3641513235&since_id=2"]

    def parse(self,response):
        # print("response.meta", response.meta)
        if('page' in response.meta):
            page = response.meta['page']
        else:
            page = 1
        result = json.loads(response.text)
        # print(response.text)
        users = result.get("data").get("cards")[0]
        if(users is None):
            return;
        for card in result.get("data").get("cards"):
            for group in card.get("card_group"):
                user = group.get("user")
                if(user):
                    weibo = WeiboItem()
                    weibo['uid'] = user['id']
                    weibo['nikename'] = user['screen_name']
                    weibo['faceurl'] = user['profile_image_url']
                    yield weibo

        request = scrapy.Request("https://m.weibo.cn/api/container/getIndex?containerid=231051_-_fans_-_3641513235&since_id=%d" %(page), callback=self.parse)
        request.meta['page'] = page + 1
        yield request
