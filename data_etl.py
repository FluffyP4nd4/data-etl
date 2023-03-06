from utils.files_info import FILE
from utils.data_info import DATA
from utils.extract import EXTRACT


class ETL:

    def __init__(self,img_path=None,annot_path=None,img_ext = '.jpeg',ann_ext='.json'):
        self.img_pth = img_path
        self.ann_pth = annot_path
        self.im_ext = img_ext
        self.ann_ext = ann_ext
        

    
    def get_img_ann(self):
        img = FILE(self.img_pth,ext=self.im_ext)
        ann = FILE(self.ann_pth,ext=self.ann_ext)

        return [[img.get_files, img.get_paths],[ann.get_files,ann.get_paths]]

        