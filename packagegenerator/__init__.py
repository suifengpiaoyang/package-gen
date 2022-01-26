import os
import re
import sys
import shutil
import argparse
from string import Template


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
TEMPLATES_DIR = os.path.join(BASE_DIR, 'templates')


def is_all_ascii(data):
    result = re.match(r'^[\-a-zA-Z0-9]+$', data)
    if result:
        return True
    else:
        return False


def show_message(message):
    print(message)
    sys.exit()


def generate_file(old, new, options=None):
    with open(old, 'r', encoding='utf-8')as fl:
        content = fl.read()
    new_content = render_from_text(content, options)
    with open(new, 'w', encoding='utf-8')as fl:
        fl.write(new_content)


def render_from_text(template, options):
    s = Template(template)
    return s.substitute(**options)


def generate_package(packagename, template_dir):

    options = {}
    if '-' in packagename:
        options['packagename_format'] = packagename.replace('-', '_')
    else:
        options['packagename_format'] = packagename
    options['packagename'] = packagename

    new_base_path = os.path.abspath('.')
    new_package_path = os.path.join(new_base_path, packagename)

    if os.path.exists(new_package_path):
        show_message(f'{new_package_path} existed!')

    os.makedirs(new_package_path)

    template_dir_length = len(template_dir)
    for root, dirs, files in os.walk(template_dir):
        new_root = root[template_dir_length + 1:]
        if '$' in new_root:
            new_root = render_from_text(new_root, options)
        new_root = os.path.join(new_package_path, new_root)
        if not os.path.exists(new_root):
            os.makedirs(new_root)
        for file in files:
            old = os.path.join(root, file)
            if file.endswith('-tmpl'):
                file = file.replace('-tmpl', '')
            new = os.path.join(new_root, file)
            generate_file(old, new, options)
    print(f'[{packagename}] generated successfully.')


def main():
    parser = argparse.ArgumentParser(
        description='generate python package framework')
    parser.add_argument('packagename', help='the package name')
    template_group = parser.add_mutually_exclusive_group()
    template_group.add_argument(
        '--template-dir', help='custom template directory path')
    template_group.add_argument(
        '--name', help='use the default template from name')

    args = parser.parse_args()

    packagename = args.packagename.strip()

    if len(packagename) == 0:
        show_message('packagename must not be null')
    if not is_all_ascii(packagename):
        show_message('packagename must be all english charactors')
    if packagename in os.listdir():
        show_message(f'ERROR: [{packagename}] already existed!')

    template_dir = None
    if args.template_dir is None and args.name is None:
        template_dir = os.path.join(TEMPLATES_DIR, 'base')
    if args.template_dir is not None:
        template_dir = args.template_dir
    if args.name is not None:
        args.name = args.name.strip()
        templates = os.listdir(TEMPLATES_DIR)
        if args.name not in templates:
            show_message(f'Template [{args.name}] not in default templates!')
        else:
            template_dir = os.path.join(TEMPLATES_DIR, args.name)
    if template_dir is None:
        show_message('Can not fetch any template path!')
    template_dir = os.path.abspath(template_dir)
    if not os.path.exists(template_dir):
        show_message(f'Error:{template_dir} does not exist!')

    generate_package(packagename, template_dir)
