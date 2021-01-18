import lambdata_james_slagle
import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="lambdata_james_slagle",  # Replace with your own username
    version="0.0.1",
    author="James Slagle",
    author_email="jrslagle@gmail.com",
    description="A small example package for Lambda homework",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/jrslagle/lambda_dspt9_test1",
    packages=setuptools.find_packages(),
    # classifiers=[
    #     "Programming Language :: Python :: 3",
    #     "OSI Approved :: GNU General Public License v3 (GPLv3)",
    #     "Operating System :: OS Independent",
    # ],
    python_requires='>=3.6',
)
