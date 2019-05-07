import json

def getjson(filepath):
    with open(filepath,'r') as file1:
        return json.load(file1)

myobj=getjson("reading.json")

print(myobj.get("glossary"))
