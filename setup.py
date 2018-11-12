'''
Created on Nov 12, 2018

@author: yangzh
'''
from setuptools import setup, find_packages


with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='data_py',
    version='0.1.0',
    description='Data Processing with Python',
    long_description=readme,
    author='Yun',
    author_email='leopard.yun@gmail.com',
    url='https://github.com/yunleopard',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)