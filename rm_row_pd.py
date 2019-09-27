import numpy as np
import pandas as pd
import shutil
import xlwt
import cv2
import os
import pdb

def read_excel(file_name):
    df = pd.read_excel(file_name, sheet_name='Sheet1')
    films = []
    for film_idx, ratio in zip(df['film'],df['ratio']):
        if float(ratio) >= 0.5:
            films.append(film_idx)
    
    return films



def moves(source_file, target_file, films):
    for film in films:
        source = os.path.join(source_file, '%05d'%film)
        target = os.path.join(target_file, '%05d'%film)
        if not os.path.isdir(target):
            os.makedirs(target)
        shutil.move(source, target_file)

def rm_row(films, source_file):
    df = pd.read_csv(source_file)

    choose_CASME2 = df.loc[df['order'].isin(films)]
    x = choose_CASME2.reset_index(drop=True)
    #dataframe_train = pd.DataFrame({'video_name': X_train, 'label': y_train})
    pdb.set_trace()
    x.to_csv("alldata_single_rm_less_50.csv", index=False, sep=',')

if __name__ == "__main__":

    info_file = 'stat_film.xlsx'

    source_file = 'alldata_labels_single_clips.csv'

    #target_file = 'a'

    films = read_excel(info_file)
    print(films)

    rm_row(films, source_file)

    #move(source_file, target_file, films)
     