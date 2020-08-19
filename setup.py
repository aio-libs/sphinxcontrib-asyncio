import codecs
import os
import re
from setuptools import setup
from setuptools.command.test import test as TestCommand

with codecs.open(os.path.join(os.path.abspath(os.path.dirname(
        __file__)), 'sphinxcontrib', 'asyncio.py'), 'r', 'latin1') as fp:
    try:
        version = re.findall(r"^__version__ = '([^']+)'\r?$",
                             fp.read(), re.M)[0]
    except IndexError:
        raise RuntimeError('Unable to determine version.')


install_requires = ['sphinx>=3.0']


def read(f):
    return open(os.path.join(os.path.dirname(__file__), f)).read().strip()


class PyTest(TestCommand):
    user_options = []

    def run(self):
        import subprocess
        import sys
        errno = subprocess.call([sys.executable, '-m', 'pytest', 'tests'])
        raise SystemExit(errno)


tests_require = install_requires + ['pytest']


setup(
    name='sphinxcontrib-asyncio',
    version=version,
    description=('sphinx extension to support coroutines in markup'),
    long_description='\n\n'.join((read('README.rst'), read('CHANGES.rst'))),
    classifiers=[
        'Environment :: Plugins',
        'Framework :: AsyncIO',
        'Framework :: Sphinx :: Extension',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Topic :: Documentation :: Sphinx',
        'Topic :: Software Development :: Documentation'],
    author='Andrew Svetlov',
    author_email='andrew.svetlov@gmail.com',
    url='https://github.com/aio-libs/sphinxcontrib-asyncio',
    license='Apache 2',
    packages=['sphinxcontrib'],
    install_requires=install_requires,
    tests_require=tests_require,
    include_package_data=True,
    cmdclass=dict(test=PyTest))
