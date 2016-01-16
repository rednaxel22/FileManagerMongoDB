from filesHandling import filesHandling

ALLOWED_EXTENSIONS = set(['txt', 'xls', 'xlsx', 'csv', 'raw'])

def delimiters(delimiter):
    deli = ','
    if delimiter == '\\t':
        deli = '\t'
    else:
        deli = delimiter
    return deli

def handleFiles(filename, delimiter, fieldnames):
    filesHandling(filename, delimiter, fieldnames)
   
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS
