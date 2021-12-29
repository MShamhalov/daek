def initconfig():
    import sys
    sys.path.insert(0, "C:\\dev\\daek\\lib")

def getModules():
    import os
    directory = './lib'
    files = os.listdir(directory)
    pattern = '*.py'
    filt=[]
    for entry in files:
        if entry[-3:] == '.py':
            filt.append(entry[:-3])
    return filt