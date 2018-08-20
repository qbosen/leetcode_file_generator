# coding=utf-8

import cookielib
import json
import ssl
import urllib2

from settings_advanced import *


class AdvancedDescriptionParser(object):
    def __init__(self):
        self.data = {}

    def parse(self, path):
        items = query_question(path)
        self.data['index'] = items['questionId']
        self.data['title'] = items['translatedTitle']
        self.data['title_en'] = items['questionTitle']
        self.data['content'] = items['translatedContent']
        self.data['path'] = path
        self.data['difficulty'] = items['difficulty']
        self.data['case'] = items['sampleTestCase']
        # get topics
        topics = []
        topics_en = []
        for topic in items['topicTags']:
            topics.append(topic['translatedName'])
            topics_en.append(topic['name'])

        self.data['topics_en'] = ', '.join(topics_en)
        self.data['topics'] = ', '.join(topics)
        stats = json.loads(items['stats'])
        self.data['percent'] = stats['acRate']
        # get sample codes
        definition_list = json.loads(items['codeDefinition'])
        for definition in definition_list:
            if language == definition['value']:
                self.data['codes'] = definition['defaultCode']
                break
        return self

    @property
    def index(self):
        return self.data['index']

    @property
    def title(self):
        return self.data['title']

    @property
    def title_en(self):
        return self.data['title_en']

    @property
    def content(self):
        # todo simplify the html by html2md.py
        return self.data['content']

    @property
    def difficulty(self):
        return self.data['difficulty']

    @property
    def percent(self):
        return self.data['percent']

    @property
    def codes(self):
        return self.data['codes']

    @property
    def case(self):
        return self.data['case']

    @property
    def topics(self):
        return self.data['topics']

    @property
    def topics_en(self):
        return self.data['topics_en']


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
    adp = AdvancedDescriptionParser().parse(None)
    print adp.content