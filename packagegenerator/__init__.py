import os
import re
import sys
import argparse


def is_all_english(data):
    result = re.match(r'^[\-a-zA-Z]+$', data)
    if result:
        return True
    else:
        return False


def show_message(message):
    print(message)
    sys.exit()


def create_file(path, data):
    with open(path, 'w', encoding='utf-8')as fl:
        fl.write(data)


def generate_package(projectname):

    if '-' in projectname:
        packagename = projectname.replace('-', '_')
    else:
        packagename = projectname

    base_path = os.path.abspath('.')
    package_path = os.path.join(base_path, projectname)
    package_sub_path = os.path.join(package_path, packagename)

    os.makedirs(package_sub_path)
    
    # create __init__.py and __main__.py
    init_code = '''def main():
    pass
'''
    main_code = '''import os
import sys


path = os.path.dirname(__file__)
sys.path.insert(0, os.path.dirname(path))

from {} import main

if __name__ == '__main__':
    main()
'''.format(packagename)
    create_file(os.path.join(package_sub_path, '__init__.py'), init_code)
    create_file(os.path.join(package_sub_path, '__main__.py'), main_code)

    # create setup.py
    setup_code = '''import setuptools

setuptools.setup(
    name="{projectname}",
    version="0.0.1",
    author="",
    author_email="",
    description="",
    packages=setuptools.find_packages(),
    include_package_data=True,
    entry_points={{
        "console_scripts": [
            "yourcommand={packagename}:main",
        ]
    }},
)
'''.format(projectname=projectname, packagename=packagename)
    create_file(os.path.join(package_path, 'setup.py'), setup_code)

    print('{} generate successfully.'.format(package_path))

def main():
    parser = argparse.ArgumentParser(
        description='generate python package framework')
    parser.add_argument('projectname', help='the project name')

    args = parser.parse_args()

    projectname = args.projectname.strip()

    if len(projectname) == 0:
        show_message('projectname must not be null')
    if not is_all_english(projectname):
        show_message('projectname must be all english charactors')
    if projectname in os.listdir():
        show_message('ERROR: {} already existed!'.format(projectname))

    generate_package(projectname)
