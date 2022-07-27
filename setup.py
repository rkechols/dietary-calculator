from setuptools import setup, find_packages


with open("README.md", "r", encoding="utf-8") as f:
    readme_md = f.read()


setup(
    name="dietary-calculator",
    version="0.1.0",
    description="Calculates if certain products are allowed under certain dietary restrictions/requirements, based on their dietary attributes.",
    long_description=readme_md,
    long_description_content_type="text/markdown",
    url="https://github.com/rkechols/dietary-calculator",
    project_urls={
        # "Documentation": "https://packaging.python.org/tutorials/distributing-packages/",
        # "Funding": "https://donate.pypi.org",
        # "Say Thanks!": "http://saythanks.io/to/example",
        # "Source": "https://github.com/pypa/sampleproject/",
        # "Tracker": "https://github.com/pypa/sampleproject/issues",
    },
    author="Ryan Echols",
    author_email="ryan@shadylakemedia.com",
    license="MIT",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        # "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Utilities"
    ],
    # keywords="data structure structures datastructure datastructures tool tools "
    #          "util utils utility utilities",
    python_requires=">=3.8",
    package_dir={"": "src"},
    packages=find_packages(
        where="src"
    ),
    # install_requires=[],
)
