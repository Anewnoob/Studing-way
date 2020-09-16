# 依赖包 (Python 2.7+)

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


