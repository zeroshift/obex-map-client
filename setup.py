# On Python for Series 60, use the SIS files instead.

from distutils.core import setup
import sys

setup(name="obex_map_client",
    version="0.1",
    author="Bea Lam",
    author_email="blammit@gmail.com",
    url="http://lightblue.sourceforge.net",
    description="Module for connecting to MAP device.",
    license="GPL",
    classifiers = [ "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: GNU General Public License (GPL)",
        "License :: OSI Approved :: GNU General Public License v3",
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries",
        "Topic :: System :: Networking",
        "Topic :: Communications",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: POSIX :: Linux",
        "Operating System :: Other OS" ]
    )
