# coding=utf-8
# /usr/bin/python gen_files.py 100

import os
import sys
import time

from settings import *
from settings_advanced import *

try:
    import cPickle as pickle
except ImportError:
    import pickle
from content_parser import DescriptionParser
from content_parser_advance import AdvancedDescriptionParser


def main():
    num = sys.argv[1] if len(sys.argv) > 1 else '11'
    level = sys.argv[2] if len(sys.argv) > 2 else None
    level = int(level) if level else default_format
    if not num:
        return

    info = get_info(num)
    package_path = make_dir(info)
    en_level = get_level(info)
    date = time.strftime('%Y/%m/%d', time.localtime())

    if not enable_advance:
        dp = DescriptionParser().parse(info['path'])
        md = md_pattern.format(title=dp.title, content=dp.content, date=date, **info)
        solution = class_pattern.format(en_level=en_level, author=author, date=date, **info)
        test = test_class_pattern.format(en_level=en_level, author=author, date=date, **info)
    else:
        dp = AdvancedDescriptionParser().parse(info['path'], level)
        dp_data = dp.data
        # print dp_data
        md = ad_md_pattern.format(date=date, **dp_data)
        solution = ad_class_pattern.format(en_level=en_level, author=author, date=date, **dp_data)
        test = ad_test_class_pattern.format(en_level=en_level, author=author, date=date, **dp_data)

    generate_file(package_path, 'README.md', md)
    generate_file(package_path, 'Solution.java', solution)
    generate_file(package_path, 'SolutionTest.java', test)


def get_info(num):
    dic = pickle.load(open('dumps.txt', 'r'))
    return dic[num] if num in dic else {}


def generate_file(base_path, file_name, content):
    full_path = os.path.join(base_path, file_name)
    with open(full_path, 'w') as f:
        f.write(content.encode('utf-8'))
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
