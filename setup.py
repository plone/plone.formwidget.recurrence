from setuptools import setup, find_packages


version = '2.1.4'

setup(
    name='plone.formwidget.recurrence',
    version=version,
    description="Recurrence widget for Plone",
    long_description="%s\n%s" % (open("README.rst").read(),
                                 open("CHANGES.rst").read()),
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Framework :: Plone",
        "Framework :: Plone :: 5.0",
        "Framework :: Plone :: 5.1",
        "Framework :: Plone :: 5.2",
        "License :: OSI Approved :: GNU General Public License (GPL)",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
    keywords='Plone Event Recurrence Date Time Widget Archetypes z3c.form',
    author='Plone Foundation',
    author_email='plone-developers@lists.sourceforge.net',
    url='https://github.com/plone/plone.formwidget.recurrence',
    license='GPL',
    packages=find_packages(),
    namespace_packages=['plone', 'plone.formwidget'],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'setuptools',
        'Products.CMFCore',
        'Products.CMFPlone',
        'python-dateutil',
        'zope.component',
        'zope.i18n',
        'zope.i18nmessageid',
        'zope.interface',
    ],
    extras_require=dict(
        z3cform=[
            'z3c.form',
            'zope.schema',
            'zope.traversing',
        ],
        archetypes=[
            'Products.Archetypes',
            'Products.validation',
        ],
        test=[
            'Products.ATContentTypes',
            'Products.GenericSetup',
            'plone.app.testing',
            'plone.app.z3cform',
            'plone.formwidget.recurrence[archetypes, z3cform]',
        ]
    ),
    entry_points="""
    # -*- Entry points: -*-
    [z3c.autoinclude.plugin]
    target = plone
    """,
)
