# Lab 5
## Part 3: Parse Different Data Types with Python
### Prep
- Launch DEVASC VM
- Launch the terminal
```bash
cd ~/labs/devnet-src/parsing
```
### Build a script to parse the XML data
```bash
code parsexml.py
```

add the following to the script:
```python
import xml.etree.ElementTree as ET
import re

xml = ET.parse("myfile.xml")
root = xml.getroot()

ns = re.match('{.*}', root.tag).group(0)
editconf = root.find("{}edit-config".format(ns))
defop = editconf.find("{}default-operation".format(ns))
testop = editconf.find("{}test-option".format(ns))

print("The default-operation contains: {}".format(defop.text))
print("The test-option contains: {}".format(testop.text))
```
Save and run the script and you should get the following output:
>devasc@labvm:~/labs/devnet-src/parsing$ python3 parsexml.py \
The default-operation contains: merge \
The test-option contains: set \
devasc@labvm:~/labs/devnet-src/parsing$

close Visual Studio Code

### Parse JSON in Python
The usual steps:
- Authenticate (user/password|token)
- Execute GET request
- Modify returned JSON
- Execute Post/Put

Example:
>{ \
"access_token":"ZDI3MGEyYzQtNmFlNS00NDNhLWFlNzAtZGVjNjE0MGU1OGZmZWNmZDEwN2ItY \
TU3", \
"expires_in":1209600, \
"refresh_token":"MDEyMzQ1Njc4OTAxMjM0NTY3ODkwMTIzNDU2Nzg5MDEyMzQ1Njc4OTEyMzQ1 \
Njc4", \
"refreshtokenexpires_in":7776000 \
}

```bash
code parsejson.py
```
add the following to the script:
```python
import json
import yaml

with open('myfile.json','r') as json_file:
 ourjson = json.load(json_file)

print(ourjson)

print("The access token is: {}".format(ourjson['access_token']))
print("The token expires in {} seconds.".format(ourjson['expires_in']))

```
>[!Note]
>We are not only printing the JSON data but also data of interest because of the custom print commands.

Save and run the script, you should see this output:
> devasc@labvm:~/labs/devnet-src/parsing$ python3 parsejson.py \
{'access_token': 'ZDI3MGEyYzQtNmFlNS00NDNhLWFlNzAtZGVjNjE0MGU1OGZmZWNmZDEwN2ItYTU3', \
'expires_in': 1209600, 'refresh_token': \
'MDEyMzQ1Njc4OTAxMjM0NTY3ODkwMTIzNDU2Nzg5MDEyMzQ1Njc4OTEyMzQ1Njc4', \
'refreshtokenexpires_in': 7776000} \
1209600 \
The access token is ZDI3MGEyYzQtNmFlNS00NDNhLWFlNzAtZGVjNjE0MGU1OGZmZWNmZDEwN2ItYTU3 \
The token expires in 1209600 seconds \
devasc@labvm:~/labs/devnet-src/parsing$

#### Output parsed JSON data in a YAML data format
add the following to the script:
```python
print("\n\n---")
print(yaml.dump(ourjson))
```

Save and run the script, you should see this output added at the end:
>devasc@labvm:~/labs/devnet-src/parsing$ python3 parsejson.py \
... \
access_token: ZDI3MGEyYzQtNmFlNS00NDNhLWFlNzAtZGVjNjE0MGU1OGZmZWNmZDEwN2ItYTU3 \
expires_in: 1209600 \
refresh_token: MDEyMzQ1Njc4OTAxMjM0NTY3ODkwMTIzNDU2Nzg5MDEyMzQ1Njc4OTEyMzQ1Njc4 \
refreshtokenexpires_in: 7776000 \
devasc@labvm:~/labs/devnet-src/parsing$

### Parse YAML

We are going to use the YAML dump we created in the previous part. \
Build a script to parse the YAML data:
```python
import json
import yaml

with open('myfile.yaml','r') as yaml_file:
 ouryaml = yaml.safe_load(yaml_file)

print(ouryaml)

print("The access token is {}".format(ouryaml['access_token']))
print("The token expires in {} seconds.".format(ouryaml['expires_in']))
```

Save and run the script, you should see this output:
>devasc@labvm:~/labs/devnet-src/parsing$ python3 parseyaml.py \
{'access_token': 'ZDI3MGEyYzQtNmFlNS00NDNhLWFlNzAtZGVjNjE0MGU1OGZmZWNmZDEwN2ItYTU3', \
'expires_in': 1209600, 'refresh_token': \
'MDEyMzQ1Njc4OTAxMjM0NTY3ODkwMTIzNDU2Nzg5MDEyMzQ1Njc4OTEyMzQ1Njc4', \
'refreshtokenexpires_in': 7776000} \
The access token is ZDI3MGEyYzQtNmFlNS00NDNhLWFlNzAtZGVjNjE0MGU1OGZmZWNmZDEwN2ItYTU3 \
The token expires in 1209600 seconds. \
devasc@labvm:~/labs/devnet-src/parsing$

#### Output parsed YAML data in a JSON data format

Just as we did with JSON, add some lines to the script to get an json dump: \
Add the following to the script:
```python
print("\n\n")
print(json.dumps(ouryaml, indent=4))
```

Save and run the script, you should see this output added at the end:
>devasc@labvm:~/labs/devnet-src/parsing$ python3 parseyaml.py \
...
{ \
 "access_token": "ZDI3MGEyYzQtNmFlNS00NDNhLWFlNzAtZGVjNjE0MGU1OGZmZWNmZDEwN2ItYTU3", \
 "expires_in": 1209600, \
 "refresh_token": "MDEyMzQ1Njc4OTAxMjM0NTY3ODkwMTIzNDU2Nzg5MDEyMzQ1Njc4OTEyMzQ1Njc4", \
 "refreshtokenexpires_in": 7776000 \
} \
devasc@labvm:~/labs/devnet-src/parsing$

