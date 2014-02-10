from setuptools import setup, find_packages


version = '1.2.dev'

setup(
    name='plone.formwidget.recurrence',
    version=version,
    description="Recurrence widgets for Plone",
    long_description="%s\n%s" % (open("README.rst").read(),
                                 open("CHANGES.rst").read()),
    # Get more strings from
    # http://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        "Framework :: Plone",
        "Programming Language :: Python",
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
            'plone.formwidget.recurrence[archetypes, z3cform]',
            'Products.ATContentTypes',
            'Products.GenericSetup',
            'plone.app.testing',
            'plone.app.z3cform',
            'unittest2',
            'z3c.form[test]',
        ]
    ),
    entry_points="""
    # -*- Entry points: -*-
    [z3c.autoinclude.plugin]
    target = plone
    """,
)
