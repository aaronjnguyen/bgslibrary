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

## bgslibrary algorithms
algorithm = bgs.StaticFrameDifference() #SFD
# algorithm = bgs.AdaptiveSelectiveBackgroundLearning() # ASD
# algorithm = bgs.DPAdaptiveMedian() # AM
# algorithm = bgs.DPGrimsonGMM() # GMM
# algorithm = bgs.DPZivkovicAGMM() # ZMM
# algorithm = bgs.DPWrenGA() # GA
# algorithm = bgs.DPEigenbackground() # EIG
# algorithm = bgs.LBMixtureOfGaussians() # MoG
# algorithm = bgs.VuMeter() # VM
# algorithm = bgs.MultiCue() # MC
# algorithm = bgs.SigmaDelta() # SD

img_folder = "dataset2014/dataset/badWeather/wetSnow/input"

print("Running ", algorithm.__class__)

base_img_name = "bin"
curr_file_num = '000001'

for filename in os.listdir(img_folder):

    # we can loop now through our array of images
#    img_path = img_array[x]

    # read file into open cv and apply to algorithm to generate background model
    img = cv2.imread(os.path.join(img_folder,filename))
    img_output = algorithm.apply(img)
    img_bgmodel = algorithm.getBackgroundModel()

    img_bg = "dataset2014/results/badWeather/wetSnow/bg"
    img_fg = "dataset2014/results/badWeather/wetSnow/fg"

    file_name = base_img_name + curr_file_num + '.png'
    
    cv2.imwrite(os.path.join(img_bg, file_name), img_bgmodel)
    cv2.imwrite(os.path.join(img_fg, file_name), img_output)
    cv2.waitKey(0)

    curr_file_num = str(int(curr_file_num) + 1)

print("Finished")
