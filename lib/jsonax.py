import re

def getTableName (sourceFile):
    # Получаем навименовние таблицы
    sourceFileDescriptor = open(sourceFile, "r", encoding="utf-8")
    for currentString in sourceFileDescriptor: 
        tn = re.search(r'(\w+)', currentString)
        if (tn != None):
            return tn
            break

def headAndTail (sourceFile):
    with open(sourceFile, 'r') as f:
        result = f.readlines()[2:-2]
    return result

def fileCreator (stringCollector, currentInformationGroup, tableName, destinationPath):
    pathToFile = destinationPath + "\\" + tableName + str(currentInformationGroup) + ".json"
    resultFileDescriptor = open(pathToFile, "w", encoding="utf-8")
    
    resultFileDescriptor.write('{\n\t"'+ tableName +'": [\n')
    for currentStr in stringCollector:
        resultFileDescriptor.write(currentStr)
    resultFileDescriptor.close
    resultFileDescriptor.write('\t]\n}')

# основная функция
def jsonax (sourceFile, destinationPath, NumOfRec):
    import sys
    
    countInformationBlockInOneGroup = int(NumOfRec)
    currentInformationGroup = 0 
    currentInformationBlock = 0
    stringCollector = []

    tableName = getTableName(sourceFile).group()
    # print (tableName)
    content = headAndTail(sourceFile) 
    # print (content)
    i = 0
    for currentString in content:
        i += 1
        stringCollector.append(currentString)
        endInfBlockSym = re.search(r'(})', currentString)
        if endInfBlockSym != None: # Достигнут конец информационного блока
            currentInformationBlock += 1
            # print (currentInformationBlock)
            # print (currentString)
            if (currentInformationBlock == countInformationBlockInOneGroup) or (i == len(content)): # Достигнут конец инфоромацинной группы (или конец файла)
                currentInformationBlock = 0
                currentInformationGroup += 1
                stringCollector[-1] = re.sub("},", '}', stringCollector[-1])
                fileCreator(stringCollector, currentInformationGroup, tableName, destinationPath)
                stringCollector = []
    
def jsonaxHelp():
    print ("Syntax error: Source file (json); Destination path; Number of records")
    print ("Ex: jsonax D:\\vrm\\task\\itsm_incident_task.json D:\\vrm\\task 4000")