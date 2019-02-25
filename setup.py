from setuptools import setup


setup(
    name="cryptopals",
    version="0.0.1",
    author="Kevin Conley",
    author_email="kmanc@comcast.net",
    description="Matasano cryptopals challenges",
    license='MIT',
    keywords="Python, Crypto",
    url="https://github.com/kmanc/cryptopals",
    packages=['cryptopals'],
    long_description='',
    python_requires='>=3.6',
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Topic :: Utilities"
    ],
    setup_requires=['pytest-runner'],
    tests_require=['pytest'],
)
