# packagegenerator
一个简单的 Python 包框架生成器  

 ### 安装
目前还没上传至 pypi，只能通过源代码安装。  
进入 setup.py 路径，运行
 ```
 python setup.py install
 ```
 
 ### 使用方式
 在安装完成后，获得一个全局命令：package-generate
 ```
$package-generate -h
usage: package-generate [-h] projectname

generate python package framework

positional arguments:
  projectname  the project name

optional arguments:
  -h, --help   show this help message and exit
 ```

### 举例说明
```
$package-generate mytest
```
将会在当前路径下生成一个标准 python package，填写 setup.py 一些信息后也可以直接通过 `python setup.py install`安装。
```
─mytest
    │  setup.py
    │
    └─mytest
            __init__.py
            __main__.py
```
