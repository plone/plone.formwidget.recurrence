from setuptools import setup, find_packages
import os

version = '1.0'

setup(name='plone.formwidget.recurrence',
      version=version,
      description="Recurrence widgets for Plone",
      long_description=open("README.txt").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      # Get more strings from
      # http://pypi.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        "Framework :: Plone",
        "Programming Language :: Python",
        ],
      keywords='Plone Event Recurrence Date Time Widget Archetypes z3c.form',
      author='Plone Foundation',
      author_email='plone-developers@lists.sourceforge.net',
      url='http://svn.plone.org/svn/collective/',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['plone', 'plone.formwidget'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'Products.Archetypes',
          'python-dateutil',
          'setuptools',
          'z3c.form',
      ],
      extras_require={'test': ['Products.GenericSetup',
                               'z3c.form[test]',
                               'plone.app.testing',
                               'unittest2']},
      entry_points="""
      # -*- Entry points: -*-

      [z3c.autoinclude.plugin]
      target = plone
      """,
      )
