# Package Generate

一个简单的 Python 包框架生成器，目的是为了方便快速构建一个全局命令行参数。而不必每次都构建类似的结构和去敲那些类似的代码。  

### 安装

通过 pypi 安装  

```
pip install package-gen
```

或者通过本地安装。进入 setup.py 路径，运行  
 ```
 python setup.py install
 ```
 
 ### 使用方式
 在安装完成后，获得一个全局命令：pk-gen
 ```
$pk-gen -h
usage: pk-gen [-h] [-l | --name NAME | --template-dir TEMPLATE_DIR]
              [packagename]

generate python package

positional arguments:
  packagename           the package name

optional arguments:
  -h, --help            show this help message and exit
  -l, --list            list the default template names and exit
  --name NAME           use the default template from name
  --template-dir TEMPLATE_DIR
                        custom template directory path
 ```

### 举例说明

#### 最小使用

```
$pk-gen mytest
```
将会在当前路径下生成一个标准 python package  
```
─mytest
    │  setup.py
    │
    └─mytest
            __init__.py
            __main__.py
```

可以在 setup.py 中自定义自己需要的全局命令，将 your_custom_command 换成自己需要的命令即可。所生成的模块即可直接通过 `python setup.py install` 安装，或者 `python setup.py develop` 进行实时调试。  
```
# setup.py
import setuptools

setuptools.setup(
    name="mytest",
    version="",
    author="",
    author_email="",
    description="",
    packages=setuptools.find_packages(),
    include_package_data=True,
    entry_points={
        "console_scripts": [
            "your_custom_command=mytest:main",
        ]
    }
)
```

```
# __init__.py
import argparse


def main():
    parser = argparse.ArgumentParser(description='')

    # add argparse parameters here

    args = parser.parse_args()

    # handle arguments

```

目前内置有多个模板，默认模板为 base。通过 `pk-gen -l` 可以查看当前内置的可使用的所有模板名。可以将模板拷贝出去自己订制，将 `--template-dir` 参数指向自己自定义的模板位置即可。  
