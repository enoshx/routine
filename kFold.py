import sys
import numpy as np
import pandas as pd 
#from logger import Logger
from sklearn.model_selection import StratifiedKFold

def Sf_KFold(X, y, n_splits):
    i = 0
    skf = StratifiedKFold(n_splits)
    skf.get_n_splits(X, y)
    for train_index, test_index in skf.split(X, y):
        i += 1
        print("Train: ", train_index, "Test: ", test_index)
        X_train, X_test = X[train_index], X[test_index]
        y_train, y_test = y[train_index], y[test_index]

        dataframe_train = pd.DataFrame({'video_name': X_train, 'label': y_train})
        dataframe_train.to_csv("video_trainset_%d.csv"%i, index=False, sep=',')
        dataframe_test = pd.DataFrame({'video_name': X_test, 'label': y_test})
        dataframe_test.to_csv("video_testset_%d.csv"%i, index=False, sep=',')

    #return X_train, X_test, y_train, y_test
def logger():
    #write log file
    sys.stdout = Logger('test.log', sys.stdout)
    sys.stderr = Logger('test_err.log', sys.stderr)

def main():
    #logger()
    n_splits=5
    all_info_file = 'alldata_single_rm_less_50.csv'
    df = pd.read_csv(all_info_file)
    images_path = df['order']
    labels = df['label']
    Sf_KFold(images_path, labels, n_splits)

if __name__ == "__main__":
    main()

