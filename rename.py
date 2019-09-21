import numpy as np
import glob
import pdb 
import os


def rename(src, dst):
    files_name = glob.glob(src+'/*')

    for old_idx in range(1, len(files_name)+1):
        src_name = os.path.join(src, str(old_idx))
        dst_name = os.path.join(src, '%05d'%dst[old_idx-1])

        os.rename(src_name, dst_name)


def read_txt(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        data  = f.readlines()
        name = []

        for i in data:
            items = i.split()
            idx = int(items[0].split('/')[0])

            name.append(idx)
            
        name_idx = list(set(name)) #排序删除重复元素

        #data = json.loads(f.readlines())
        #pdb.set_trace()
    return name_idx

def main(idx):
    box_name = 'boxpoint_%d.txt'%idx
    part_name = 'part_%d'%idx
    names = read_txt(box_name)
    rename(part_name, names)


if __name__ == "__main__":
    idx = 12
    main(idx)

