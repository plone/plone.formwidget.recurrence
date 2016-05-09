from setuptools import setup, find_packages


version = '2.1.0'

setup(
    name='plone.formwidget.recurrence',
    version=version,
    description="Recurrence widget for Plone",
    long_description="%s\n%s" % (open("README.rst").read(),
                                 open("CHANGES.rst").read()),
    classifiers=[
        "Framework :: Plone",
        "Framework :: Plone :: 5.0",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.7",
    ],
    keywords='Plone Event Recurrence Date Time Widget Archetypes z3c.form',
    author='Plone Foundation',
    author_email='plone-developers@lists.sourceforge.net',
    url='https://github.com/plone/plone.formwidget.recurrence',
    license='GPL',
    packages=find_packages(exclude=['ez_setup']),
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
