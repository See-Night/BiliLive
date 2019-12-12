数据挖掘
=========================
### mapper.py
```
#!/usr/bin/python3 
# -*- coding: utf-8 -*-

import sys

for line in sys.stdin :
    title = 1
    l = line.strip()
    t = l.split()
    for i in t :
        if i == "child" :
            title = 0
    if title is 1 :
            print(l)

```
- `str.split()` 和 `str.strip()` 对数据进行格式化

### reduce.py
```
#!/usr/bin/python3 
# -*- coding: utf-8 -*-

import sys

f = []
l1 = []
l2 = []

for line in sys.stdin :
    line = line.strip().split()
    for word in line :
        f.append(word)

for i in range(0, len(f), 2) :
    s1 = ['', '']
    s2 = ['', '']
    s1[0], s1[1] = f[i], '1+' + f[i + 1]
    s2[0], s2[1] = f[i + 1], '2+' + f[i]
    l1.append(s1)
    l2.append(s2)
print('grandchild\tgrandparent')
m = 0
try :
    while l1[m][0] :
        x1 = '1+' + l1[m][0]
        x2 = '2+' + l1[m][0]
        for j in range(len(l1)) :
            if x1 in l1[j][1] :
                for k in range(len(l2)) :
                    if x2 in l2[k][1] :
                        print(l1[j][0] + '\t\t' + l2[k][0])
        m = m + 2
except :
    pass

```
- `List.append()` 向列表末尾添加元素  
  
### C.txt
```
child   parent
Steven  Lucy
Steven  Jack
Jone    Lucy
Jone    Jack
Lucy    Mary
Lucy    Frank
Jack    Alice
Jack    Jesse
David   Alice
David   Jesse
Philip  David
Philip  Alma
Mark    David
Mark    Alma
```
### result
```
grandchild      grandparent
Mark            Alice
Mark            Jesse
Philip          Alice
Philip          Jesse
Jone            Alice
Jone            Jesse
Steven          Alice
Steven          Jesse
Jone            Frank
Jone            Mary
Steven          Frank
Steven          Mary```
