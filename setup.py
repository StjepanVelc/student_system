from setuptools import setup, find_packages

setup(
    name="student_system",
    version="0.1.0",
    packages=find_packages(),
    description="A simple student management system.",
    author="Stjepan Velc",
    author_email="",
    install_requires=[],
    entry_points={"console_scripts": ["student-system=student_system.app.main:main"]},
)
