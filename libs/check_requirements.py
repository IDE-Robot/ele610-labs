"""
This script checks the current Python environment and verifies the installation
of required modules listed in a 'requirements.txt' file.

Usage:
    python check_requirements.py
Note:
    The 'requirements.txt' file should be in the same directory as this script.
"""
import sys
PYTHON_V_STR = (
    f"Current Python version: {sys.version_info.major}."
    f"{sys.version_info.minor}.{sys.version_info.micro}"
)

class CheckRequirements:
    '''Class to assist checking the Python environment and required modules.'''
    def __init__(self, requirements_file='../requirements.txt'):
        self.requirements_file = requirements_file
        self.package_to_import = {
            'opencv-python': 'cv2',
            # Add more mappings here if needed
        }
        self.messages = []
        self.py_version = ""
    def check_os(self):
        import platform
        import sys
        # Check operating system
        if platform.system() == 'Windows':
            import win32api
            version_info = win32api.GetVersionEx()
            major, minor, build = version_info[:3]
            if major == 10 and build >= 22000:
                self.os_version = ("Operating System: Windows 11")
            else:
                self.os_version = (f"Operating System: Windows {major}.{minor} (Build {build})")
        elif platform.system() == 'Linux':
            self.os_version = platform.linux_distribution()
        elif platform.system() == 'Darwin':
            self.os_version = platform.mac_ver()

    def check_system_version(self):
        '''Check the Python version and environment.'''
        if hasattr(sys, 'real_prefix') or (
            hasattr(sys, 'base_prefix') and sys.base_prefix != sys.prefix
        ):
            self.py_version = (PYTHON_V_STR + " - venv: Yes")
        else:
            self.py_version = (PYTHON_V_STR + " - venv: No")

    def check_requirements(self):
        '''Check required modules from requirements file.'''
        self.messages = []
        try:
            with open(self.requirements_file, 'r', encoding='utf-8') as file:
                requirements = file.readlines()
        except FileNotFoundError:
            print("requirements.txt file not found.")
            requirements = []
        for requirement in requirements:
            module = requirement.strip().split('==')[0]
            if not module or requirement.startswith('#'):
                continue
            import_name = self.package_to_import.get(module, module)
            try:
                __import__(import_name)
            except ImportError:
                self.messages.append(f"The module '{module}' (import as '{import_name}') is not installed.")

    def check_lab_1_requirements(self):
        '''Check the requirements for Lab 1.'''
        self.messages = []
        try:
            import numpy as np
            # Check numpy version
            self.messages.append(f"Numpy Version: {np.__version__}")
        except:
            self.messages.append("Numpy not installed. Please install numpy using 'pip install numpy'")
        try:
            import cv2
            # Check OpenCV version
            self.messages.append(f"OpenCV Version: {cv2.__version__}")
        except:
            self.messages.append("OpenCV not installed. Please install OpenCV using 'pip install opencv-python'")
        try:
            from PyQt6.QtCore import QT_VERSION_STR
            # Check Qt version
            self.messages.append(f"Qt Version: {QT_VERSION_STR}")
        except:
            self.messages.append("PyQt6 not installed. Please install PyQt6 using 'pip install PyQt6'")

        try:
            from pyueye import ueye
            self.messages.append("pyueye installed and working.")
        except ModuleNotFoundError as e:
            self.messages.append("PyuEye module is not installed. Please install pyueye to use this module.")
        except ImportError as e:
            if str(e).__contains__("DLL_PATH"):
                self.messages.append("uEye software is not installed. Please install ueye to use pyueye.")
        try:
            import qimage2ndarray
            self.messages.append("qimage2ndarray installed and working.")
        except:
            self.messages.append("qimage2ndarray not installed. Please install qimage2ndarray using 'pip install qimage2ndarray'")

if __name__ == '__main__':
    check = CheckRequirements()
    check.check_os()
    check.check_requirements()
    for message in check.messages:
        print(message)
    if not check.messages:
        print("All required modules are installed.")
    sys.exit()
