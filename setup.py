import os

from setuptools import setup


HERE = os.path.dirname(__file__)
README = open(os.path.join(HERE, 'README.rst')).read()
CHANGES = open(os.path.join(HERE, 'CHANGES.rst')).read()

setup(
    name='sphinxtools',
    version=0.1,
    description='Paver tasks for Sphinx Search server',
    long_description=README + '\n\n' + CHANGES,
    license="New BSD License",
    author='Janne Vanhala',
    author_email='janne.vanhala@gmail.com',
    install_requires=[
        'paver >= 1.0'
    ],
    url='https://github.com/jpvanhal/sphinxtools',
    py_modules=['sphinxtools'],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Indexing/Search',
        'Topic :: Software Development',
    ],
    keywords='paver sphinxsearch'
)
