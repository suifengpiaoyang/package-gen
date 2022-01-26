import setuptools

setuptools.setup(
    name="packagegenerator",
    version="0.0.2",
    author="Zhang",
    author_email="",
    url = 'https://github.com/suifengpiaoyang/packagegenerator',
    description="Generate python package",
    packages=setuptools.find_packages(),
    include_package_data=True,
    entry_points={
        "console_scripts": [
            "pk-gen=packagegenerator:main",
        ]
    },
    python_requires='>=3.6.0'
)