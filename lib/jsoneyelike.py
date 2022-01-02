def filtration(sourceFile):
    import re
    sourceFileDescriptor = open(sourceFile, "r", encoding="utf-8")
    for readString in sourceFileDescriptor:
        readString = re.sub(",}", '}', readString)
        readString = re.sub(",]", ']', readString)
    
        readString = re.sub(", +}", '}', readString)
        readString = re.sub(", +]", ']', readString)
    
        readString = re.sub(",\t+}", '}', readString)
        readString = re.sub(",\t+]", ']', readString)
    return readString

def jsoneyelike(sourceFile):
    import json
    data = filtration(sourceFile)
    obj = json.loads(data) 
    resultFileDescriptor = open(sourceFile, "w", encoding="utf-8")
    resultFileDescriptor.write(json.dumps(obj, sort_keys=True, indent=4))

def jsoneyelikeHelp():
    print ("Syntax error: Source file (json); Destination filenme")
    print ("Ex: jsonax D:\\vrm\\task\\itsm_incident_task.json ready.json")