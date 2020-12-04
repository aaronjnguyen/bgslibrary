import numpy as np
import shutil
# 17251

indices = np.random.choice(17252, 10000, replace=False)

# training set
for i in range(7000):    
    first_arg = 'inputs/in_' + str(indices[i]) + '.jpg'
    second_arg = 'train_inputs/in_' + str(indices[i]) + '.jpg'
    shutil.copyfile(first_arg, second_arg)  

    first_arg = 'groundtruth/gt_' + str(indices[i]) + '.png'
    second_arg = 'train_groundtruth/gt_' + str(indices[i]) + '.png'
    shutil.copyfile(first_arg, second_arg)

# validation set
for i in range(7000, 8500):
    first_arg = 'inputs/in_' + str(indices[i]) + '.jpg'
    second_arg = 'val_inputs/in_' + str(indices[i]) + '.jpg'
    shutil.copyfile(first_arg, second_arg)  

    first_arg = 'groundtruth/gt_' + str(indices[i]) + '.png'
    second_arg = 'val_groundtruth/gt_' + str(indices[i]) + '.png'
    shutil.copyfile(first_arg, second_arg)

# test set
for i in range(8500,10000):
    first_arg = 'inputs/in_' + str(indices[i]) + '.jpg'
    second_arg = 'test_inputs/in_' + str(indices[i]) + '.jpg'
    shutil.copyfile(first_arg, second_arg)  

    first_arg = 'groundtruth/gt_' + str(indices[i]) + '.png'
    second_arg = 'test_groundtruth/gt_' + str(indices[i]) + '.png'
    shutil.copyfile(first_arg, second_arg)