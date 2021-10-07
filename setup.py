from setuptools import setup, find_packages

setup(
    name='checkmypass',
    version='1.0',
    packages=find_packages(['password', 'password.*']),
    url='',
    license='',
    author='bobomatic',
    author_email='boxjellyone@tutanota.com',
    description='Check your password has not been hacked'
)
