from setuptools import setup

setup(
    name='ktorrent',
    version='0.1.0',
    description='Fetches and parses data from Kickass Torrents.',
    license='MIT',
    author='Udit Vasu',
    author_email='admin@codenirvana.in',
    url='https://github.com/codenirvana/kTorrent',
    packages=['ktorrent'],
    install_requires=[
        "beautifulsoup4==4.4.1",
        "requests==2.8.1"
    ],
    test_suite='nose.collector',
    tests_require=['nose']
    )
