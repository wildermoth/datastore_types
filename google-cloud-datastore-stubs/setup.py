from setuptools import setup, find_packages

setup(
    name="google-cloud-datastore-stubs",
    version="2.21.0",
    description="Type stubs for google-cloud-datastore",
    long_description=open("../README.md").read(),
    long_description_content_type="text/markdown",
    author="Type Stubs Contributor",
    packages=find_packages(),
    package_data={
        "google-cloud-datastore-stubs": ["py.typed", "**/*.pyi"],
        "google.cloud.datastore": ["py.typed", "*.pyi"],
    },
    include_package_data=True,
    zip_safe=False,
    python_requires=">=3.7",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Typing :: Typed",
    ],
)
