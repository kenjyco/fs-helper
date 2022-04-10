from setuptools import setup, find_packages


with open('README.rst', 'r') as fp:
    long_description = fp.read()

setup(
    name='fs-helper',
    version='0.0.8',
    description='CLI helpers for filesystem and logging tasks',
    long_description=long_description,
    author='Ken',
    author_email='kenjyco@gmail.com',
    license='MIT',
    url='https://github.com/kenjyco/fs-helper',
    download_url='https://github.com/kenjyco/fs-helper/tarball/v0.0.8',
    packages=find_packages(),
    include_package_data=True,
    package_dir={'': '.'},
    package_data={
        '': ['*.ini'],
    },
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries',
        'Topic :: System :: Filesystems',
        'Topic :: System :: Logging',
        'Topic :: Utilities',
    ],
    keywords=['filesystem', 'logging', 'files', 'helper', 'kenjyco']
)
