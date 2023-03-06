import matplotlib.pyplot as plt
import os

class DATA:

    def __init__(self):
        self.class_info = None
        self.img_dist = None

    def get_class_dist(self,json_list=None):
        self.class_info ={
            'big cardboard':0,
            'bulky':0,
            'compactor':0,
            'dumpster':0,
            'electrical and electronic waste':0,
            'garbage bag':0,
            'glass':0,
            'green waste':0,
            'hygiene':0,
            'plastic bag':0,
            'recycle waste':0,
            'textile':0,
            'cylinders':0,
            'bag':0
        }

        

        for i in json_list:
            test = i[0]
            for j in test:
                j['label']=j['label'].lower()
                clss = j['label'].lower()
                self.class_info[clss] +=1

        return self.class_info
    
                
    def plot_dist_class(self,save = False):
        classes = list(self.class_info.keys())
        values = list(self.class_info.values())
        c = ['red', 'yellow', 'black', 'blue', 'orange']
        fig, ax = plt.subplots(figsize =(16, 9))
        # creating the bar plot
        ax.barh(classes, values,color=c)

        for i in ax.patches:
            plt.text(i.get_width()+0.2, i.get_y()+0.5,
            str(round((i.get_width()), 2)),
            fontsize = 10, fontweight ='bold',
            color ='grey')
 
        plt.xlabel("Instances")
        plt.ylabel("Classes")
        plt.title("Garbage Classes From all available annotaion files")
        plt.show()
        if save:
            plt.savefig('all.png')
    
    def get_img_dist(self,json_list,path=True):
        self.img_dist ={
            'big cardboard':[],
            'bulky':[],
            'compactor':[],
            'dumpster':[],
            'electrical and electronic waste':[],
            'garbage bag':[],
            'glass':[],
            'green waste':[],
            'hygiene':[],
            'plastic bag':[],
            'recycle waste':[],
            'textile':[],
            'cylinders':[],
            'bag':[]
        }

        for i in json_list:
            
            test = i[0]
            if not path:
              fname = (os.path.basename(i[3]).split('/')[-1])
            fname = i[3]
            
            
            for j in test:
                j['label']=j['label'].lower()
                clss = j['label'].lower()
                if fname not in self.img_dist[clss]:
                    self.img_dist[clss].append(fname)
            
        return self.img_dist
    
    def plot_dist_img(self,save = False):
        classes = list(self.img_dist.keys())
        val = list(self.img_dist.values())
        values =[]
        for i in val:
            values.append(len(i))
        c = ['red', 'yellow', 'black', 'blue', 'orange']
        fig, ax = plt.subplots(figsize =(16, 9))
        # creating the bar plot
        ax.barh(classes, values,color=c)

        for i in ax.patches:
            plt.text(i.get_width()+0.2, i.get_y()+0.5,
            str(round((i.get_width()), 2)),
            fontsize = 10, fontweight ='bold',
            color ='grey')
 
        plt.xlabel("Number of Images Per Classes")
        plt.ylabel("Classes")
        plt.title("Garbage Classes From all available annotaion files")
        plt.show()
        if save:
            plt.savefig('all.png')


               

        

        

