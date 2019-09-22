import cv2  
import os
import glob
import sys
import pdb
import argparse

def make_folder_anyway(folder_path):
    flag = os.path.exists(folder_path)
    if flag is not True:
        os.makedirs(folder_path)

def video2pic(video_path, output_folder, clips_name):
    '''
    video_path: './1.mp4'
    output_path: './output_folder/'
    '''
    vc = cv2.VideoCapture(video_path)
    num = 0
    rval = vc.isOpened()
    output_folder = os.path.join(output_folder, '%05d'%clips_name)
    make_folder_anyway(output_folder)
    
    while rval:
        num = num + 1
        rval, frame = vc.read()
        if rval:
           
            #cv2.imwrite(output_folder+str(num)+'.jpg', frame)
            cv2.imwrite(output_folder+'/'+'%05d'%clips_name+'_'+'%05d'%num+'.jpg', frame)
        else:
            break
    vc.release()
    
def main(argv):
    
    part_files = './all_clips_H264_distribute/part_%d'%argv.num_idx
    videos = glob.glob(part_files+'/*')
    len_videos = len(videos)
    
    for index_videos in range(len_videos):
        strings = videos[index_videos].split('/')
        clips_name = int(strings[-1][:-4])
        
        video_path = videos[index_videos]
        
        output_folder = './output/orgin'

        #pdb.set_trace()
        
        video2pic(video_path, output_folder, clips_name)
        print("finish:",str(index_videos+1),"/",str(len_videos))

def parse_arguments(argv):
    parser = argparse.ArgumentParser()

    parser.add_argument('--num_idx', type=int, help='num of parts.',default=0)

    return parser.parse_args(argv)

if __name__ == "__main__":

    main(parse_arguments(sys.argv[1:]))