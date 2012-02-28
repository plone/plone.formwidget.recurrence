from setuptools import setup, find_packages
import os

version = '1.0b2'

setup(name='plone.formwidget.recurrence',
      version=version,
      description="Recurrence widgets for Plone",
      long_description=open("README.rst").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.rst")).read(),
      # Get more strings from
      # http://pypi.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        "Framework :: Plone",
        "Programming Language :: Python",
        ],
      keywords='Plone Event Recurrence Date Time Widget Archetypes z3c.form',
      author='Plone Foundation',
      author_email='plone-developers@lists.sourceforge.net',
      url='https://github.com/collective/plone.formwidget.recurrence',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['plone', 'plone.formwidget'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'python-dateutil',
          'setuptools',
      ],
      extras_require=dict(
          z3cform=[
              'z3c.form',
          ],
          archetypes=[
              'Products.Archetypes',
          ],
          test=[
              'Products.GenericSetup',
              'z3c.form[test]',
              'plone.app.testing',
              'unittest2'
          ]),
      entry_points="""
      # -*- Entry points: -*-

      [z3c.autoinclude.plugin]
      target = plone
      """,
      )
