
from setuptools import setup

setup(
    name='eto',
    version='0.2.0',
    description=(
        'Library for estimating reference andnpotential evapotranspiration.'
    ),
    long_description=open('README.rst').read(),
    author='Mark Richards',
    author_email='mark.l.a.richardsREMOVETHIS@gmail.com',
    license='BSD 3-Clause',
    url='None',
    packages=['pyeto'],
    test_suite='tests',
)
