from filesHandling import filesHandling

filename = 'txtSampleData1.txt' 
##filename = 'txtSampleData1.xlsx'

def handlefiles():
##    files = open(filename,'r')
##    for line in files:
##        print line
    filesHandling(filename)

if __name__ == '__main__':
    handlefiles()
    
