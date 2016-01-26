from setuptools import setup

long_description = open('README.rst').read()

setup(
    name='ktorrent',
    version='0.4.5',
    description='Fetches and parses data from Kickass Torrents.',
    long_description=long_description,
    license='MIT',
    author='Udit Vasu',
    author_email='admin@codenirvana.in',
    url='https://github.com/codenirvana/kTorrent',
    packages=['ktorrent'],
    install_requires=[
        "beautifulsoup4==4.4.1",
        "requests==2.8.1"
    ],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'License :: OSI Approved :: MIT License',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Topic :: Internet',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Utilities',
    ],
    test_suite='nose.collector',
    tests_require=['nose']
    )
