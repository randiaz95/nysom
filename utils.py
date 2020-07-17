import os


def create_directory(root, folder):
    if folder is str:
        path = os.path.join(root, folder)
        if not os.path.exists(path):
            os.mkdir(path)
        return path
    elif folder is list:
        path = os.path.join(root, *folder)
        if not os.path.exists(path):
            os.mkdir(path)
        return path
    else:
        return "Error while creating directory; folder argument is not string or list of strings."

class Conceptor:
    def __init__(self, name):
        self.name = name
        self.columns = []
    
    def addColumn(name, type, primary_key=False):
        self.columns.append({"name": name, 
                             "type": type,
                             "primary_key": primary_key})

    def createController():
        pass

    def createModel():
        pass

    def createComponent():
        pass
