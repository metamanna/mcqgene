# to store local package in virtual environment
from setuptools import find_packages,setup

setup(
    name='mcqgenerator',
    version='0.0.1',
    author='tamanna aggarwal',
    author_email='tamanna08aggarwal@gmail.com',
    install_requires=["openai","langchain","streamlit","python-dotenv","PyPDF2"],
    packages=find_packages()
)