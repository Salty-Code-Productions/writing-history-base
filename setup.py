from setuptools import setup, find_packages

setup(
    name="writing-history-base",
    version="1.0.0",
    description="Base FastAPI app, settings, and logging utilities for Writing History services.",
    url="https://github.com/Salty-Code-Productions/writing-history-base",
    author="Salty Code Productions",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    include_package_data=True,
    python_requires=">=3.10",
    install_requires=[
        "fastapi>=0.115.0",
        "pydantic-settings>=2.3.0",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
    ],
    keywords=["fastapi", "pydantic", "settings", "logging"],
    project_urls={
        "Source": "https://github.com/Salty-Code-Productions/writing-history-base",
    },
)
