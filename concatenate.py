import cv2
import os
import numpy as np
import random

# Used for testing for CNN predict purposes

# change name based on which algorithm
def get_data():

    algos = ['asd', 'eig', 'ga', 'gmm', 'mc', 'mog', 'sd', 'sfd', 'vm', 'zmm']
    folders = ['bungalow', 'fall', 'highway', 'snowFall', 'turnpike']
    cwd = os.getcwd()

    for i in range(len(folders)):
        folder_name = folders[i]
        img_folder = 'analysis-im/' + folder_name + '/'

        fnames = sorted(os.listdir(img_folder))
        filename = fnames[0]
        idx = filename[2:8]

        print(cwd + '/' + img_folder + 'am' + str(idx) + '.png')
        concatenated_images = cv2.imread(cwd + '/' + img_folder + 'am' + str(idx) + '.png', cv2.IMREAD_GRAYSCALE)
        concatenated_images = cv2.resize(concatenated_images, (224, 224))
        concatenated_images = np.array(concatenated_images)
        concatenated_images = np.expand_dims(concatenated_images, axis=2)

        for i, algo in enumerate(algos):
            im = cv2.imread(cwd + '/' + img_folder + algo + str(idx) + '.png', cv2.IMREAD_GRAYSCALE)
            im = cv2.resize(im, (224, 224))
            im = np.array(im)
            im = np.expand_dims(im, axis=2)
            concatenated_images = np.concatenate((concatenated_images, im), axis=2)

        np.save(img_folder + str(idx) + '.npy', concatenated_images)

if __name__ == "__main__":
    get_data()