##############################################
# Demo file
# python demo2.py --- will use video
# python demo2.py image --- will use images
#############################################

import numpy as np
import cv2
import pybgs as bgs
import sys
import glob
import os

print("OpenCV Version: {}".format(cv2.__version__))

def is_cv2():
    return check_opencv_version("2.")

def is_cv3():
    return check_opencv_version("3.")

def is_cv4():
    return check_opencv_version("4.")

def check_opencv_version(major):
    return cv2.__version__.startswith(major)

algorithms = []

names = ['sfd', 'asd', 'am', 'gmm', 'zmm', 'ga', 'eig', 'mog', 'vm','mc', 'sd']
## bgslibrary algorithms
algorithms.append(bgs.StaticFrameDifference()) #SFD
algorithms.append(bgs.AdaptiveSelectiveBackgroundLearning() # ASD
algorithms.append(bgs.DPAdaptiveMedian()) # AM
algorithms.append(bgs.DPGrimsonGMM()) # GMM
algorithms.append(bgs.DPZivkovicAGMM()) # ZMM
algorithms.append(bgs.DPWrenGA()) # GA
algorithms.append(bgs.DPEigenbackground()) # EIG
algorithms.append(bgs.LBMixtureOfGaussians()) # MoG
algorithms.append(bgs.VuMeter()) # VM
algorithms.append(bgs.MultiCue()) # MC
algorithms.append(bgs.SigmaDelta()) # SD

# change based on which algorithm
#img_folder = "sets/train_inputs"
img_folder = "dataset2014/dataset/badWeather/wetSnow/input"

print("Running ", algorithm.__class__)

# change name based on which algorithm
base_img_name = "sfd_"
for filename in sorted(os.listdir(img_folder)):

    # we can loop now through our array of images
#    img_path = img_array[x]

    # read file into open cv and apply to algorithm to generate background model
    img = cv2.imread(os.path.join(img_folder,filename))
    img_output = algorithm.apply(img)
    # img_bgmodel = algorithm.getBackgroundModel()

    img_fg = "dataset2014/results/badWeather/wetSnow/sfd"
    #img_fg = "sets/foreground/test/sfd"

    file_num = filename[2:8]
    
    file_name = base_img_name + file_num + '.png'
    
    # cv2.imwrite(os.path.join(img_bg, file_name), img_bgmodel)
    cv2.imwrite(os.path.join(img_fg, file_name), img_output)
    cv2.waitKey(0)

    #file_num += 1

print("Finished")
