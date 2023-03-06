import os

class FILE:

    def __init__(self,pth=None,ext=".json"):
        self.path_list=None
        self.files_list=None
        self.path = pth 
        self.ext = ext        
    
    def get_file_path(self):
        self.path_list=[]
        self.files_list=[]
        for file in os.listdir(self.path):
            if file.endswith(self.ext):
                self.path_list.append(self.path+'/'+file)
                self.files_list.append(file)
    
        return self.path_list,self.files_list
    
    def get_files(self):

        return self.get_file_path()[1]
    
    def get_paths(self):
                
        return self.get_file_path()[0]

        

        
