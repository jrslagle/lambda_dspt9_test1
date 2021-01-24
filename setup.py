import lambdata_james_slagle
import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="lambdata_james_slagle",  # Replace with your own username
    version="0.0.3",
    author="James Slagle",
    author_email="jrslagle@gmail.com",
    description="A small example package for Lambda homework",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/jrslagle/lambda_dspt9_test1",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
