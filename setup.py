from setuptools import setup, find_packages

setup(
    name="briefme-validator",
    version="0.1.12",
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
    install_requires=["dnspython3", "Django>=2.0"],
    entry_points={"console_scripts": []},
    zip_safe=False,
)
