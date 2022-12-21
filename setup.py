from setuptools import find_packages
from setuptools import setup


version = "3.0.0"

setup(
    name="plone.formwidget.recurrence",
    version=version,
    description="Recurrence widget for Plone",
    long_description="%s\n%s" % (open("README.rst").read(), open("CHANGES.rst").read()),
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Framework :: Plone",
        "Framework :: Plone :: 6.0",
        "License :: OSI Approved :: GNU General Public License (GPL)",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
    keywords="Plone Event Recurrence Date Time Widget z3c.form",
    author="Plone Foundation",
    author_email="plone-developers@lists.sourceforge.net",
    url="https://github.com/plone/plone.formwidget.recurrence",
    license="GPL",
    packages=find_packages(),
    namespace_packages=["plone", "plone.formwidget"],
    include_package_data=True,
    python_requires=">=3.8",
    zip_safe=False,
    install_requires=[
        "setuptools",
        "Products.CMFCore",
        "Products.CMFPlone",
        "python-dateutil",
        "zope.component",
        "zope.i18n",
        "zope.i18nmessageid",
        "zope.interface",
    ],
    extras_require=dict(
        z3cform=[
            "z3c.form",
            "zope.schema",
            "zope.traversing",
        ],
        test=[
            "plone.app.testing",
            "plone.testing",
            "plone.app.z3cform",
        ],
    ),
    entry_points="""
    # -*- Entry points: -*-
    [z3c.autoinclude.plugin]
    target = plone
    """,
)
