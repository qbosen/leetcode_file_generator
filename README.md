# Leetcode Files Generator
[中文](README-zh.md)

Simple tools to generate leetcode exercises files conveniently 

### Usage:
```
1. edit `settings.py` and set `src_path` to your source path
src_path = "your/source/path"

2. run `search_leetcode.py` to search `keyword`
python search_leetcode.py [keyword]

3. run `gen_files.py` by giving specified leetcode question id
python gen_files.py [qid]
``` 
### Note:
1. python version: `2.7`
2. some operations are based on the local data `dumps.txt`
3. all codes are based on `leetcode-cn.com`, 
if `leetcode.com` version is required, you can commit `issue` or `pull request`

### How to update `dumps.txt`
There are two files: `html_parser.py` and `default.html`

1. open the website `https://leetcode-cn.com/problemset/all/`
2. open `devTools` of the browser, select the element of question table. 
    the selector is somehow like this `#question-app > ... > table > tbody.reactable-data` 
3. if Chrome is used, right click the `tbody` element in `devTools`, select `edit as HTML`,
    copy and create our html file like `lc-2018-08.html`
4. use `html_parser.py` to parse html file and it will update the `dumps.txt` file 

```bash
python html_parser.py lc-2018-08.html
```

### Others:
The tool is integrated in [Alfred](https://www.alfredapp.com) workflow

Project Link: [Find Leetcode](https://github.com/qbosen/Alfred-WorkFlow/tree/master/FindLeetCode)


### Pictures:
1. Searching questions:
![](pic/search.png)
2. Generate files
![](pic/gen_file.png)
