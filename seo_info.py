import argparse
from atexit import register
import sys
import requests
import re
from parsel import Selector

#参数自定义

# parser = argparse.ArgumentParser()
# parser.add_argument('-r', dest='read', help='path file')
# parser.add_argument('-u',dest='read',help='targetdomain')
# parser_args = parser.parse_args()
#爬虫模块查询

VERBOSE = True

def askurl(target_url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.106 Safari/537.36'
    }


    #baidu权重
    baidu_url=f"https://rank.chinaz.com/{target_url}"
    baidu_txt=requests.get(url=baidu_url,headers=headers)
    baidu_html=baidu_txt.content.decode('utf-8')
    baidu_PC=re.findall('PC端</i><img src="//csstools.chinaz.com/tools/images/rankicons/baidu(.*?).png"></a></li>',baidu_html,re.S)
    baidu_moblie=re.findall('移动端</i><img src="//csstools.chinaz.com/tools/images/rankicons/bd(.*?).png"></a></li>',baidu_html,re.S)
    #分割线
    print("*"*60)

    #如果查询html中有正则出来到权重关键字就输出，否则将不输出
    result={}

    baidu_pc_weight = None
    baidu_mobile_weight = None

    if len(baidu_PC) > 0:
        print('百度_PC:', baidu_PC[0])
        baidu_pc_weight=baidu_PC[0]
    if len(baidu_moblie) > 0:
        print('百度_moblie:', baidu_moblie[0])
        baidu_mobile_weight = baidu_moblie[0]
    else:
        print("百度无权重")

    result['baidu_pc_weight']=baidu_pc_weight
    result['baidu_mobile_weight']=baidu_mobile_weight

    #360权重
    url=f"https://rank.chinaz.com/sorank/{target_url}/"
    text = requests.get(url=url,headers=headers)
    html=text.content.decode('utf-8')
    sorank360_PC=re.findall('PC端</i><img src="//csstools.chinaz.com/tools/images/rankicons/360(.*?).png"></a><',html,re.S)
    sorank360_Mobile=re.findall('移动端</i><img src="//csstools.chinaz.com/tools/images/rankicons/360(.*?).png"',html,re.S)

    _360_pc_weight=None
    _360_mobile_weight=None

    # 如果查询html中有正则出来到权重关键字就输出，否则将不输出
    if len(sorank360_PC) > 0:
        _360_pc_weight=sorank360_PC[0]
        print("360_PC:", sorank360_PC[0])
    if len(sorank360_Mobile) > 0:
        _360_mobile_weight=sorank360_Mobile[0]
        print("360_moblie:", sorank360_Mobile[0])
    else:
        print("360无权重")

    result['360_pc_weight']=_360_pc_weight
    result['360_mobile_weight']=_360_mobile_weight


    #搜狗权重


    sogou_pc_weight=None
    sogou_mobile_weight=None

    sogou_url = f"https://rank.chinaz.com/sogoupc/{target_url}"
    sougou_txt = requests.get(url=sogou_url, headers=headers)
    sougou_html = sougou_txt.content.decode('utf-8')
    sougou_PC = re.findall('PC端</i><img src="//csstools.chinaz.com/tools/images/rankicons/sogou(.*?).png"></a></li>',sougou_html, re.S)
    sougou_mobile = re.findall('移动端</i><img src="//csstools.chinaz.com/tools/images/rankicons/sogou(.*?).png"></a></li>',sougou_html, re.S)

    # 如果查询html中有正则出来到权重关键字就输出，否则将不输出
    if len(sougou_PC) > 0:
        print('搜狗_PC：', sougou_PC[1])
        sogou_pc_weight=sougou_PC[1]
        
    if len(sougou_mobile) > 0 :
        print('搜狗_moblie：', sougou_mobile[1])
        sogou_mobile_weight=sougou_mobile[1]

    else:
        print('搜狗无权重')


    result['sogou_pc_weight']=sogou_pc_weight
    result['sogou_mobile_weight']=sogou_mobile_weight


    #神马权重
    shenma_pc_weight =None   
    shenma_url=f'https://rank.chinaz.com/smrank/{target_url}'
    shenma_txt=requests.get(url=shenma_url,headers=headers)
    shenma_html=shenma_txt.content.decode('utf-8')
    shenma_PC=re.findall('class="tc mt5"><img src="//csstools.chinaz.com/tools/images/rankicons/shenma(.*?).png"></a></li>',shenma_html,re.S)

    # 如果查询html中有正则出来到权重关键字就输出，否则将不输出
    if len(shenma_PC) > 0:
        print('神马权重为：', shenma_PC[1])
        shenma_pc_weight=shenma_PC[1]
    else:
        print("神马无权重")


    result['shenma_pc_weight']=shenma_pc_weight
    # result['shenma_mobile_weight']=None


    #头条权重

    toutiao_pc_weight=None
    toutiao_url=f'https://rank.chinaz.com/toutiao/{target_url}'
    toutiao_txt=requests.get(url=toutiao_url,headers=headers)
    toutiao_html=toutiao_txt.content.decode('utf-8')
    toutiao_PC=re.findall('class="tc mt5"><img src="//csstools.chinaz.com/tools/images/rankicons/toutiao(.*?).png"></a></li>',toutiao_html,re.S)

    # 如果查询html中有正则出来到权重关键字就输出，否则将不输出
    if len(toutiao_PC) > 0:
        print('头条权重为：', toutiao_PC[1])
        toutiao_pc_weight=toutiao_PC[1]
    else:
        print("头条无权重")

    result['toutiao_pc_weight']=toutiao_pc_weight
    # result['toutiao_mobile_weight']=None


    #备案信息、title、企业性质
    beian_url=f"https://seo.chinaz.com/{target_url}"
    beian_txt=requests.get(url=beian_url,headers=headers)
    beian_html=beian_txt.content.decode('utf-8')
    
    with open('beian_html.html','w') as fp:
        fp.write(beian_html)

    title,beian_no,name,ip,nature,register,years=parse_info(beian_html)
    
    result['name']=name
    result['title']=title
    result['beian_no']=beian_no
    result['ip']=ip
    result['nature']=nature
    result['register']=register
    result['years']=years

    try:
        print("备案信息:",beian_no,"名称:",name,"网站首页Title：",title,"企业性质：",nature,"IP地址为：",ip)
        print("*"*60)
    except:
        print("没有查询到有效信息！")

    return result

strip_fun = lambda x:x.strip() if x is not None else ""

def parse_info(html):

    resp = Selector(text=html)
    title = strip_fun(resp.xpath('//div[@class="_chinaz-seo-t2l ellipsis"]/text()').extract_first())
    table = resp.xpath('//table[@class="_chinaz-seo-newt"]/tbody')
    
    if table[0].xpath('.//tr[4]/td[2]/span[1]/i'):
        beian_num=strip_fun(table[0].xpath('.//tr[4]/td[2]/span[1]/i/a/text()').extract_first())
    else:
        beian_num=strip_fun(table[0].xpath('.//tr[4]/td[2]/span[1]/a/text()').extract_first())

    name=strip_fun(table[0].xpath('.//tr[4]/td[2]/span[2]/i/text()').extract_first())
    if not name:
        print('---->',name)
        name=strip_fun(table[0].xpath('.//tr[4]/td[2]/span[2]/i/a/text()').extract_first())

    nature=strip_fun(table[0].xpath('.//tr[4]/td[2]/span[3]/i/text()').extract_first())
    ip=strip_fun(table[0].xpath('.//tr[5]/td[2]/div/span[1]/i/a/text()').extract_first())
    register=strip_fun(table[0].xpath('.//tr[3]/td[2]/div[1]/span[1]/i/text()').extract_first())
    years=strip_fun(table[0].xpath('.//tr[3]/td[2]/div[2]/span[1]/i/text()').extract_first())



    return title,beian_num,name,ip,nature,register,years


def crawl_info(site):
    return askurl(site)




if __name__ == '__main__':
    main()