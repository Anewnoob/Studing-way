# os.path (Python 2.7+)

import os

### 获取当前文件路径

path = os.path.dirname(__file__)  or os.path.dirname(.)

### 获取父级目录

path = os.path.dirname(file_name)

### 获取绝对路径

abs_path = os.path.abspath(file_name)

### 获取相对路径

real_path = os.path.relpath(path)

### 路径拼接

path = os.path.join(pathA,pathB) #pathA/pathB

### 路径或文件是否存在

os.path.exist(path)

### 获取最后一个斜杠之后的字符串

os.path.basename(path)

### 路径分割

(dir,basename) = os.path.split(path)


# Pathlib (python 3.4+)

from pathlib import path

#define a object

p = Path(r'/Anewnoob/project/test.txt.bk')

p.name  #test.txt.bk  获取文件名

p.stem #test.txt  获取除后缀的文件名

p.suxffix #.bk  获取文件后缀

p.suffixs #{.txt, .bk}  文件的所有后缀

p.parent #/Anewnoob/project/  文件所在目录

p.parent #返回一个iterable, 包含所有父目录

for i in p.parents:
    print(i)
    
p.parts #将路径通过分隔符分割成一个元祖

p.stat()  #获取文件详细信息

p.stat().st_
