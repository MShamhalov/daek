def csv2json(sourceFile, resultFile, tableName, separator):
    sourceFileDescriptor = open(sourceFile, "r", encoding="utf-8-sig")
    resultFileDescriptor = open(resultFile, "w", encoding="utf-8")

    i = 1
    resultFileDescriptor.write('{"' + tableName + '":') 
    resultFileDescriptor.write("[")
    for readString in sourceFileDescriptor:
        if (i == 1):
            tableHead = readString.split(separator)
            i += 1
        else:
            tableBody = readString.split(separator)
            j = 0
            resultFileDescriptor.write("{")
            for currentElem in tableHead:
                currentElem = currentElem.replace('\n', '')
                tableBody[j] = tableBody[j].replace('\n', '')
                resultFileDescriptor.write('"' + currentElem + '": ')
                if tableBody[j].isdigit():
                    resultFileDescriptor.write(tableBody[j])
                elif tableBody[j] == 'true' or tableBody[j] == 'false':
                    resultFileDescriptor.write(tableBody[j])
                elif tableBody[j] == '':
                    resultFileDescriptor.write('null')
                else: resultFileDescriptor.write('"' + tableBody[j] + '"')
                
                if (currentElem != tableHead[-1]):
                    resultFileDescriptor.write(",")
                j += 1
            resultFileDescriptor.write("},")
    resultFileDescriptor.write("]")
    resultFileDescriptor.write('}')

def csv2jsonHelp():
    print ("Syntax error: Source file (csv); Destination file (json); Table name; Separator")
    print ("note: The incoming file must be in utf-8 with bom format! (Ms Excel utf-8 export file)")
    print ("Ex: csv2json D:\\vrm\\task\\itsm_incident_task.csv D:\\vrm\\task\\ready_task.json itsm_incident_task ;")
