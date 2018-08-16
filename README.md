# leetcode files generator
[中文](README-zh.md)

simple tools to generate leetcode exercises files conveniently 

usage:
1. edit `settings.py` and set `src_path` to your source path
2. run the script by giving specified leetcode question id

```python
src_path = "your/source/path"
```
```bash
python gen_lc_files.py [qid]
``` 
**note:** 
1. python version: `2.7`
2. all codes are based on `leetcode-cn.com`, 
if `leetcode.com` version is required, you can commit `issue` or `pull request`
