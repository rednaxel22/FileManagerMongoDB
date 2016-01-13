class sdmDAO(object):
    def __init__(self,database):
        self.db = database
        self.sources = database.sources
        self.sourceMetadata = database.sourceMetadata
        self.dashboard = database.dashboard

    def getSource(self, file):
        l = []
        
        return 
