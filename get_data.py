import cv2
import os
import numpy as np
import random
import tensorflow as tf

# Used to create input (concatenated images) and ground truths for CNN training

def get_data():

    train_idxs = 0   # 3303
    val_idxs = 0    # 425 (empty) + 75 (w/ motion)
    val_idxs_no_motion = 0
    test_idxs = 0    # 425 (empty) + 75 (w/ motion)
    test_idxs_no_motion = 0

    algos = ['asd', 'eig', 'ga', 'gmm', 'mc', 'mog', 'sd', 'sfd', 'vm', 'zmm']
    cwd = os.getcwd()

    thresh = 0.005
    fnames = os.listdir('dataset2014/combined/groundtruth')
    random.shuffle(fnames)
    for filename in fnames:
        gt_im = cv2.imread(cwd + '/dataset2014/combined/groundtruth/' + filename, cv2.IMREAD_GRAYSCALE)        
        gt_im = cv2.resize(gt_im, (224, 224))

        im_bw = cv2.threshold(gt_im, 254, 255, cv2.THRESH_BINARY)[1]
        h, w = im_bw.shape
        np_im = np.array(im_bw)
        num = np.count_nonzero(np_im)
        frac = thresh * h * w
        temp = filename.split('_')
        idx = temp[1].split('.')[0]

        concatenated_images = cv2.imread(cwd + '/dataset2014/combined/am/am_' + str(idx) + '.png', cv2.IMREAD_GRAYSCALE)
        concatenated_images = cv2.resize(concatenated_images, (224, 224))
        concatenated_images = np.array(concatenated_images)
        concatenated_images = np.expand_dims(concatenated_images, axis=2)

        if (num > frac):    
            if train_idxs < 3303:
                for i, algo in enumerate(algos):
                    im = cv2.imread(cwd + '/dataset2014/combined/' + algo + '/' + algo + '_' + str(idx) + '.png', cv2.IMREAD_GRAYSCALE)
                    im = cv2.resize(im, (224, 224))
                    im = np.array(im)
                    im = np.expand_dims(im, axis=2)
                    concatenated_images = np.concatenate((concatenated_images, im), axis=2)

                np.save('numpy_new_sets/train_algo/' + str(idx) + '.npy', concatenated_images)
                np.save('numpy_new_sets/train_groundtruth/' + str(idx) + '.npy', np_im)
                train_idxs += 1
            elif val_idxs < 500:
                for i, algo in enumerate(algos):
                    im = cv2.imread(cwd + '/dataset2014/combined/' + algo + '/' + algo + '_' + str(idx) + '.png', cv2.IMREAD_GRAYSCALE)
                    im = cv2.resize(im, (224, 224))
                    im = np.array(im)
                    im = np.expand_dims(im, axis=2)
                    concatenated_images = np.concatenate((concatenated_images, im), axis=2)

                np.save('numpy_new_sets/val_algo/' + str(idx) + '.npy', concatenated_images)
                np.save('numpy_new_sets/val_groundtruth/' + str(idx) + '.npy', np_im)
                val_idxs += 1
            elif test_idxs < 500:
                for i, algo in enumerate(algos):
                    im = cv2.imread(cwd + '/dataset2014/combined/' + algo + '/' + algo + '_' + str(idx) + '.png', cv2.IMREAD_GRAYSCALE)
                    im = cv2.resize(im, (224, 224))
                    im = np.array(im)
                    im = np.expand_dims(im, axis=2)
                    concatenated_images = np.concatenate((concatenated_images, im), axis=2)

                np.save('numpy_new_sets/test_algo/' + str(idx) + '.npy', concatenated_images)
                np.save('numpy_new_sets/test_groundtruth/' + str(idx) + '.npy', np_im)
                test_idxs += 1
        else:
            if val_idxs_no_motion < 425:
                for i, algo in enumerate(algos):
                    im = cv2.imread(cwd + '/dataset2014/combined/' + algo + '/' + algo + '_' + str(idx) + '.png', cv2.IMREAD_GRAYSCALE)
                    im = cv2.resize(im, (224, 224))
                    im = np.array(im)
                    im = np.expand_dims(im, axis=2)
                    concatenated_images = np.concatenate((concatenated_images, im), axis=2)

                np.save('numpy_new_sets/val_algo/' + str(idx) + '.npy', concatenated_images)
                np.save('numpy_new_sets/val_groundtruth/' + str(idx) + '.npy', np_im)
                val_idxs_no_motion += 1
                val_idxs += 1
            elif test_idxs_no_motion < 425:
                for i, algo in enumerate(algos):
                    im = cv2.imread(cwd + '/dataset2014/combined/' + algo + '/' + algo + '_' + str(idx) + '.png', cv2.IMREAD_GRAYSCALE)
                    im = cv2.resize(im, (224, 224))
                    im = np.array(im)
                    im = np.expand_dims(im, axis=2)
                    concatenated_images = np.concatenate((concatenated_images, im), axis=2)
                    
                np.save('numpy_new_sets/test_algo/' + str(idx) + '.npy', concatenated_images)
                np.save('numpy_new_sets/test_groundtruth/' + str(idx) + '.npy', np_im)
                test_idxs_no_motion += 1
                test_idxs += 1


if __name__ == "__main__":
    get_data()