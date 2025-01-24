from setuptools import setup, find_packages

setup(
    name="my_project",                # Package name
    version="0.1.0",                  # Version of your project
    author="Your Name",               # Author name
    author_email="your.email@example.com",  # Author email
    description="A sample Python project", # Short project description
    long_description=open("README.md").read(),  # Detailed description
    long_description_content_type="text/markdown",
    url="https://github.com/username/my_project",  # Project URL (e.g., GitHub repo)
    packages=find_packages(),         # Automatically find Python packages
    install_requires=[                # Dependencies
        "flask",
        "requests",
    ],
    classifiers=[                     # Metadata about your project
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",          # Minimum Python version
)
