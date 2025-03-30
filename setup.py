from setuptools import setup, find_packages

setup(
    name="coinglass-api-v3",
    version="1.0.0",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        "requests>=2.28.0",
        "typing-extensions>=4.4.0",
        "python-dotenv>=1.0.0",
        "websocket-client>=1.7.0",
    ],
    extras_require={
        "test": [
            "pytest==8.1.1",
            "pytest-mock==3.12.0",
        ],
    },
    python_requires=">=3.7",
    author="GuiltyMorishita",
    author_email="",
    description="Coinglass APIへのアクセスを簡素化するPythonライブラリ",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/GuiltyMorishita/coinglass-api-v3",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
)
