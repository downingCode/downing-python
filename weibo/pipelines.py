# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import requests
from weibo.items import WeiboItem

class WeiboPipeline(object):
    def process_item(self, item, spider):
        return item


class downloadImagePipeline(object):
    def process_item(self, item, spider):
        if isinstance(item, WeiboItem):
            faceurl = item['faceurl']
            self.download_file(faceurl, "D:\weibopic")
            return item

    def download_file(self, url, directory):
        local_filename = "%s/%s" % (directory, url.split('/')[-1])
        # NOTE the stream=True parameter
        print(local_filename)
        r = requests.get(url, stream=True)
        with open(local_filename, 'wb') as f:
            for chunk in r.iter_content(chunk_size=1024):
                if chunk:  # filter out keep-alive new chunks
                    f.write(chunk)
                    # f.flush() commented by recommendation from J.F.Sebastian
        return local_filename
