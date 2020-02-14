import os
from setuptools import setup, find_packages


# Utility function to read the README file.
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


VERSION = '0.1'

setup(
    name='digilocker',
    version=VERSION,

    packages=find_packages(),

    url='',

    author='Shrihari Shastry',
    author_email='shriharishastrysmg@gmail.com',

    description='Python client library for Digilocker Partner API V.1.6 : https://www.brightpearl.com',
    long_description=read('README.md'),
    license='MIT',

    keywords=['digilocker', 'api', 'client'],
)