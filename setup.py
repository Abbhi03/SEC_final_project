from setuptools import find_packages,setup
from typing import List

def get_requirements()->List[str]:
    """
    to return list of requirements
    
    """
    requirement_list:List[str]=[]
    try:
        with open('requirements.txt','r') as file:
            #to read lines from the files
            lines =file.readlines()
            ##process each line
            for line in lines:
                requirement=line.strip()
                ##ignore empty lines and -e. 
                if requirement and requirement!= '-e .':
                    requirement_list.append(requirement)
    except FileNotFoundError:     
        print("requirements.txt file not found")

    return requirement_list

print(get_requirements())  

setup(
    name="SEC_final_project",
    version="0.0.1",
    author="Abhinav Yadav",
    author_email="yadavabhinav48@ce.du.ac.in",
    packages=find_packages(),
    install_requires = get_requirements()
)