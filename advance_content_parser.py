# -*- coding:utf-8 -*-

import urllib2
import html2text
from settings_advanced import *
import cookielib
import ssl
import json


def test():
    text = u"<p>给定 <em>n</em> 个非负整数 <em>a</em><sub>1</sub>，<em>a</em><sub>2，</sub>...，<em>a</em><sub>n，</sub>每个数代表坐标中的一个点&nbsp;(<em>i</em>,&nbsp;<em>a<sub>i</sub></em>) 。在坐标内画 <em>n</em> 条垂直线，垂直线 <em>i</em>&nbsp;的两个端点分别为&nbsp;(<em>i</em>,&nbsp;<em>a<sub>i</sub></em>) 和 (<em>i</em>, 0)。找出其中的两条线，使得它们与&nbsp;<em>x</em>&nbsp;轴共同构成的容器可以容纳最多的水。</p>\n\n<p><strong>说明：</strong>你不能倾斜容器，且&nbsp;<em>n</em>&nbsp;的值至少为 2。</p>\n\n<p><img alt=\"\" src=\"https://aliyun-lc-upload.oss-cn-hangzhou.aliyuncs.com/aliyun-lc-upload/uploads/2018/07/25/question_11.jpg\" style=\"height: 287px; width: 600px;\"></p>\n\n<p><small>图中垂直线代表输入数组 [1,8,6,2,5,4,8,3,7]。在此情况下，容器能够容纳水（表示为蓝色部分）的最大值为&nbsp;49。</small></p>\n\n<p>&nbsp;</p>\n\n<p><strong>示例:</strong></p>\n\n<pre><strong>输入:</strong> [1,8,6,2,5,4,8,3,7]\n<strong>输出:</strong> 49</pre>\n"
    # print text
    h = html2text.HTML2Text()
    print h.handle(text)


def get_default_code(question_detail):
    definition_list = json.loads(question_detail['codeDefinition'])
    for definition in definition_list:
        if language == definition['value']:
            return definition['defaultCode']
    return ''


def query_question(query_path=None):
    path = query_path if not debug_mode else 'container-with-most-water'
    question_url = "https://leetcode-cn.com/problems/%s/description/" % path
    query = r'\n'.join(query_keys)
    body = r'{"query":"query {question(titleSlug: \"%s\") { %s} }"}' % (path, query)

    if debug_mode:
        ctx = ssl.create_default_context()
        ctx.check_hostname = False
        ctx.verify_mode = ssl.CERT_NONE
        csrftoken = 'orQY5ceImPq4HkUHpd3a0lC2me0F25bMIRoEfW4SaP9uOAzDxeOb7zHkqofI5fZM'
    else:
        ctx = None
        cookie_jar = cookielib.CookieJar()
        opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie_jar))
        urllib2.install_opener(opener)
        request = urllib2.Request(question_url)
        urllib2.urlopen(request)
        cookies = dict((cookie.name, cookie.value) for cookie in cookie_jar)
        csrftoken = cookies['csrftoken']

    headers = {
        'Content-Type': 'application/json',
        'X-CSRFToken': csrftoken,
        'Referer': question_url,
        'Cookie': 'csrftoken=%s' % csrftoken
    }
    request = urllib2.Request('https://leetcode-cn.com/graphql', body, headers)
    response = urllib2.urlopen(request, context=ctx)
    data = json.load(response)
    return data['data']['question']


if __name__ == '__main__':
    detail = query_question('two-sum')
    print get_default_code(detail)
