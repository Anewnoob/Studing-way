# f = open(file_name,mode,encoding)

mode = {r,w,a,r+,w+,a+}  # r+: 读写模式  w+:写读模式  a+：写读模式

f.read()

f.readlines() #读取文件所有内容，按行存储在列表中

f.write(contents)

f.seek() #将光标移到文件开头

f.tell() #获取光标当前位置

# example 1:
f = open("text.txt", mode = 'r', encoding = 'uft-8')

res = f.read()

f.close()


# example 2:

with open("text.txt", mode = 'r', encoding = 'uft-8') as f:

    res = f.read()
   

# example 3:
f = open('e:\\123.txt',mode='a+',encoding='gbk')  # 在 a+ 模式下，将在文件的末尾追加数据，不会覆盖原来的内容

f.write('\njack is a student')

f.seek(0)  # 将光标移动到文件开头

print(f.read())

f.close()
 
