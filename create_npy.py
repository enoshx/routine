import numpy as np
import glob
import sys
import pdb
import cv2
import os

def read_image(npy_path, part_name):
    video_name = glob.glob(part_name+'/*')
    for video in video_name:
        video_npy = []
        for i in range(1, 17):
            image = cv2.imread(video+'/%d.jpg'%i)
            video_npy.append(image)
        save_npy(npy_path, video_npy, video)


def save_npy(npy_path, video_npy, video):

    npy_name = os.path.join(npy_path, video.split('\\')[-1]+'.npy')          #系统环境不同，此处需要改变,此处为window

    #pdb.set_trace()
    np.save(npy_name, video_npy)
def create_file(dirs):
    if not os.path.exists(dirs):
        os.makedirs(dirs)
def main(idx):

    npy_path = '224by224npy'
    create_file(npy_path)

    part_name = 'part_%d'%idx
    read_image(npy_path,part_name)



if __name__ == "__main__":
    idx = 1
    main(idx)