from baidu_collection import baidu_site_collect
from seo_info import crawl_info
from configure.settings import DBSelector
import datetime
import argparse

client = DBSelector().mongo('qq')
doc = client['db_parker']['seo']


def main():

    parser = argparse.ArgumentParser()
    '''
    Command line options
    '''
    parser.add_argument(
        '-n',
        '--name', type=str,
        help='input web domain'
    )

    parser.add_argument(
        '-f',
        '--file', type=str,
        help='input web site domain file name'
    )

    FLAGS = parser.parse_args()
    site_list=[]
    if FLAGS.name:
        print(FLAGS.name)
        if '.' in FLAGS.name:
            site_list.append(FLAGS.name)

    elif FLAGS.file:
        print(FLAGS.file)
        with open(FLAGS.file,'r') as fp:
            webs=fp.readlines()

        site_list.extend(list(map(lambda x:x.strip(),webs)))

    if site_list:

        run(site_list=site_list)
    else:
        print("please input correct web domain")


def run(site_list):

    # TODO： 改为命令行形式


    for site in site_list:
        count = baidu_site_collect(site)
        info = crawl_info(site)
        print(info)
        print(count)
        info['site'] = site
        info['baidu_count'] = count
        info['update_time'] = datetime.datetime.now()
        doc.insert_one(info)


if __name__ == '__main__':
    main()
