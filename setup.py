from setuptools import setup, find_packages

setup(
    name='bracketeer',
    description='Python Library for testing march madness brackets',
    version='0.5.0',
    author='Charlie Haley',
    author_email='charlie.haley@gmail.com',
    url='https://github.com/joowani/binarytree',
    download_url='https://github.com/cshaley/bracketeer/archive/0.5.0.tar.gz',
    packages=find_packages(),
    include_package_data=True,
    license='MIT',
    classifiers=[
        'Intended Audience :: Developers',
        'Intended Audience :: End Users/Desktop',
        'Intended Audience :: Information Technology',
        'License :: OSI Approved :: MIT License',
        'Operating System :: POSIX',
        'Operating System :: MacOS',
        'Operating System :: Unix',
        'Operating System :: Microsoft :: Windows',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
    ]
)