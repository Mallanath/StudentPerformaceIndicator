from setuptools import find_packages, setup
from typing import List

def get_requirements(filepath: str) -> List[str]:
    """
    This function returns a list of requirements.
    """
    requirements = []
    with open(filepath) as obj:
        requirements = obj.readlines()
        requirements = [req.replace("\n", "") for req in requirements]

        if "-e ." in requirements:
            requirements.remove("-e .")  # Corrected

    return requirements

setup(
    name="studentPerformanceIndicator",
    author="mallanath",
    packages=find_packages(),
    install_requires=get_requirements("requirements.txt")  # Corrected name
)
