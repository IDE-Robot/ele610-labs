# ELE610 - Image Acquisition (IA) part

Resources:
* The subject page on Canvas, including code, video lectures and supporting documents
* The (official) <a href="https://docs.python.org/3.11/index.html"> Python documentation </a>
* The (official) <a href="https://docs.python.org/3.11/reference/index.html"> Python reference </a>
* The web page from <a href="https://www.datacamp.com/cheat-sheet/category/python"> DataCamp </a> includes many cheat sheets. Cheat sheet for numpy, SciPy, linear algebra, and more are available here
* A good Python <a href="https://perso.limsi.fr/pointal/_media/python:cours:mementopython3-english.pdf"> Cheat sheet </a> with much information compressed to two pages
* Bernd Klein <a href="https://python-course.eu/index.php"> Python course </a>
* <a href="https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_tutorials.html"> OpenCV tutorial </a>
* <a href="https://doc.qt.io/qt-6/"> The official Qt documentation </a>

## Installation and use
For ease of installation and setup this repository includes a "requirements.txt" file that can be used by <a href="https://pypi.org/project/pip/"> pip </a> (package installer) to install the required packages/libraries used in this course. You can also install additional packages by using "pip" directly, or by adding them to the requirements-file yourself. Having the requirements-file updated will help you/teammates make sure you have all required packages installed. VSCode offers good support for Python and <a href="https://jupyter.org/"> Jupyter Notebooks </a>, and offers easy setup of both "Virtual environment" and installing required packages with minimal effort. It is recommended that you also check the "requirements.txt" file, and check the packages in the list. The repository also includes a list of useful/recommended VSCode extensions that you might find useful, including:
* "Python"
* "Qt for Python"
* "GitLens" (if you are planning to use git this could be useful)

## Installing software:
The first thing to do here, if it is not already done, is to install Python. Python should be installed on the office computers in E462 and E464. More information is also available in the "Fragments of Python stuff" document. Make the decisions appropriate for you, do the necessary installations, and check that everything is as it should be.

### Python
You can choose Python version yourself, and easily switch between different versions of Python using "virtual environment". Python 3.10 or 3.12 was used for testing/writing the lab notebooks and would be the safest choice. (3.11 might very well work)

<a href="https://www.python.org/downloads/"> Download Python here </a>

### Camera driver (IDS software suite)
The IDS software suite (a zip-file) can be downloaded from <a href="https://en.ids-imaging.com/downloads.html"> IDS web-pages </a> (find downloads for the relevant camera model). An alternative is to download it from this <a href="https://liveuis-my.sharepoint.com/:u:/g/personal/2900780_uis_no/EbSHJPqJeMhPqYiXylktUZwBIGcgPdnQ3UcFQ4BI6nuCQg?e=xhuLb6"> OneDrive link </a>

### VSCode
VSCode can be found on <a href="https://code.visualstudio.com/download"> https://code.visualstudio.com/download </a>

If you are planning to use that as your IDE, then follow the installation instructions according to your platform (Windows/Linux/Mac). This guide is based on using Windows 11, however it should be similar for Linux/Mac.

### Creating/Using a "Virtual environment" (In VSCode):
* Download (or clone) this repository, and open using "open folder" in VSCode
* Open a Python file or .ipynb (Notebook) file
* Python file: Click on the bottom right corner to “Select interpreter”.  This “field” could also be a version number of the already selected python interpreter.
* ipynb file: Press "Select kernel" (top right)
* Choose a venv or "Create Virtual Environment …"
* Select the Python interpreter you want to use for the virtual environment. If the version of python you want to use is not in the list, choose path or install it, and restart VSCode
* If you want to automatically install the python packages in the "requirements.txt" file, select it and press OK. VSCode will then try to install the required packages (this repository contains a requirements.txt file)

### Command line (Powershell) / VSCode terminal:
https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/
* Go to the folder containing the python project/files

For Windows:
* You can create a virtual environment by running the command:
```console
py -m venv .venv
```

* To activate the virtual environment run the command:
```console
.\.venv\Scripts\Activate.ps1
```

* To install the required packages run:
```console
pip install -r .\requirements.txt
```

If you get an error when starting the virtual environment on windows you might have to change the execution policy to allow running the script (you can also change to "-Scope Process"). You can do this by running the command:
```console
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

### Check / verify installation:
You can now open ia_lab_1.ipynb and use the script cell in 1.3 to check that VSCode/your system is set up to run Python including the required libraries. If something is missing or an error appears while fetching required packages you might need to check that it is available for the python version you are using (one common error). Read the error message and check with a search engine, ask for help if needed.

### Known/common OpenCV Error:
* E: "ImportError: DLL load failed while importing cv2"
* S: Could be missing "Windows Media Pack" or Visual C++ redistributable 2015

Windows Media Pack:
* The instructions are a little out of date, but I believe they would solve the issue
* Go to Windows -> Settings -> Uninstall/Install Apps
* Go to Optional Features
* Go to Add button
* Look for Windows Media Pack

