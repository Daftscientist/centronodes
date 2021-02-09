import setuptools

with open("README.md", "r", encoding="utf-8", errors="ignore") as fh:
    long_description = fh.read()

setuptools.setup(
    name="centronodes",
    version="0.3",
    author="centronodes",
    description="Simple API Wrapper for centronodes api.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Daftscientist/centronodes",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>= 3.6',
    include_package_data=True,
    install_requires=["requests"]
)
