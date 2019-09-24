import pandas as pd 
import numpy as np 
import os
import shutil

if __name__ == '__main__':
    path_excel  = 'excel.xlsx'
    sheetnames  = ['part_3', 'part_4', 'part_6','part_8', 'part_10', 'part_12']
    for sheet in sheetnames:
        df = pd.read_excel(path_excel, sheet_name=sheet, dtype=np.str)
        images_path = df['path']
        #print(images_path)
        for image_path in images_path:
            image_path = image_path + '.jpg'
            path = os.path.join(sheet, image_path)
            #print(path)
            shutil.copy(path, os.path.join('out', 'none_cut', path))

