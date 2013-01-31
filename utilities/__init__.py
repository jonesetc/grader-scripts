import os

def getdirs():
    files = os.listdir('.')
    files = [f for f in files if f[0] != '.']
    files = [f for f in files if os.path.isdir(f)]

    return files

def getfiles():
    files = os.listdir('.')
    files = [f for f in files if f[0] != '.']
    files = [f for f in files if os.path.isfile(f)]

    return files
