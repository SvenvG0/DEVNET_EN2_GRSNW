# Lab 1: PYTHON EXPERIMENTS
## Part 1: Install different tools/packages on Ubuntu DEVASC-LABVM:
### Task preparation and implementation:
- Update system
    - ```sudo apt update -y```
    - ```sudo apt upgrade -y```
- Install Python 3.8 (+ Python IDLE)
    - ```sudo apt install python3.8```
- Install PIP
    - ```sudo apt install python3-pip```
- Install Visual Studio Code
    - Download Visual Studio Code
    - ```sudo apt install <filelocation>```
- Install Jupyter Notebook
    - ```pip3 install jupyter```

>[!Note]
>If any of these are already installed on your system but you only want to check the installation and the version, use the commands as explained in `task verification`


### Task troubleshooting:

- Incompatible versions
    - Install correct depedencies
    (`pip install <dependency>`)
- ImportError on IDLE
    - ```sudo apt-get install python3-tk```

### Task verification:
- Python 3.8
    - ```python3 --version```
- PIP
    - ```pip3 --version```
- Visual Studio Code
    - ```code --version```
- Jupyter Notebook
    - ```jupyter --version```
- Python IDLE
    - ```idle-python3.8```


## Part 2: Run geopy and timedate Python Scripts on the DEVASC-LABVM using the tools from part 1:
### Task preparation and implementation:
- Open the terminal
    - Python:
        - ```python3 timedate.py```
    - Visual Studio Code:
        - ```code```
        - Open timedate.py && Run
        - Open geopy-geocoders_location.py && Run
        - Open location.py && Run
    - Jupyter Notebook:
        - ```jupyter notebook```
        - ```%run timedate.py```
        - ```%run geopy-geocoders_location.py```
        - ```%run location.py```
    - IDLE:
        - ```idle-python3```
         - Open timedate.py && Run
        - Open geopy-geocoders_location.py && Run
        - Open location.py && Run



### Task troubleshooting:
- "No Module named geopy":
    - ```sudo pip3 install geopy```
- "No module named folium":
    - ```sudo pip3 install folium```

### Task verification:
- timedate.py:
    - Check time and date
- geopy-geocoders_location.py:
    - Check location result
- location.py:
    - Check location result

## Part 3: Install different tools/packages on Windows OS
### Task preparation and implementation:
- Install Python 3.8 (+ Python IDLE)
    - Download Python 3.8 (official website)
    - follow installation instructions

>[!Important]
>Make sure you activate the option to add python to `PATH` in the firsts steps!
- Install PIP
    - open terminal
    - ```python3 -m pip install --upgrade pip```
- Install PIP-packets
    - Open terminal
    - ```pip3 install requests```
    - ```pip3 install geopy```
    - ```pip3 install folium```
- Install Visual Studio Code
    - Download Visual Studio Code
    - Follow installation instructions
- Install Jupyter Notebook
    - ```pip3 install jupyter```

### Task troubleshooting:
- Microsoft Visual C ++ `<version>` or greater is required:
    - Download Build Tools (Visual studio 2022)
    - Install Build Tools
    - Retry: ```pip3 install jupyter```


### Task verification:
Open the different tools.

## Part 4: Install different tools/packages on Ubuntu 22.04.01 LTS
### Task preparation and implementation:
- Python:
    - ```sudo apt install software-properties-common```
    - ```sudo add-apt-repository ppa:deadsnakes/ppa```
    - ```sudo apt update -y```
    - ```sudo apt upgrade -y```
    - ```sudo apt install python3.8```
- PIP:
    - ```sudo apt install python3-pip```
- PIP-packets:
    - ```sudo pip install geopy```
    - ```sudo pip install folium```
- Visual Studio Code:
    - ```sudo apt install software-properties-common apt-transport-https wget```
    - ```wget -q https://packages.microsoft.com/keys/microsoft.asc -O- | sudo apt-key add -```
    - ```sudo add-apt-repository "deb [arch=amd64] https://packages.microsoft.com/repos/vscode stable main```
    - ```sudo apt update -y```
    - ```sudo apt install code```
- Jupyter Notebook:
    - ```sudo apt install jupyter-notebook```
- IDLE:
    - ```sudo apt install idle-python3.8```

### Task troubleshooting:

### Task verification:
- Python: 
    - ```python3.8 --version```
- PIP:
    - ```sudo apt install python3-pip```
- PIP-packets:    
    - ```pip3 show geopy```
    - ```pip3 show folium```
- Visual Studio Code:    
    - ```code```
- Jupyter Notebook:
    - ```jupyter-notebook```
- IDLE:
    - ```idle-python3.8```
