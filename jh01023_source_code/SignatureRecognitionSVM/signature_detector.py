from skimage.feature import hog
from scipy.misc import imread,imresize
from sklearn.svm import SVC
from sklearn.svm import LinearSVC
import pickle

### Remove forced-depreciation warnings about outdated python modules
def warn(*args, **kwargs):
    pass
import warnings
warnings.warn = warn
### End warning removal


if __name__ == '__main__':
    #load the detector
    clf = pickle.load( open("signature.detector","rb"))

    #now load a test image and get the hog features.
    test_image = imread('./testing/s/sh.jpg',1) # you can modify which image is tested by changing the filename here
    test_image = imresize(test_image, (200,200))

    hog_features = hog(test_image, orientations=12, pixels_per_cell=(16, 16),
                    cells_per_block=(1, 1))
    hog_features = hog_features.reshape(1, -1)

    # result_type returns a number based on whether the image predicted is a b h or s depending on the person
    result_type = clf.predict(hog_features)


    # we now translate the above result into a string, making the result easier to understand
    if result_type == 'b':
	    print 'The SVM identifies this image as Burts Signature'
    elif result_type == 'h':
	    print "The SVM identifies this image as  Hawkins Signature"
    elif result_type == 's':
	    print "The SVM identifies this image as a Brians Signature"
    else:
	    print "Something went wrong"

print '\nFinished identifying'
