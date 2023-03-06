import json
import os
from .classes import class_info
from pycocotools.coco import COCO

class EXTRACT:

    def __init__(self,path_list):
       
        self.files = path_list
        self.categories = None
        
        

    def load_annot(self,coco=False,coco_lst=None):
        json_lst =[]
        if not coco:
            for i in self.files:
                with open(i) as json_file:
                    data = json.load(json_file)
                
                ins_list=[]
                for i in data['shapes']:
                    extract = {
                    'label':'',
                    'points':0
                    }
                    extract['label'] = i['label'].lower()
                    if extract['label']=='bulk':
                        extract['label']='bulky'
                
                    extract['points']= i['points']

                    ins_list.append(extract)
        
                json_lst.append([ins_list,data['imageHeight'],data['imageWidth'],data['imagePath']])
        
        elif coco:
            for i in coco_lst:
                
                
                ins_list=[]
                for j in i['shapes']:
                    extract = {
                    'label':'',
                    'points':0
                    }
                    extract['label'] = j['label'].lower()
                    if extract['label']=='bulk':
                        extract['label']='bulky'
                
                    extract['points']= j['points']

                    ins_list.append(extract)
        
                json_lst.append([ins_list,i['imageHeight'],i['imageWidth'],i['imagePath']])

    
        return json_lst

    
    def convert_label(self,coco=False,coco_lst=None):

        cplte =[]
        lst = self.labelme(coco,coco_lst)
        for i in lst:
            w = i[2]
            h = i[1]
            img_pth =i[3]
            label =[]
            for j in i[0]:
                lbl = class_info[j['label'].lower()]
                
                pts=[]
                for k,l in j['points']:
                    pts.append(k/w)
                    pts.append(l/h)
                label.append([lbl,pts])
            cplte.append([label,img_pth])
        
        cplte_label=[]
        for i,img in cplte:
            labels=[]
            for j in i:
                id = str(j[0])
                pts=' '.join(map(str, j[1]))
                result = id+' '+pts
                labels.append(result)
            cplte_label.append([labels,img])
            
        return cplte_label
    
    
    def labelme2yolo(self):
        return self.convert_label()
    
    
    def coco2labelme(self):
        
        self.categories = None
        # Load COCO annotations
        coco = COCO(self.files)
        # Create LabelMe JSON format
        labelme = {"version": "4.5.6", "flags": {}, "shapes": []}
        self.categories = {cat["id"]: cat["name"] for cat in coco.loadCats(coco.getCatIds())}
        # print(categories)
        for ann in coco.loadAnns(coco.getAnnIds()):
            label = self.categories[ann["category_id"]]
            points = ann["segmentation"][0]
            shape = {
                "label": label,
                "points":  self.process_points(points),
                "group_id": ann['image_id'],
                "shape_type": "polygon",
                "flags": {},
            }
            labelme["shapes"].append(shape)
        
        img_lst = {}
        for img in coco.loadImgs(coco.getImgIds()):
            img_with_ann = {"version": "4.5.6", "flags": {}, "shapes": [],'imageHeight':img['height'],'imageWidth':img['width'],'imagePath':img['file_name']}
            
            img_lst[img['id']]= img_with_ann
            #print(img['id'])
        
        
        
        for i in labelme['shapes']:
            
            img_lst[i['group_id']]['shapes'].append(i)

        
        labelme_lst =[]
        for i in range(len(img_lst)):
            labelme_lst.append(img_lst[i+1])
        
        # Save LabelMe JSON file
        return labelme_lst
    


    def process_points(self,points):
        x=[]
        y=[]
        for i in range(len(points)):
            if i%2==0:
                x.append(points[i])
            else:
                y.append(points[i])
        
        pts =[]
        for i,j in zip(x,y):
            pts.append([i,j])
        
        return pts

    def yolo_format(self,dest_dir,cplte_label):
        for i in cplte_label:
            f_pth = os.path.basename(i[1]).split('/')[-1]
            fle = os.path.splitext(f_pth)[0]
            with open(dest_dir+fle+'.txt', 'w') as f:
                for line in i[0]:
                    f.write(line)
                    f.write('\n')
        
    
    

    