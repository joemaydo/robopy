from setuptools import setup

setup(
    name='robopy',
    version='0.1.4',
    description='simple lib for robo stuff',
    author='joemaydo',
    author_email='joerg_mueller26@hotmail.com',
    url='https://github.com/joemaydo/robopy.git',
    packages=['robopy',
                'robopy.mainapp',
                'robopy.controller'],


    classifiers=[
        'Development Status :: 1 - Planning',
        'Operating System :: POSIX :: Windows'
        'Programming Language :: Python :: 3.9'
    ],
)
