from setuptools import find_packages,setup
from typing import List

hyphene = '-e .'
def get_required(file_path:str)->List[str]:
  '''this function will return the list of requirements'''
  reqirements = []
  
  with open(file_path) as file_obj:
    requirements = file_obj.readlines()
    requirements = [req.replace("\n","") for req in requirements]
    
    if  hyphene in reqirements:
      requirements.remove(hyphene)
    
setup(
    name='see_me',
    version='0.0.1',  # Version should be a string
    author='jbl302',
    author_email='jaibhagatnet@gmail.com',
    packages=find_packages(),  # find_packages() should be called
    install_requires=get_required('requirements.txt')  # Call the function properly
)
  