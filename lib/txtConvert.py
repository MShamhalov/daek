def socsv2json(sourceFile, resultFile, separator, tableName):
    sourceFileDescriptor = open(sourceFile, "r", encoding="utf-8")

    i = 1
    resultFile.write('{"' + tableName + '":') 
    resultFile.write("[")
    for readString in sourceFileDescriptor:
        if (i == 1):
            tableHead = readString.split(separator)
            i += 1
        else:
            tableBody = readString.split(separator)
            j = 0;
            resultFile.write("{")
            for currentElem in tableHead:
                currentElem = currentElem.replace('\n', '')
                tableBody[j] = tableBody[j].replace('\n', '')
                resultFile.write('"' + currentElem + '": ')
                if tableBody[j].isdigit():
                    resultFile.write(tableBody[j])
                elif tableBody[j] == '':
                    resultFile.write('null')
                else: resultFile.write('"' + tableBody[j] + '"')
                if (currentElem != tableHead[-1]):
                    resultFile.write(",")
                j += 1
            resultFile.write("},")
    resultFile.write("]")
    resultFile.write('}')

def sojson2csv():
    print ("sojson2csv: under construction")