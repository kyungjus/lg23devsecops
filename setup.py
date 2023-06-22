from setuptools import find_packages
from distutils.core import setup

setup(name='owmapi',
      version='0.1',
      description='OpenWeatherMap API Test for DevOps Exercise',
      install_requires=[
          'requests'
      ],
      classifiers=[
          'Programming Language :: Python :: 3.9'
      ],
      keywords=('OpenWeatherMap'),
      url='https://github.com/kyungjus/lg23devsecops',
      author='KyungJun Shin',
      author_email='kyungjus@andrew.cmu.edu',
      packages=find_packages(exclude=['tests']),
      include_package_data=True,
      zip_safe=False,
      long_description='OpenWeatherMap API Test for DevOps Exercise')

