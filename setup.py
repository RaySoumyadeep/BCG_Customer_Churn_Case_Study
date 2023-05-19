'''
 The setup.py is a Python script typically included with Python-written libraries or apps. Its objective is to ensure that the program is installed correctly. With the aid of pip, we can use the setup.py to install any module without having to call setup.py directly. The setup.py is a standard Python file.
'''

from setuptools import find_packages, setup
from typing import List


HYPHEN_E_DOT = '-e .'
def get_requirements(file_path:str) -> List[str]:
    '''
    This function will return a list of requirements
    '''
    requirements=[]
    with open(file_path, 'r') as f:
        requirements=f.readlines()
        [req.replace("\n","") for req in requirements]

        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)
    
    return requirements

setup(
    name='BCG_Customer_Churn_Case_Study',
    version='0.0.1',
    author='Soumyadeep',
    author_email='soumyadeepray95@gmail.com',
    packages=find_packages,
    install_requires=get_requirements('requirements.txt')
)