from setuptools import setup, find_packages

from validator import __version__

setup(
    name="briefme-validator",
    version=__version__,
    description="An email validator.",
    long_description="""A simple validator, check mail for example.""",
    keywords="dns, email, validator",
    author="Brief.me",
    author_email="tech@brief.me",
    url="https://github.com/briefmnews/briefme-validator",
    license=None,
    classifiers=[
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "Framework :: Django",
        "Framework :: Django :: 2.2",
        "Programming Language :: Python :: 3.7",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Programming Language :: Python",
        "Operating System :: OS Independent",
    ],
    packages=find_packages(),
    include_package_data=False,
    install_requires=["dnspython3", "Django>=3.0"],
    entry_points={"console_scripts": []},
    zip_safe=False,
)
