# coding=utf-8

enable_advance = True

query_keys = [
    'questionId',
    'questionTitle',
    'translatedTitle',
    'translatedContent',
    'difficulty',
    'stats',
    'codeDefinition',
    'sampleTestCase',
    r'topicTags{name\n translatedName}'
]

debug_mode = True
language = 'java'

convert_tags = {
    'em': '_',
    'strong': '**',
    'p': '\n'
}

clearable_tags = ['em', 'strong', ]

ad_md_pattern = u'''### {title}
|\t|\t|
|---:|:---|
|题号|{index:0>3s}|
|中文名|{title}|
|英文名|{title_en}|
|难度|{difficulty}|
|通过率|{percent}|
|链接|[{path}](https://leetcode-cn.com/problems/{path}/description/)
|标签|{topics}|
|topics|{topics_en}|

{content}

### 思路 {date}
'''

ad_class_pattern = '''package {en_level}.q{index:0>3s};

/**
 * @author {author}
 * @date {date}
 */
{codes}
'''

ad_test_class_pattern = '''package {en_level}.q{index:0>3s};

import static org.junit.Assert.*;
import org.junit.Test;

/**
 * @author {author}
 * @date {date}
 */
public class SolutionTest {{
    @Test
    public void test() {{
        // simpleCase: {case}
    }}
}}
'''
