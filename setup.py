import setuptools

setuptools.setup(
    name="packagegenerator",
    version="0.0.2",
    author="",
    author_email="",
    description="generate python package framework",
    packages=setuptools.find_packages(),
    include_package_data=True,
    entry_points={
        "console_scripts": [
            "package-generate=packagegenerator:main",
        ]
    },
)