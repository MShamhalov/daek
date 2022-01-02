def jsoneyelike(sourceFile, destFile):
    import json
    with open(sourceFile, 'r') as myfile:
        data = myfile.read()
    obj = json.loads(data) 
    resultFileDescriptor = open(destFile, "w", encoding="utf-8")
    resultFileDescriptor.write(json.dumps(obj, sort_keys=True, indent=4))

def jsoneyelikeHelp():
    print ("Syntax error: Source file (json); Destination filenme")
    print ("Ex: jsonax D:\\vrm\\task\\itsm_incident_task.json ready.json")