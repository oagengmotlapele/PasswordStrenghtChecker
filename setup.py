from setuptools import setup, find_packages

setup(
    name="p_s_c",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        # Add your external dependencies here, for example:
        # 'numpy',
    ],
    test_suite="tests",
    author="Oageng Motlapele",
    author_email="oagengmtlapele@gmail.com",
    description="A password strength checker with leak detection",
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
