<<<<<<< HEAD
from setuptools import find_packages,setup 
from typing import List

HYPEN_E_DOT='-e .'

def get_requirments(file_path:str)-> List[str]:
    '''
    This Function will return the list of requirements
=======
from setuptools import find_packages,setup
from typing import List

HYPEN_E_DOT = '-e .'

def get_requirements(file_path:str) ->List[str]:
    '''
    this function returns a list of requirements for a given file
>>>>>>> 999b7df9a176a8bea1e754505369e61db7f2a12a
    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
<<<<<<< HEAD
        requirements=[req.replace("/n"," ") for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
            
    return requirements
    
 
setup(
name="MLProject",
version='0.0.1',
auther='Avkash',
author_email='khandekaravkash60@gmail.com',
packages=find_packages(),
install_requires=get_requirments('requirements.txt'),


=======
        [req.repalce("\n","") for req in requirements]
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
            
    return requirements        

setup(
name="ML Project",
version="0.0.1",
author='Avkash',
author_email="offavkash98@gmail.com",
packages=find_packages(),
install_requires=get_requirements('requirements.txt'),
>>>>>>> 999b7df9a176a8bea1e754505369e61db7f2a12a
)