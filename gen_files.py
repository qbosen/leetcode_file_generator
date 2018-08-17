# -*- coding:utf-8 -*-
# /usr/bin/python gen_files.py 100

import sys
import time
import os
from settings import *

try:
    import cPickle as pickle
except ImportError:
    import pickle
from content_parser import DescriptionParser


def main():
    num = sys.argv[1] if len(sys.argv) > 1 else ''
    if not num:
        return

    info = get_info(num)
    dp = DescriptionParser().parse(detail_url % info['path'])
    package_path = make_dir(info)
    en_level = get_level(info)
    date = time.strftime('%Y/%m/%d', time.localtime())

    md = md_pattern.format(title=dp.title, content=dp.content, date=date, **info)
    generate_file(package_path, 'README.md', md)

    solution = class_pattern.format(en_level=en_level, author=author, date=date, **info)
    generate_file(package_path, 'Solution.java', solution)

    test = test_class_pattern.format(en_level=en_level, author=author, date=date, **info)
    generate_file(package_path, 'SolutionTest.java', test)


def get_info(num):
    dic = pickle.load(open('dumps.txt', 'r'))
    return dic[num] if num in dic else {}


def generate_file(base_path, file_name, content):
    full_path = os.path.join(base_path, file_name)
    with open(full_path, 'w') as f:
        f.write(content)
    print 'create file: %s' % full_path


def get_level(info_dict):
    ch_level = info_dict['level']
    level_map = {'简单': 'easy', '中等': 'medium', '困难': 'hard'}
    return level_map[ch_level] if ch_level in level_map else 'default'


def make_dir(info_dict):
    level = get_level(info_dict)
    base_path = os.path.join(src_path, level, 'q{:0>3s}'.format(info_dict['index']))
    if not os.path.exists(base_path):
        os.makedirs(base_path)
    return base_path


if __name__ == '__main__':
    main()
