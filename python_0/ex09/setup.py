import setuptools


with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="ft_package",
    version="0.0.1",
    author="gyim",
    author_email="gyim@student.42seoul.kr",
    description="A sample test package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/GihongYim",
    license="MIT",
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="./src"),
    python_requires=">=3.6",
)
