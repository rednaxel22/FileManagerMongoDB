import csv
import json

TXT = 'txt'
XLS = 'xls'
XLSX = 'xlsx'
CSV = 'csv'

#shameless copy paste from json/decoder.py
##FLAGS = re.VERBOSE | re.MULTILINE | re.DOTALL
##WHITESPACE = re.compile(r'[ \t\n\r]*', FLAGS)

def filesHandling(path, delimiter, fieldnames):
    fileType = path[path.rfind('.')+1:]
    if fileType == TXT:
        txtFile(path, delimiter, fieldnames)
    
def txtFile(path, delimiter, fields):
    with open(path,'r') as f:
        next(f)
        reader = csv.DictReader(f, fieldnames=fields, delimiter=delimiter)
        json_filename = path[:path.rfind('.')] + '.json'
        jsonf = open(json_filename, 'w')
        data = json.dumps([r for r in reader])
        jsonf.write(data)
        jsonf.close()

