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

# change based on which algorithm
img_folder = "combined/train_inputs"

print("Running ", algorithm.__class__)

# change name based on which algorithm
base_img_name = "sfd_"

for filename in os.listdir(img_folder):

    # we can loop now through our array of images
#    img_path = img_array[x]

    # read file into open cv and apply to algorithm to generate background model
    img = cv2.imread(os.path.join(img_folder,filename))
    img_output = algorithm.apply(img)
    # img_bgmodel = algorithm.getBackgroundModel()

    # img_bg = "dataset2014/results/badWeather/wetSnow/bg"
    img_fg = "combined/foreground/sfd"

    filename_split = filename.split('_')
    without_tag = filename_split[1].split('.')
    file_num = without_tag[0]

    file_name = base_img_name + file_num + '.png'
    
    # cv2.imwrite(os.path.join(img_bg, file_name), img_bgmodel)
    cv2.imwrite(os.path.join(img_fg, file_name), img_output)
    cv2.waitKey(0)


print("Finished")
