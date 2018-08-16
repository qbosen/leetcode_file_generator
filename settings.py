# -*- coding:utf-8 -*-

src_path = "your/src/path"
search_limit = 10

search_display = "{index:0>3s} {level} {percent} {ch_name}"

md_pattern = '''### {title}
|\t|\t|
|---:|:---|
|题号|{index:0>3s}|
|中文名|{ch_name}|
|英文名|{en_name}|
|难度|{level}|
|通过率|{percent}|
|链接|[{path}][desc_url]

```
{content}
```
### 思路 {date}\n\n
[desc_url]:[https://leetcode-cn.com/problems/{path}/description/]'''

class_pattern = '''package {en_level}.q{index};

/**
 * @author {author}
 * @date {date}
 */
public class Solution {{
    
}}
'''

test_class_pattern = '''package {en_level}.q{index};

import static org.junit.Assert.*;
import org.junit.Test;

/**
 * @author {author}
 * @date {date}
 */
public class SolutionTest {{
    @Test
    public void test() {{
        
    }}
}}
'''

detail_url = "https://leetcode-cn.com/problems/%s/description/"

query_url = "https://leetcode-cn.com/problems/api/filter-questions/%s"
