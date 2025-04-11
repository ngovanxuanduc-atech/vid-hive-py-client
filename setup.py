from setuptools import setup, find_packages

setup(
    name="vid-hive-client",
    version="1.0.0",
    description="Python client for Vid-Hive API",
    author="Your Name",
    author_email="your.email@example.com",
    packages=find_packages(),
    install_requires=[
        "requests>=2.25.1"
    ],
    python_requires=">=3.6",
    url="https://github.com/your-repo/vid-hive-py-client",  # Add your repository URL
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    long_description=open("README.md").read(),  # Ensure README.md exists
    long_description_content_type="text/markdown",
    include_package_data=True,  # Include non-code files specified in MANIFEST.in
)
