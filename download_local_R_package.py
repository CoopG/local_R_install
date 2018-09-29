import requests, shutil, re, os

# define preset terms
BASE_URL = "https://cran.r-project.org"
REG_EXP = r"bin\/macosx\/el-capitan\/contrib\/3\.5\/[\w.]+"
FILE_REG_EXP = r"contrib\/3\.5\/([\w.]+)"

#input package name
packages = input("What are the package names? ")

outputs = []

for package in packages.split(", "):
    info_url = "/".join([BASE_URL, "web/packages", package, "index.html"])
    response = requests.get(info_url)
    file_path_list = re.findall(REG_EXP, response.text)
    file_url = "/".join([BASE_URL, file_path_list[0]])
    file_response = requests.get(file_url, stream=True)
    if file_response.status_code == 200:
        file_name = re.search(FILE_REG_EXP, file_url).group(1)
        with open(file_name, 'wb') as f:
            file_response.raw.decode_content = True
            shutil.copyfileobj(file_response.raw, f)
    package_path = '"' + "/".join([str(os.getcwd()), file_name]) + '"' 
    outputs.append("install.packages(" + package_path + ", repos = NULL, type=" + '"' + "source" + '")')
    if os.path.exists(file_name):
        print("Successfully downloaded package " + package + " to " + file_name)
    else:
        print("Problem downloading package " + package)

print("Copy the following into your R studio console to install packages: \n" + '; '.join(outputs))

