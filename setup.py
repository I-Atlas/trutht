#!/usr/bin/env python

#!/usr/bin/env python

# Copyright 2019 Ilya Bol
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.

# Package forked from truth-table-generator, a module by Francisco Bustamante
# Main code by Francisco Bustamante

# Copyright 2019 Francisco Bustamante
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.

# Package forked from truths, a module by Trey Morris


from setuptools import setup, find_packages

MAIN_PACKAGE = "Trutht"
DESCRIPTION = "Python API for truth tables"
LICENSE = "Apache Software License"
URL = "https://github.com/I-Atlas/Trutht"
AUTHOR = "Ilya Bol"
EMAIL = "joachim.gotzz@gmail.com"
VERSION = '0.0.1'
KEYWORDS = ['truth', 'table', 'truth table', 'truthtable',
            'logic', 'trutht']


CLASSIFIERS = ['Development Status :: 5 - Production/Stable',
               'Environment :: Console',
               'Intended Audience :: Science/Research',
               'License :: OSI Approved :: Apache Software License',
               'Natural Language :: English',
               'Programming Language :: Python',
               'Programming Language :: Python :: 3',
               'Topic :: Scientific/Engineering :: Mathematics']


DEPENDENCIES = ['numpy', 'pandas', 'PTable', 'pyparsing', 'tabulate', 'jinja2']


def readme():
    """Return the contents of the README.md file."""
    with open('README.md') as freadme:
        return freadme.read()


def setup_package():
    """ Setup instructions """

    setup(name=MAIN_PACKAGE,
          version=VERSION,
          url=URL,
          description=DESCRIPTION,
          long_description_content_type="text/markdown",
          author=AUTHOR,
          author_email=EMAIL,
          include_package_data=True,
          install_requires=DEPENDENCIES,
          keywords=KEYWORDS,
          license=LICENSE,
          long_description=readme(),
          classifiers=CLASSIFIERS,
          packages=find_packages(exclude=['tests', 'tests.*']),
          entry_points={'console_scripts': ['Trutht_cli.py = truth_table.Trutht_cli:clielement']},
          )


if __name__ == "__main__":
    setup_package()
