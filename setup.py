try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


setup(
    name='romaji',
    version='0.0.1',
    description='a converter to romanize Japanese hiragana/katakana string',
    long_description=open('README.rst', 'r', encoding='utf-8').read(),
    author='Junnosuke Moriya',
    author_email='shinsen.jikyo@gmail.com',
    url='https://github.com/jikyo/romaji4p',
    license='Apache License 2.0',
    packages=['romaji'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Topic :: Software Development :: Libraries',
        'Natural Language :: Japanese',
    ],
)
