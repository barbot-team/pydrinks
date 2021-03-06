# setup.py for pyserial
#
# windows installer:
#  python setup.py bdist_wininst

import sys

from distutils.core import setup

try:
    from distutils.command.build_py import build_py_2to3 as build_py
except ImportError:
    if sys.version_info >= (3, 0):
        raise ImportError("build_py_2to3 not found in distutils - it is required for Python 3.x")
    from distutils.command.build_py import build_py
    suffix = ""
else:
    suffix = "-py3k"


if sys.version < '2.3':
    # distutils that old can't cope with the "classifiers" or "download_url"
    # keywords and True/False constants and basestring are missing
    raise ValueError("Sorry Python versions older than 2.3 are no longer"
                     "supported - check http://pyserial.sf.net for older "
                     "releases or upgrade your Python installation.")

setup(
    name = "pydrinks" + suffix,
    description = "Python Library for BarBot v0.1 'Little Brobot'",
    version = "0.1",
    author = "Chris Woodall, Benjamin Havey",
    author_email = "chris.j.woodall@gmail.com, benhavey@bu.edu",
    url = "n/a",
    packages = ['lib/pydrinks'],
    license = "Python",
    long_description = "Python Library for making mixed drinks with BarBot v0.1 'Little Brobot'",
    classifiers = [
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Intended Audience :: End Users/Desktop',
        'License :: OSI Approved :: Python Software Foundation License',
        'Natural Language :: English',
        'Operating System :: POSIX',
        'Operating System :: Microsoft :: Windows',
        #~ 'Operating System :: Microsoft :: Windows :: Windows CE', # could work due to new ctypes impl. someone needs to confirm that
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.3',
        'Programming Language :: Python :: 2.4',
        'Programming Language :: Python :: 2.5',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.0',
        'Programming Language :: Python :: 3.1',
        'Topic :: Communications',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Terminals :: Serial',
    ],
    requires =['pyserial', 'pyyaml'],
    platforms = 'any',
    cmdclass = {'build_py': build_py},
)
