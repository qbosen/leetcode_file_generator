# coding=utf-8
# /usr/bin/python html_parser.py [default.html]

import sys
from bs4 import BeautifulSoup

try:
    import cPickle as pickle
except ImportError:
    import pickle


def main():
    filename = sys.argv[1] if len(sys.argv) > 1 else 'default.html'
    soup = BeautifulSoup(open(filename), "html.parser", from_encoding="utf8")
    data_dic = {}
    for tr in soup.find_all('tr'):
        tds = tr.find_all('td')
        index, dic = parse_td(tds)
        data_dic[index] = dic
    print 'complete parse file: %s' % filename
    with open('dumps.txt', 'wr') as f:
        pickle.dump(data_dic, f)
    print 'success update dumps.txt!'


def parse_td(tds):
    index = tds[1].get_text().encode('utf8')
    en_name = tds[2]['value'].encode('utf8')
    a_tag = tds[2].a
    href = a_tag['href'].encode('utf8')
    ch_name = a_tag.get_text().encode('utf8')
    percent = tds[4].get_text().encode('utf8')
    level = tds[5].span.get_text().encode('utf8')
    dic = {
        'index': index,
        'en_name': en_name,
        'path': href[10:],
        'ch_name': ch_name,
        'percent': percent,
        'level': level,
    }
    return index, dic


if __name__ == '__main__':
    main()
