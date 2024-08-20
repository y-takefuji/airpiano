import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="airpiano",
    version="0.0.8",
    author="yoshiyasu takefuji",
    author_email="takefuji@keio.jp",
    description="airpiano ",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/y-takefuji/airpiano",
    project_urls={
        "Bug Tracker": "https://github.com/y-takefuji/airpiano",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    py_modules=['airpiano'],
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.8",
    entry_points = {
        'console_scripts': [
            'airpiano = airpiano:main'
        ]
    },
)
