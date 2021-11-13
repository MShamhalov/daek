def executor(command): 
    parameter = command.split(' ')

    if parameter[0] == 'socsv2json':
        from txtConvert import socsv2json
        socsv2json(parameter[1], parameter[2], parameter[3], parameter[4])

    elif parameter[0] == 'sojson2csv':
        from txtConvert import sojson2csv
        sojson2csv()

    elif parameter[0] == '':
        print('Don\'t know what to do')

    else: print ('bad command')
