def vcs2codeHelp():
    print ("vcs2code syntax error: Source file (json)")
    print ("Ex: vcs2code D:\\vrm\\task\\itsm_incident_task.json D:\\vrm\\task\\unpack")

def filtration(sourceFile):
    import re

def vcs2code(sourceFile, unpackFilePath):
    import json
    # data = filtration(sourceFile)
    # obj = json.loads(data) 
    resultFileDescriptor = open(sourceFile, "w", encoding="utf-8")
    resultFileDescriptor.write(json.dumps(obj, sort_keys=True, indent=4))