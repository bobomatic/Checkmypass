from setuptools import setup, find_packages

setup(
    name='checkmypass',
    version='1.0',
    packages=find_packages('Checkmypass', 'Checkmypass.*'),
    url='',
    license='',
    author='bobomatic',
    author_email='boxjellyone@tutanota.com',
    description='Check your password has not been hacked',
    install_requires=['certifi==2021.5.30',
                      'charset-normalizer==2.0.6',
                      'idna==3.2',
                      'requests==2.26.0',
                      'urllib3==1.26.7'],
    extras_require='',
    setup_requires='',
    tests_require='',
    package_data=''
    )
