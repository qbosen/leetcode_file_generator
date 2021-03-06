# leetcode 文件生成器
[English](README.md)

一个简单的工具用来快速生成 `leetcode` 学习所需要的文件

### 使用方式:
```
1. 编辑 `settings.py` 并设置 `src_path` 到目标目录
src_path = "your/source/path"

2. 运行 `search_leetcode.py` 搜索关键字
python search_leetcode.py [keyword]

3. 给定一个题号，运行 `gen_files.py` 生成文件
python gen_files.py {qid}
``` 

### 高级功能:
1. 自动创建方法声明
2. 对问题描述内容，可以自定义格式。`html` 标签到 `markdown` 的转化
3. 内置 `10` 种格式, 从`0-9`, 数字越小，数字越大，`html` 标签越少
4. 获取测试输入数据
5. 支持获取题目描述中的图片
6. 获取题目话题 `topic`
7. 支持更多的语言

在 `settings_advanced.py` 设置 `enable_advance=True` 来开启功能
```
format为可填项
python gen_files.py {qid} [format]
```
### 注意:
1. python version: `2.7`
2. 部分操作是基于本地数据 `dumps.txt`
3. 当前仅支持 `leetcode-cn.com`, 如果需要对 `leetcode.com` 进行支持，可以提交 `issue` 或者 `pull request`
* 高级功能中：
1. format 为`0-9`, 不输入默认为`8`, 数字越大 html 标签越少。对比可参照 [format contrast](Formats.md)
2. 自定义 `markdown` 格式, 用于 `README.md` 中的的题目信息。
通过连续调用 html2md.Html2md()的方法可以完成定制。
需要修改代码。
3. 默认是`java`语言, 配置`language` 时参考 `language_map` 同时需要修改下面的`pattern` 设置，
修改命名空间, 注释风格, 模版等


### 如何更新数据集 `dumps.txt`
使用 `gen_table_readme.py` 来更新 `dumps.txt` 文件或者生产 `README.md`

* 更新 `leetcode` 的本地资源，这个资源是用来加速本地搜索的。
```bash
python gen_table_readme.py update_dumps
```
* 根据 `src_path` 下的包名，生成 索引表文件
```bash
python gen_table_readme.py update_readme
```

### 其他:
此工具已经集成到了 [Alfred](https://www.alfredapp.com) workflow

链接地址: [Find Leetcode](https://github.com/qbosen/Alfred-WorkFlow/tree/master/FindLeetCode)

### 图片:
1. 搜索功能:
![](pic/search.png)
2. 生成文件
![](pic/gen_file.png)
