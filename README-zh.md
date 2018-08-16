# leetcode 文件生成器
[English](README.md)

一个简单的工具用来快速生成 `leetcode` 学习所需要的文件

使用方式:
1. 编辑 `settings.py` 并设置 `src_path` 到目标目录
2. 给定一个题号，运行 `gen_lc_files.py` 脚本吧

```python
src_path = "your/source/path"
```
```bash
python gen_lc_files.py [qid]
``` 
**注意:** 
* python version: `2.7`
* 当前仅支持 `leetcode-cn.com`, 如果需要对 `leetcode.com` 进行支持，可以提交 `issue` 或者 `pull request`
