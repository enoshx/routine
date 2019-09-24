import pandas as pd 
import numpy as np 
import os
import shutil

if __name__ == '__main__':
    path_excel  = 'check_3.xls'

    df = pd.io.excel.read_excel(path_excel, sheetname='Sheet1')
    images_path = df['path']
    #print(images_path)
    for image_path in images_path:
        image_path = image_path 
        path = os.path.join('none_cut', image_path)
        #print(path)
        os.remove(path)

