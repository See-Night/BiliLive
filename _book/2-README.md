数据分析排序
==============================================
### Mapper.py
```
#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys

for line in sys.stdin :
        line = line.split()
        for num in line :
                print(num)

```
- `Mapper.py` 用于读取数据并传递数据到Reduce
- `sys.stdin` 用于读取数据流  
- `split()` 用于格式化字符串为List列表  

### Reduce.py
```
#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys

cache   = []

for num in sys.stdin :
        num = int(num.split()[0])
        cache.insert(len(cache), num)

t = sorted(cache)

i = 1

for temp in t :
        out = "{}\t{}".format(temp, i)
        i = i + 1
        print(out)

``` 
- `Reduce.py` 用于对数据进行处理
- `sys.stdin` 用于读取数据流
- `split()` 用于格式化字符串为List列表  
- `sorted()` 用于对List列表进行排序操作

### A.txt
```
33
37
12
40
```
### B.txt
```
4
16
39
5
```
### result
```
4
5
12
16
33
37
39
40
```

##### Mapper与Reduce之间的数据传输格式的错误是导致大多数Reduce错误的根本原因