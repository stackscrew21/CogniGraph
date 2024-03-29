from setuptools import setup, find_packages

classifiers = [
    'Development Status :: 5 - Production/Stable',
    'Intended Audience :: Education',
    'Operating System :: Microsoft :: Windows :: Windows 10',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3'
]

setup(
    name='CogniGraph',
    version='0.0.1',
    description='',
    long_description=open('README.txt').read() + '\n\n' + open('CHANGELOG.txt').read(),
    url='',
    author='stacks crew and Ahmed bailgh',
    author_email='ahmedgamejd1992@gmail.com',
    license='MIT',
    classifiers=classifiers,
    keywords='Graph',
    packages=find_packages(),
    install_requires=['']
)