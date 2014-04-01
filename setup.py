from setuptools import setup

setup(
    name='scrapy-top',
    version='0.0.1',
    description='Real-time metrics for scrapy server',
    long_description=open('README.md').read(),
    license='MIT',

    url='https://github.com/sing1ee/scrapy-top',
    author='Cheng Zhang',
    author_email='zh.milo@gmail.com',

    classifiers=[
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: MIT License',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
    ],
    keywords='cli monitoring scrapy system',

    packages=['scrapy_top'],
    install_requires=['prettytable'],

    entry_points={
        'console_scripts': [
            'scrapy-top = scrapy_top.scrapy_top:main',
        ],
    },
)
