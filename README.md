# packagegenerator
一个简单的 Python 包框架生成器  

 ### 安装
目前还没上传至 pypi，只能通过源代码安装。  
进入 setup.py 路径，运行
 ```
 python setup.py install
 ```
 
 ### 使用方式
 在安装完成后，获得一个全局命令：pk-gen
 ```
$pk-gen -h
usage: pk-gen [-h] [--template-dir TEMPLATE_DIR | --name NAME] packagename

generate python package framework

positional arguments:
  packagename           the package name

optional arguments:
  -h, --help            show this help message and exit
  --template-dir TEMPLATE_DIR
                        custom template directory path
  --name NAME           use the default template from name
 ```

### 举例说明
```
$pk-gen mytest
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
