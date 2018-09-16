import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="life-progress",
    version="0.0.2",
    author="Alex Beal",
    author_email="alex@alb.computer",
    description="Visualize your progress through life",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/beala/life-progress",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=['click', 'dateutil']
)