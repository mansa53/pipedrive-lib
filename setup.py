import os
from setuptools import setup


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(name='pipedrive-squad',
      version='1.0.0',
      description='Integration Library to Pipedrive written in Python',
      long_description=read('README.md'),
      long_description_content_type="text/markdown",
     
      author='Manasa Hegde',
      author_email='manasahegde503@gmail.com',
      license='MIT',
      packages=['pipedrive'],
      install_requires=[
          'requests',
      ],
      zip_safe=False)
