# LAB 3 – PYTHON REVIEW – DEVELOPMENT TOOLS AND CLASSES

## Part 1: Python Programming Review 
### Required Resources
- 1 PC with operating system of your choice
- Virtual Box or VMWare
- DEVASC Virtual Machine

### Setup and first steps
- Start the DEVASC VM
- Open Visual Studio Code
- Open a terminal in Visual Studio Code and check the python version

```bash
python3 -V
```

- Start python

```bash
python3
```

>[!Note]
>Notice `>>>`, indicating you are using python.

>[!Warning]
>You would need to change it to python2 -V if a different device you are using is running version 2.
However, as of January 1, 2020, Python 2 is no longer supported. Therefore, Python 2 is not supported in
this lab or this course.

- Try some basic calculations in python.

![alt text](https://github.com/SvenvG0/DEVNET_EN2_GRSNW/blob/main/Lab%203/Images/operatorTable.png?raw=true)

>[!Note]
>Python follows PEMDAS as order of operations:
>- Parentheses
>- Exponents
>- Multiplication and Division
>- Addition and Subtraction

- Now try printing via multiple ways

```python
"Hello World!"
'Hello World!'
print("Hello World!")
quit()
```

>[!Note]
>`quit()` is used to go out of the python interpreter

### First script

- Make a script by making a new file and giving it the name `hello-world.py`.

![alt text](https://github.com/SvenvG0/DEVNET_EN2_GRSNW/blob/main/Lab%203/Images/HWscript.png?raw=true)

>[!Note]
>Notice the `.py` extension. This marks the file as a file with python commands. A file with commands is called a script.

- Paste the print command in the file and save it.

```python
print("Hello World!")
```

- Open the script in the Visual Studio Code terminal

```bash
python3 labs/devnet-src/python/hello-world.py
```

>[!Tip]
>If you change your working directory to the one your script is saved in, you can use:
> ```python
> python hello-world.py
> ```

- Here is some extra information to use in scripts:

>• Integer - used to specify whole numbers (no decimals), such as 1, 2, 3, and so on. If an integer is entered
with a decimal, the interpreter ignores the decimal. For example, 3.75 is interpreted as 3. \
• Float - used to specify numbers that need a decimal value, such as 3.14159. \
• String - any sequence of characters such as letters, numbers, symbols, or punctuation marks. \
• Boolean - any data type that has a value of either True or False

![alt text](https://github.com/SvenvG0/DEVNET_EN2_GRSNW/blob/main/Lab%203/Images/BooleanOperators.png?raw=true)

- Now use `=` to create some variables and play around with them.

```python
x=3
x*5
Cisco*x
```

- Make a dictionary and see what is possible with those

```python
hostnames=["R1","R2","R3","S1","S2"]
type(hostnames)
len(hostnames)
hostnames
hostnames[0]
```

- You can also change dictionaries

```python
ipAddress={"R1":"10.1.1.1","R2":"10.2.2.1","R3":"10.3.3.1"}
ipAddress["S1"]="10.1.1.10"
ipAddress["R3"]=["10.3.3.1","10.3.3.2","10.3.3.3"]
ipAddress
```

- Try the input function

```python
firstName = input("What is your first name? ")
User_Name
print("Hello " + firstName +"!")
```

- Make a new script named `personal-info.py` and try it out

```python
firstName = input("What is your first name?")
lastName = input("What is your last name?")
location = input("What is your location?")
age = input("What is your age?")
print("Hi " + firstName + " " + LastName + "! Your location is " + location + " and you are " + age + " years old.")
```

- Make a script named `if-vlan.py` and paste the code below

```python
nativeVLAN = 1
dataVLAN = 100
if nativeVLAN == dataVLAN:
 print("The native VLAN and the data VLAN are the same.")
else:
    print("The native VLAN and the data VLAN are different.")
```

- Now try the script and alter between possible outcomes by changing values

- We can also add extra outcomes by using `elif`

```python
aclNum = int(input("What is the IPv4 ACL number? "))
if aclNum >= 1 and aclNum <= 99:
 print("This is a standard IPv4 ACL.")
elif aclNum >=100 and aclNum <= 199:
 print("This is an extended IPv4 ACL.")
else:
 print("This is not a standard or extended IPv4 ACL.")
```

- Save as `if-acl.py` and run the script. Try to get the different outcomes

>[!Tip]
>Change the input each time: 10,110,200

- Explore for loops and while loops:

##### For

```python
devices=["R1","R2","R3","S1","S2"]
for item in devices:
print(item)
```
##### While

```python
while True:
    x=input("Enter a number to count to: ")
    if x == 'q' or x == 'quit':
        break

    x=int(x)
    y=1
    while True:
        print(y)
        y=y+1
        if y>x:
            break
```

- Start a new script with the name `file-access.py.`

```python
devices=[]
file=open("devices.txt","r")
for item in file:
    item=item.strip()
    devices.append(item)
file.close()
print(devices)
```

- Make sure there is a `devices.txt` file, if not create one:

```
Cisco 819 Router
Cisco 881 Router
Cisco 888 Router
Cisco 1100 Router
Cisco 4321 Router
Cisco 4331 Router
Cisco 4351 Router
Cisco 2960 Catalyst Switch
Cisco 3850 Catalyst Switch
Cisco 7700 Nexus Switch
Cisco Meraki MS220-8 Cloud Managed Switch
Cisco Meraki MX64W Security Appliance
Cisco Meraki MX84 Security Appliance
Cisco Meraki MC74 VoIP Phone
Cisco 3860 Catalyst Switch
```
- Now run the script and see what is happening.

- Try using everything you learned to append extra devices:

```python
devices=[]
newItem=""
file=open("devices.txt","a")
while True:
    if (newItem != "exit"):
        newItem = input("Enter new device: ")
        file.write(newItem + "/n")
    else
        print("All done!")
        break
file.close()
file=open("devices.txt","r")
for item in file:
    item=item.strip()
    devices.append(item)
file.close()
print(devices)
```

>[!Note]
>Notice the `a` in the open function. This makes sure we can append.


## Part 2: Explore Python Development Tools 

- Change to the directory `labs/devnet-src/python`

```bash
cd labs/devnet-src/python/
```

- Use this command to make a virtual environment for python

```bash
python3 -m venv devfun
```

>[!Note]
>The -m switch tells Python to run the venv module. The name is chosen by the programmer.

- Install  `requests` package and check what packages are installed

```python
pip3 install requests
pip3 freeze
```

>[!Tip]
>Use `deactivate` to go back to the main system

- Check the packages in the main system

```bash
python3 -m pip freeze
```

>[!Note]
> Because Python 3 is invoked with the following command, you only use pip instead of pip3.

>[!Tip]
>Use grep to quickly find the packages you need

### Share you virtual environment

>[!Note]
> ```bash
> pip3 freeze > requirements.txt
> ```
> can make a required packages list for other developers, while
> ```bash
> pip3 install -r requirements.txt
> ```
> can be used to install all the requirements by the other developers

- Restart the environment

```bash
source devfun/bin/activate
```

- Make a requirement list

```bash
pip3 freeze > requirements.txt
```

- The requirement list should now be in the directory on the main system.

```bash
deactivate
ls
```
- Create a new environment

```bash
python3 -m venv devnew
source devnew/bin/activate
```

- Install the requirements

```python
pip3 install -r requirements.txt
```

- Verify that the packages are installed

```python
pip3 freeze
```

- Close the environment

```python
deactivate
```

## Part 3: Explore Python Classes

- Example of a function:

```
# Define the function
def functionName:
    ...blocks of code...

# Call the function
functionName()
```
- Example of a methode:

```
# Define the class
class className
    # Define a method
    def method1Name
        ...blocks of code

    # Define another method
    def method2Name
        ...blocks of code

    # Define yet another method
    def method3Name
        ...blocks of code

# Instantiate the class
myClass = className()

# Call the instantiation and associated methods
myClass.method1Name()
myClass.method2Name()
myClass.method3Name()
```

### Define a function

- Go to `~/labs/devnet-src/python` and create a new file named `myCity.py`

```python
def myCity(city):
    print("I live in " + city + ".") 

myCity("Austin")
myCity("Tokyo")
myCity("Salzburg")
```

- Save and run the script

```bash
python3 myCity.py
```

### Define a class with methodes

- Review the class with methodes, save the following script as `myLocation.py`

```python
# Define a class with variables for **name** and **country**.
# Then define a method that belongs to the class. The method’s
# purpose is to print a sentence that uses the variables.
class Location:
    def __init__(self, name, country):
        self.name = name
        self.country = country
    def myLocation(self):
        print("Hi, my name is " + self.name + " and I live in " + self.country + ".")
# First instantiation of the Location class
loc1 = Location("Tomas", "Portugal")
# Call a method from the instantiated class
loc1.myLocation()
# Three more instantiations and method calls for the Location class
loc2 = Location("Ying", "China")
loc3 = Location("Amare", "Kenya")
loc2.myLocation()
loc3.myLocation()
your_loc = Location("Your_Name", "Your_Country")
your_loc.myLocation()
```


- Review another script, save this one as `circleClass.py`

>[!Tip]
>The circumference of a circle is calculated.

```python
# Given a radius value, print the circumference of a circle.
# Formula for a circumference is c = pi * 2 * radius
class Circle:
    def __init__(self, radius):
        self.radius = radius

    def circumference(self):
        pi = 3.14
        circumferenceValue = pi * self.radius * 2
        return circumferenceValue

    def printCircumference(self):
        myCircumference = self.circumference()
        print ("Circumference of a circle with a radius of " + str(self.radius) + " is " + str(myCircumference))

# First instantiation of the Circle class.
circle1 = Circle(2)
# Call the printCircumference for the instantiated circle1 class.
circle1.printCircumference()
# Two more instantiations and method calls for the Circle class.
circle2 = Circle(5)
circle2.printCircumference()
circle3 = Circle(7)
circle3.printCircumference()
```

>[!Important]
>The printCircumference method prints a string. Notice that the variables are casted as strings with the
str() function. Otherwise, the print statement would throw an error because self.radius and
myCircumference are not strings
