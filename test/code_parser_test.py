import re
from template_codes import *

if __name__ == '__main__':
    signature = re.compile(r'public\s(?P<ret>\w+)\s(?P<med>\w+)\((?P<par>.*?)\)\s{')
    m = signature.search(code_2)
    signature = dict(zip(['ret', 'name', 'param'], m.groups()))
    dp = {'sign': signature}
    print pattern_test.format(author='abosen', date='now',case='', **dp)
