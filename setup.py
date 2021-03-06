# Always prefer setuptools over distutils
from setuptools import setup
# To use a consistent encoding
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='mdutils',

    # Versions should comply with PEP440.  For a discussion on single-sourcing
    # the version across setup.py and the project code, see
    # https://packaging.python.org/en/latest/single_source_version.html
    version='0.4.2',

    description='Python package for working with Markdown. Includes `docxtomd`, a Word .docx to Markdown converted using `pandoc` and `wmf2svg`, and `wmftosvgpng`, an intelligent WMF to SVG or PNG converter using `wmf2svg`.',
    long_description=long_description,

    # The project's main homepage.
    url='https://github.com/twardoch/markdown-utils',
    download_url='https://github.com/twardoch/markdown-utils/archive/master.zip',

    # Author details
    author='Adam Twardoch',

    # Choose your license
    license='LICENSE.txt',

    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        'Environment :: MacOS X',
        'Operating System :: MacOS :: MacOS X', 
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 3 - Alpha',

        # Indicate who your project is intended for
        'Intended Audience :: Developers',
        'Topic :: Text Processing :: Markup',

        # Pick your license as you wish (should match "license" above)
        'License :: OSI Approved :: Apache Software License',

        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        'Programming Language :: Python :: 2.7',
    ],

    # What does your project relate to?
    keywords=['Markdown', 'typesetting', 'pandoc', 'word', 'docx', 'wmf', 'svg'], 

    # You can just specify the packages manually here if your project is
    # simple. Or you can use find_packages().
    packages=['mdutils'],

    # List run-time dependencies here.  These will be installed by pip when
    # your project is installed. For an analysis of "install_requires" vs pip's
    # requirements files see:
    # https://packaging.python.org/en/latest/requirements.html
    install_requires=['scour>=0.35', 'pandocfilters>=1.4.1', 
        'Markdown>=2.6.7', 'pymdown-extensions>=1.2', 'markdown-include>=0.5.1', 'mdx_sections>=0.1', 
        'markdown-figures>=0.0.3', 'markdown-wikilinks>=0.0.3',
        ],
    dependency_links = [
     'git+https://github.com/twardoch/markdown-figures.git/@master#egg=markdown-figures-0.0.3',
     'git+https://github.com/twardoch/markdown-wikilinks.git/@master#egg=markdown-wikilinks-0.0.3',
    ],

    # To provide executable scripts, use entry points in preference to the
    # "scripts" keyword. Entry points provide cross-platform support and allow
    # pip to create the appropriate form of executable for the target platform.
    entry_points={
        'console_scripts': [
            'docxtomd=mdutils.docxtomd:main',
            'wmftosvgpng=mdutils.wmftosvgpng:main',
        ],
    },
)
