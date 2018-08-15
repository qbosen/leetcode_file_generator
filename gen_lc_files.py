# -*- coding:utf-8 -*-
# /usr/bin/python gen_lc_files.py 100

import sys
import time
import os
from settings import *

try:
    import cPickle as pickle
except ImportError:
    import pickle
from content_parser import DescriptionParser


def get_info(num):
    dic = pickle.load(open('dumps.txt', 'r'))
    return dic[num] if num in dic else {}


def generate_file(package_path, file_name, content):
    full_path = os.path.join(package_path, file_name)
    with open(full_path, 'w') as f:
        f.write(content)


def make_dir(info):
    def get_level(ch_level):
        level_map = {'简单': 'easy', '中等': 'medium', '困难': 'hard'}
        return level_map[ch_level] if ch_level in level_map else 'not_define'

    level = get_level(info['level'])
    package_path = os.path.join(src_path, level, 'q{:0>3s}'.format(info['index']))
    if not os.path.exists(package_path):
        os.makedirs(package_path)
    return package_path


if __name__ == '__main__':
    # num = sys.argv[1]
    info = get_info('2')
    dp = DescriptionParser().parse(url_pattern % info['path'])
    package_path = make_dir(info)
    date = time.strftime('%Y-%m-%d', time.localtime())

    md = table_pattern.format(title=dp.title, content=dp.content, date=date, **info)
    generate_file(package_path, 'README.md', md)

    # os.makedirs('./a/b/c')
