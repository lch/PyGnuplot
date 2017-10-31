try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(name='PyGnuplot',
      py_modules=['PyGnuplot'],
      version='0.11.4',
      license='MIT',
      description='Python Gnuplot wrapper',
      author='Ben Schneider',
      author_email=' ',
      url='https://github.com/benschneider/PyGnuplot',
      download_url='https://github.com/benschneider/PyGnuplot/archive/0.11.0.tar.gz',
      keywords=['gnuplot', 'plot'],
      install_requires=['numpy'],
      classifiers=["Topic :: Scientific/Engineering",
                   "License :: OSI Approved :: MIT License",
                   "Programming Language :: Python :: 2.7",
                   "Programming Language :: Python :: 3.6",
                   "Development Status :: 4 - Beta"],
      )
