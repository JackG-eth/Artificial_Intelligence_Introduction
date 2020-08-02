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

    #Same code as part 1 pretty much
    data = []
    labels = []


    #At the moment only testing it on 3 different people
    folder_string = 'bhs'
    print 'folderstring -> 1: ' + str(len(folder_string))
    string_counter = 0
    string_countertest = 0

    # 3 people so loop through 3 times
    # Exact same process as part 1 when it comes to extracting hog_features
    #fill the training dataset
    # the flow is
    # 1) load sample
    # 2) resize it to (200,200) so that we have same size for all the images
    # 3) get the HOG features of the resized image
    # 4) save them in the data list that holds all the hog features
    # 5) also save the label (target) of that sample in the labels list
    # we go through each folder one by one
    while string_counter < 3:
        path = './training_type/' + str(folder_string[string_counter]) + '/'
        filenames = sorted([filename for filename in os.listdir(path) if (filename.endswith('.jpg') or filename.endswith('.png') or (filename.endswith('.bmp'))) ])
        filenames = [path+filename for filename in filenames]
        for filename in filenames:
            #read the images
            print (string_countertest)
            image = imread(filename,1)
            #flatten it
            image = imresize(image, (200,200))
            hog_features = hog(image, orientations=12, pixels_per_cell=(16, 16),
                        cells_per_block=(1, 1))
            data.append(hog_features)
            labels.append(str(folder_string[string_counter]))
            string_countertest += 1
        #print 'Filename print' + str(filenames) + '/'
        string_counter += 1

    print 'Training the SVM'
    #create the SVC
    clf = LinearSVC(dual=False,verbose=1)
    #train the svm
    clf.fit(data, labels)

    #pickle it - save it to a file
    pickle.dump( clf, open( "signature.detector", "wb" ) )
