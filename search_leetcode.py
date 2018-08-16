# -*- coding:utf-8 -*-
import urllib2
import sys
from settings import query_url, search_limit, search_display

try:
    import cPickle as pickle
except ImportError:
    import pickle


def main():
    q_str = sys.argv[1]
    id_list = query(q_str)
    info_list = get_info_list('dumps.txt')
    for qid in id_list:
        display = get_desc(info_list, qid)
        if display:
            print display


def query(text):
    qid_str = urllib2.urlopen(query_url % text).read()
    id_list = qid_str[1:-1].split(',')[:search_limit]
    return id_list


def get_desc(info_list, qid):
    return search_display.format(**info_list[qid]) if qid in info_list else ''


def get_info_list(file_name):
    return pickle.load(open(file_name, 'r'))


if __name__ == '__main__':
    main()
