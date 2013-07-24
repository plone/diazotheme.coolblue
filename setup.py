from setuptools import setup, find_packages
import os

version = '0.1'

setup(name='diazotheme.coolblue',
      version=version,
      description="",
      long_description=open("README.rst").read() + "\n" +
                       open(os.path.join("docs", "CHANGES.rst")).read(),
      classifiers=[
        "Framework :: Plone",
        "Programming Language :: Python",
        ],
      keywords='',
      author='TH-code',
      author_email='t.jonkman@gmail.com',
      url='https://github.com/TH-code',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['diazotheme'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          'z3c.jbot',
      ],
      entry_points="""
      [z3c.autoinclude.plugin]
      target = plone
      """,
      )
