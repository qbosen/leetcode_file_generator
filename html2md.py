# coding=utf-8
import re
from settings_advanced import tags_map, clearable_tags, symbol_map


class Html2md(object):
    def __init__(self, html):
        self._html = html

    def _trans_symbol(self, mapping):
        self._html = trans_symbol(self._html, mapping)
        return self

    def _empty_tags(self):
        pattern = re.compile(r'<.*?>|</.*?>', re.S)
        self._html = re.sub(pattern, '', self._html)
        return self

    def _trans_tags_in_scope(self, scope, to):
        self._html = trans_tags_in_scope(self._html, scope, to)
        return self

    def _tags2md(self, mapping):
        self._html = tags2md(self._html, mapping)
        return self

    def _replace_tag(self, fr, to):
        self._html = replace_tag(self._html, fr, to)
        return self

    def _img2md(self):
        self._html = img2md(self._html)
        return self

    def _format_lines(self):
        self._html = format_lines(self._html)
        return self

    def read(self):
        return self._format_lines()._html

    def pure_html_l0(self):
        return self._trans_symbol(symbol_map)

    def remove_ptag_l1(self):
        return self.pure_html_l0()._replace_tag('p', '\n')

    def md_preview_l2(self):
        return self.remove_ptag_l1()._trans_tags_in_scope('pre', '')._replace_tag('pre', '\n```\n')

    def convert_md_tags_l3(self):
        return self.pure_html_l0()._trans_tags_in_scope('pre', '')._tags2md(tags_map)

    def img_url_md_l4(self):
        return self.convert_md_tags_l3()._img2md()

    def pure_text_but_pre_l8(self):
        return self.md_preview_l2()._img2md()._empty_tags()

    def pure_text_l9(self):
        return self.pure_html_l0()._img2md()._empty_tags()


def trans_symbol(text, mapping):
    for k, v in mapping.items():
        text = text.replace(k, v)
    return text


def trans_tags_in_scope(text, tag_scope, to=''):
    def clear_tags(match):
        tags = []
        for tag in clearable_tags:
            tags.append('<%s>' % tag)
            tags.append('</%s>' % tag)
        options = '%s' % '|'.join(tags)
        return re.sub(options, to, match.group(0))

    pattern = re.compile(r'(<%s>.*?</%s>)' % (tag_scope, tag_scope), re.S)
    pure_text = re.sub(pattern, clear_tags, text)
    return pure_text


def add_surround_space4tag(text, tag):
    front = re.compile(r'(?<!\s)(?P<content><%s>.*?</%s>)' % (tag, tag), re.S)
    back = re.compile(r'(?P<content><%s>.*?</%s>)(?!\s)' % (tag, tag), re.S)
    text = re.sub(front, ' \g<content>', text)
    return re.sub(back, '\g<content> ', text)


def replace_tag(text, fr, to):
    pattern = re.compile(r'<%s>(?P<content>.*?)</%s>' % (fr, fr), re.S)
    return re.sub(pattern, '{t}\g<content>{t}'.format(t=to), text)


def format_lines(text):
    pattern = re.compile(r'(?P<space>(\s*\n){2,})')
    return re.sub(pattern, '\n\n', text)


def tags2md(text, mapping):
    for k, v in mapping.items():
        text = add_surround_space4tag(text, k)
        text = replace_tag(text, k, v)
    return text


def img2md(text):
    pattern = re.compile(r'<img.*?src="(?P<url>.*?)".*?>')
    return re.sub(pattern, '![](\g<url>)', text)


def pretty(html):
    # 1. deal symbols
    html = trans_symbol(html, symbol_map)
    # 2. remove tags in <pre>
    html = trans_tags_in_scope(html, 'pre')
    # 3. replace tags
    html = tags2md(html, tags_map)
    # 4. format img url
    html = img2md(html)
    # 5. format lines
    html = format_lines(html)
    return html


if __name__ == '__main__':
    t = '''<p>给定 <em>n</em> 个非负整数 <em>a</em><sub>1</sub>，<em>a</em><sub>2，</sub>...，<em>a</em><sub>n，</sub>每个数代表坐标中的一个点&nbsp;(<em>i</em>,&nbsp;<em>a<sub>i</sub></em>) 。在坐标内画 <em>n</em> 条垂直线，垂直线 <em>i</em>&nbsp;的两个端点分别为&nbsp;(<em>i</em>,&nbsp;<em>a<sub>i</sub></em>) 和 (<em>i</em>, 0)。找出其中的两条线，使得它们与&nbsp;<em>x</em>&nbsp;轴共同构成的容器可以容纳最多的水。</p>

<p><strong>说明：</strong>你不能倾斜容器，且&nbsp;<em>n</em>&nbsp;的值至少为 2。</p>

<p><img alt="" src="https://aliyun-lc-upload.oss-cn-hangzhou.aliyuncs.com/aliyun-lc-upload/uploads/2018/07/25/question_11.jpg" style="height: 287px; width: 600px;"></p>

<p><small>图中垂直线代表输入数组 [1,8,6,2,5,4,8,3,7]。在此情况下，容器能够容纳水（表示为蓝色部分）的最大值为&nbsp;49。</small></p>

<p>&nbsp;</p>

<p><strong>示例:</strong></p>

<pre><strong>输入:</strong> [1,8,6,2,5,4,8,3,7]
<strong>输出:</strong> 49</pre>'''
    print Html2md(t).img_url_md_l4().read()
