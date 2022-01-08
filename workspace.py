def executor(command):
    #from conf import getModules
    #modules = getModules()  
    parameter = command.split(' ')
    if parameter[0] == 'csv2json':
        if len(parameter) == 5:
            from csv2json import csv2json
            csv2json(parameter[1], parameter[2], parameter[3], parameter[4])
        else: 
            from csv2json import csv2jsonHelp
            csv2jsonHelp()

    elif parameter[0] == 'json2csv':
        if len(parameter) == 4:
            from json2csv import json2csv
            json2csv(parameter[1], parameter[2], parameter[3])
        else:
            from json2csv import json2csvHelp
            json2csvHelp()
    
    elif parameter[0] == 'jsonax': 
        if len(parameter) == 4:
            from jsonax import jsonax
            jsonax(parameter[1], parameter[2], parameter[3])
        else:
            from jsonax import jsonaxHelp
            jsonaxHelp()

    elif parameter[0] == 'jsoneyelike': 
        if len(parameter) == 2:
            from jsoneyelike import jsoneyelike
            jsoneyelike(parameter[1])
        else:
            from jsoneyelike import jsoneyelikeHelp
            jsoneyelikeHelp()

    elif parameter[0] == 'vcs2code': 
        if len(parameter) == 3:
            from vcs2code import vcs2code
            vcs2code(parameter[1], parameter[2])
        else:
            from vcs2code import vcs2codeHelp
            vcs2codeHelp()

    elif parameter[0] == '':
        print('Don\'t know what to do')
