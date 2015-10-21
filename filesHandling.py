TXT = 'txt'
XLS = 'xls'
XLSX = 'xlsx'
CSV = 'csv'


def filesHandling(path):
    fileType = path[path.rfind('.')+1:]
    if fileType == TXT:
        txtFile(path)
    

def txtFile(path):
    print 1

