# coding=utf-8

# options that enable advanced feature
enable_advance = True

# language setting is related to the template code
language = 'java'
comment_symbol = '//'
language_map = {
    'java': '.java', 'c': '.c', 'cpp': '.cpp', 'python': '.py', 'python3': '.py', 'csharp': '.cs',
    'javascript': '.js', 'ruby': '.rb', 'swift': '.swift', 'golang': '.go', 'scala': '.scala', 'kotlin': '.kt'
}

# keep this value false otherwise wrong result you will get
debug_mode = False

# README content format type (0..9)
# style looks more markdown when numbers grow
default_format = 8

# the map of tags and markdown labels
tags_map = {
    'em': '_',
    'strong': '**',
    'p': '\n',
}

# html symbol mapping
symbol_map = {
    '&amp;': '&',
    '&quot;': '"',
    '&lt;': '<',
    '&gt;': '>',
    '&circ;': '^',
    '&tilde;': '~',
    '&nbsp;': ' ',
    '&le;': u'≤',
    '&ge;': u'≥',
    '&#39;': '\'',
    '&ldquo;': '\"',
    '&rdquo;': '\"',
    '&rarr;': u'→',
}
# the tags will be cleared in pre scope when get md preview
# or remain when get html preview
clearable_tags = ['em', 'strong', ]

ad_md_pattern = u'''### {title}
|\t|\t|
|---:|:---|
|题号|{index:0>3s}|
|中文名|{title}|
|英文名|{title_en}|
|难度|{difficulty}|
|通过率|{percent}|
|链接|[{path}](https://leetcode-cn.com/problems/{path}/description/)|
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
 
public class Solution implements Answer {{
    @Override
    public {sign[ret]} {sign[name]}({sign[param]}) {{
        
    }}
}}
'''
ad_interface_pattern = '''package {en_level}.q{index:0>3s};

/**
 * @author {author}
 * @date {date}
 */
 
@FunctionalInterface
public interface Answer {{
    {sign[ret]} {sign[name]}({sign[param]});
}}
'''

ad_test_class_pattern = '''package {en_level}.q{index:0>3s};

import com.rits.cloning.Cloner;
import org.junit.Assert;
import org.junit.BeforeClass;
import org.junit.Test;

/**
 * @author {author}
 * @date {date}
 */
 
public class SolutionTest {{
    private static Cloner cloner;
    private static Answer[] answers;

    @BeforeClass
    public static void init() {{
        cloner = new Cloner();
        answers = new Answer[]{{new Solution()}};
    }}

    @Test
    public void test() {{
        // simpleCase: {case}
        {sign[param_1]} param = null;
        {sign[ret]} expect = null;
        testAnswer(param, expect);
    }}

    private void testAnswer({sign[param_1]} input, {sign[ret]} expect) {{
        for (Answer answer : answers) {{
            {sign[param_1]} param = cloner.deepClone(input);
            {sign[ret]} result = answer.{sign[name]}(param);

            boolean correct = result == expect;
            if (!correct) {{
                String info = String.format("\\nAnswer: %s\\tExpect: %s\\tActual: %s",
                        answer.getClass().getSimpleName(), expect, result);
                Assert.fail(info);
            }}
        }}
    }}
}}
'''

# query part
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
