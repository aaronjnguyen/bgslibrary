import numpy as np
import shutil

# Used initially to split dataset.. not used in final dataset used

algo_paths = ['am', 'asd', 'eig', 'ga', 'gmm', 'mc',
              'mog', 'sd', 'sfd', 'vm', 'zmm']

indices = np.random.choice(17252, 10000, replace=False)

# training set
for i in range(7000):    
    first_arg = 'combined/inputs/in_' + str(indices[i]) + '.jpg'
    second_arg = 'sets/train_inputs/in_' + str(indices[i]) + '.jpg'
    shutil.copyfile(first_arg, second_arg)  

    first_arg = 'combined/groundtruth/gt_' + str(indices[i]) + '.png'
    second_arg = 'sets/train_groundtruth/gt_' + str(indices[i]) + '.png'
    shutil.copyfile(first_arg, second_arg)

    for algo_path in algo_paths:
        first_arg = 'combined/' + algo_path + '/' + algo_path + '_' + str(indices[i]) + '.png'
        second_arg = 'sets/train_algo/' + algo_path + '_' + str(indices[i]) + '.png'
        shutil.copyfile(first_arg, second_arg)

# validation set
for i in range(7000, 8500):
    first_arg = 'combined/inputs/in_' + str(indices[i]) + '.jpg'
    second_arg = 'sets/val_inputs/in_' + str(indices[i]) + '.jpg'
    shutil.copyfile(first_arg, second_arg)  

    first_arg = 'combined/groundtruth/gt_' + str(indices[i]) + '.png'
    second_arg = 'sets/val_groundtruth/gt_' + str(indices[i]) + '.png'
    shutil.copyfile(first_arg, second_arg)

    for algo_path in algo_paths:
        first_arg = 'combined/' + algo_path + '/' + algo_path + '_' + str(indices[i]) + '.png'
        second_arg = 'sets/val_algo/' + algo_path + '_' + str(indices[i]) + '.png'
        shutil.copyfile(first_arg, second_arg)

# test set
for i in range(8500,10000):
    first_arg = 'combined/inputs/in_' + str(indices[i]) + '.jpg'
    second_arg = 'sets/test_inputs/in_' + str(indices[i]) + '.jpg'
    shutil.copyfile(first_arg, second_arg)  

    first_arg = 'combined/groundtruth/gt_' + str(indices[i]) + '.png'
    second_arg = 'sets/test_groundtruth/gt_' + str(indices[i]) + '.png'
    shutil.copyfile(first_arg, second_arg)

    for algo_path in algo_paths:
        first_arg = 'combined/' + algo_path + '/' + algo_path + '_' + str(indices[i]) + '.png'
        second_arg = 'sets/test_algo/' + algo_path + '_' + str(indices[i]) + '.png'
        shutil.copyfile(first_arg, second_arg)