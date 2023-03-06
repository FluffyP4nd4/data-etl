from utils.data_info import DATA
from utils.extract import EXTRACT
from utils.files_info import FILE
from utils.classes import class_id2name
import argparse
import os


info = DATA()


def get_data(json,img):
    img_exist =[]
    for i in img:
        fname = os.path.splitext(i)[0] +'.json'
        if fname in json:
            img_exist.append(i)
    
    return img_exist



def labelme_list(path):
    labelme_annot = FILE(pth=path,ext='.json')
    labelme_img = FILE(pth=path,ext='.jpeg')

    labelme = EXTRACT(labelme_annot.get_paths())
    labelme_data =  labelme.load_annot()    
    labelme_lst = info.get_img_dist(labelme_data)

    exist_list = get_data(labelme_annot.get_files(),labelme_img.get_files())   

    return labelme_lst,exist_list
	
def coco_list(path):
    # coco
    coco = EXTRACT(path)
    files = coco.coco2labelme()
    coco_data =  coco.load_annot(True,files)
    coco_lst = info.get_img_dist(coco_data)

    return coco_lst

def get_class_name(opt):
    cls =[]
    for i in opt.classes:
        cls.append(class_id2name[i])
    
    return cls


def process(opt):
    
    cls = get_class_name(opt)

    data_dict = None
    img_list =None

    
    if not opt.coco:
        out_labelme = labelme_list(opt.path)
        data_dict = out_labelme[0]
        img_list = out_labelme[1]
        for i in cls:
            with open(opt.dest+i+'.txt','w') as f:
                for j in data_dict[i]:
                    f_pth = os.path.basename(j).split('/')[-1]
                    if f_pth in img_list:
                        f.write(opt.path+'/'+f_pth)
                        f.write('\n')
        

    else:
        data_dict =coco_list(opt.path)
        for i in cls:
            with open(opt.dest+i+'.txt','w') as f:
                for j in data_dict[i]:
                    f.write(j)
                    f.write('\n')
        
    
    
        


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--classes', nargs='+', type=int, default=[0,1,2,3,4,5,6,7,8,9,10,11,12,13],help='filter by class: --class 0, or --class 0 2 3'
        )
    parser.add_argument(
        '--path', type=str, default='/content/drive/Shareddrives/Ficha/Tech/Annotation/Truck_project/Annotated ones', help='path to annotated data file'
        )
    parser.add_argument(
        '--coco', type=bool, default=False, help='If lableing is coco set to True'
    )
    parser.add_argument(
        '--dest',default='/content/',help='the destination folder to save txt file'
    )
   
    opt = parser.parse_args()
    process(opt=opt)
    

