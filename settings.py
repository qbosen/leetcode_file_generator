# -*- coding:utf-8 -*-

src_path = "/Users/abosen/PycharmProjects/leetcode-file-generator"
url_pattern = "https://leetcode-cn.com/problems/%s/description/"

table_pattern = \
    '''### {title}
|\t|\t|\n|---:|:---|\n|题号|{index:0>3s}|\n|中文名|{ch_name}|
|英文名|{en_name}|\n|难度|{level}|\n|通过率|{percent}|\n|链接|[{path}][desc_url]
\n{content}
### 思路 {date}\n\n
[desc_url]:[https://leetcode-cn.com/problems/{path}/description/]'''
