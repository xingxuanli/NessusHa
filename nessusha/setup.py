import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="nessusha",
    version="0.2.1",
    author="Li Xingxuan",
    author_email="lxx895466249@gmail.com",
    description="Parse Nessus HA html to xlsx",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/SanPersie",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)