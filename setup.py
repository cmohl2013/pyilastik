import os

from setuptools import setup, find_packages
from pip.req import parse_requirements

requirements_txt = os.path.join(os.path.dirname(__file__), 'requirements.txt')
install_reqs = parse_requirements(requirements_txt, session=False)
reqs = [str(ir.req) for ir in install_reqs]

def readme():
    README_md = os.path.join(os.path.dirname(__file__), 'README.md')
    with open(README_md) as f:
        return f.read()


setup(name='pyilastik',
      version='0.0.1',
      description='Read ilastik labels in python',
#      long_description=readme(),
      author='Manuel Schoelling',
      author_email='manuel.schoelling@dzne.de',
      packages=find_packages(exclude=['contrib', 'docs', 'tests*']),
      zip_safe=False,
      install_requires=reqs,
      test_suite='nose.collector',
      tests_require=['nose', 'coverage', 'nose-timer', 'nose-deadline'])
