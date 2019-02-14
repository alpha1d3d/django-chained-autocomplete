# read the contents of your README file
from os import path

from setuptools import setup

this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='django-chained-autocomplete',
    version='0.0.1',
    description='Chain autocomplete dropdowns in django admin.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.6',
    ],
    keywords='django autocomplete chained filtered',
    url='http://github.com/alpha1d3d/django-autocomplete-chained',
    author='Jonathan Loo',
    author_email='alpha1d3d@hotmail.com',
    license='MIT',
    packages=[
        'autocomplete_chained',
    ],
    zip_safe=False,
    python_requires='>=3.6',
    install_requires=[
        'django',
    ]
)
