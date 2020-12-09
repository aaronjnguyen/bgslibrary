import os

# paths = ['am', 'asd', 'eig', 'ga', 'gmm', 'mc',
#               'mog', 'sd', 'sfd', 'vm', 'zmm', 'inputs', 'groundtruth']

# for path in paths:
#     print(path + ': ' + str(len(os.listdir('combined/' + path))))

print('train_groundtruth: ' + str(len(os.listdir('../numpy_new_sets/train_groundtruth/'))))
print('train_algo: ' + str(len(os.listdir('../numpy_new_sets/train_algo/'))))

print('val_groundtruth: ' + str(len(os.listdir('../numpy_new_sets/val_groundtruth/'))))
print('val_algo: ' + str(len(os.listdir('../numpy_new_sets/val_algo/'))))

print('test_groundtruth: ' + str(len(os.listdir('../numpy_new_sets/test_groundtruth/'))))
print('test_algo: ' + str(len(os.listdir('../numpy_new_sets/test_algo/'))))