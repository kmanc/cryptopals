from setuptools import setup

with open("README.MD", "r") as f:
    long_description = f.read()

setup(
    name="cryptopals",
    version="0.1.0",
    author="Kevin Conley",
    author_email="kmancxc@gmail.com",
    description="Provides building blocks that can be used to complete Matasano Cryptopals Challenges",
    license="MIT",
    keywords="Python, Crypto, Cryptopals",
    url="https://github.com/kmanc/cryptopals",
    packages=["cryptopals", "cryptopals.attacks", "cryptopals.building_blocks"],
    long_description=long_description,
    python_requires=">=3.6",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Topic :: Utilities"
    ],
    setup_requires=["pytest-runner"],
    tests_require=["pytest"],
)
