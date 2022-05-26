from parsel import Selector
import requests

def baidu_site_collect(site):
    # 百度收录
    headers = {'User-Agent': 'Chrome Google FireFox IE'}
    url = 'https://www.baidu.com/s?wd=site:{}&rsv_spt=1&rsv_iqid=0xf8b7b7e50006c034&issp=1&f=8&rsv_bp=1&rsv_idx=2&ie=utf-8&tn=baiduhome_pg&rsv_enter=0&rsv_dl=ib&rsv_sug3=14&rsv_sug1=7&rsv_sug7=100&rsv_n=2&rsv_btype=i&inputT=8238&rsv_sug4=8238'.format(site)
    resp = requests.get(
        url=url,
        headers=headers
    )

    resp.encoding='utf8'
    html = resp.text
    selector = Selector(text=html)

    count = selector.xpath('//div[@class="op_site_domain c-row"]/div/p/span/b/text()').extract_first()
    if count:
        count=int(count.replace(',',''))
    return count

if __name__=='__main__':
    site='30daydo.com'
    print(baidu_site_collect(site))


