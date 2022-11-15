import pathlib
import setuptools

HERE = pathlib.Path(__file__).parent
README = (HERE / "README.md").read_text()

setuptools.setup(
    name="TN_code",
    version="1.4",
    description="Code gebruikt bij de opleiding TN van de Haagse Hogeschool",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://hhs-tn.github.io",
    license="MIT",
    author="Derek Land",
    author_email="d.d.land@hhs.nl",
    packages=setuptools.find_packages(
        exclude=("voorbeelden"),
    ),
    install_requires=[
        "numpy",
        "matplotlib",
        "pandas",
        "sympy",
    ],
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Natural Language :: Dutch",
        "Programming Language :: Python :: 3",
        "Topic :: Utilities",
    ],
)
