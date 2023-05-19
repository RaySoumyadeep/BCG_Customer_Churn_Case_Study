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