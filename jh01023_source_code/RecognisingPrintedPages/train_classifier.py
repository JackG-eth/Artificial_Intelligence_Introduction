import numpy as np
import os
import itertools
import operator
import random
import matplotlib.pyplot as plt
import matplotlib.cm as cm
from skimage.feature import hog
from skimage import color, exposure
from scipy.misc import imread,imsave,imresize
import numpy.random as nprnd
from sklearn.svm import SVC
from sklearn import linear_model
from sklearn.svm import LinearSVC
import matplotlib
import pickle

if __name__ == '__main__':

    #format of folders
    folder_string = 'abcdefghijklmnopqrstuvwxyz123456789'

    #create the list that will hold ALL the data and the labels
    #the labels are needed for the classification task:
    data = []
    labels = []
    #Lets me know how far through a given array I am.
    string_counter = 0

    #fill the training dataset
    # the flow is
    # 1) load sample
    # 2) resize it to (200,200) so that we have same size for all the images
    # 3) get the HOG features of the resized image
    # 4) save them in the data list that holds all the hog features
    # 5) also save the label (target) of that sample in the labels list
    # we go through each folder one by one
    while string_counter < 35:
        # within that folder we get all of the files.
        path = './training_type/' + str(folder_string[string_counter]) + '/'
        print 'Number of training images -> 1: ' + str((path))
        filenames = sorted([filename for filename in os.listdir(path) if (filename.endswith('.jpg') or filename.endswith('.png') or (filename.endswith('.bmp'))) ])
        #print 'Number of training images -> 2: ' + str((filenames))
        filenames = [path+filename for filename in filenames]
        #print 'Number of training images -> 3: ' + str((filenames))
        for filename in filenames:
            #read the images
            image = imread(filename,1)
            #flatten it
            image = imresize(image, (200,200))
            hog_features = hog(image, orientations=12, pixels_per_cell=(16, 16),
                        cells_per_block=(1, 1))
            data.append(hog_features)
            labels.append(str(folder_string[string_counter]))
        #print 'Filename print' + str(filenames) + '/'
        string_counter += 1



    print 'Training the SVM'
        #create the SVC
    clf = LinearSVC(dual=False,verbose=1)
        #train the svm
    clf.fit(data, labels)

    #pickle it - save it to a file
    pickle.dump( clf, open( "letter.detector", "wb" ) )
