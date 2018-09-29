A common problem when trying to install R packages locally in the workplace can be problems with permissions which restrict the ability to run the standard R code below: 

> install.packages("tidyverse")

This python code locates and downloads the R packages that you need and provides the text you need to paste into R to install these locally installed packages.

Note that this code was inspired by [this stackoverflow answer](https://stackoverflow.com/questions/17077494/how-do-i-convert-a-ipython-notebook-into-a-python-file-via-commandline)

## Getting Started

In order to use this code, first make sure prerequisite python3 packages are installed (see below). Next make a clone of this repository and open a terminal in this folder and type the following:

> python3 Download_local-R-package.py

Text will appear in the terminal asking "What are the package names?". Type the packages separated by a comma and press the ENTER key. 

Each package will then be located and downloaded to the folder where you have saved the local_R_install repository. 
The necessary R code to install these packages will then be outputted. Simply open up R studio and copy the output from the terminal into the R studio console and your packages should install!

**Note that you can easily copy from the terminal using CTRL+SHIFT+C.**

### Prerequisites

This code is dependent on having python3 and pip3 installed and the following python3 packages: requests. 
Either install these or, if you are less familiar with python, open a terminal in the repository folder and type the following:

> bash install_dependencies.sh

## Authors
* **Graham Cooper** -- [CoopG](https://github.com/CoopG)
* **Dan Carpenter** -- [dansebcar](https://github.com/dansebcar)
