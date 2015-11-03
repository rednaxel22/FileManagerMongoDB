from filesHandling import filesHandling

def delimiters(delimiter):
    deli = ','
    if delimiter == '\\t':
        deli = '\t'
    else:
        deli = delimiter
    return deli

def handleFiles(filename, delimiter, fieldnames):
    filesHandling(filename, delimiter, fieldnames)

def copyFileToServer(path):
    shutil.copy(path, LOCALPATH)
