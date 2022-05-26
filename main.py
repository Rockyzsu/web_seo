from baidu_collection import baidu_site_collect
from seo_info import crawl_info
from configure.settings import DBSelector
import datetime


client = DBSelector().mongo('qq')
doc = client['db_parker']['seo']


site_list=[
    'www.gairuo.com',
]

for site in site_list:
    count=baidu_site_collect(site)
    info = crawl_info(site)
    print(info)
    print(count)
    info['site']=site
    info['baidu_count']=count
    info['update_time']=datetime.datetime.now()
    doc.insert_one(info)