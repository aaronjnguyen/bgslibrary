import os
import shutil

paths = ['badminton', 'canoe', 'park', 'parking', 'pedestrians',
         'peopleInShade', 'tramCrossroad_1fps', 'turbulence3', 'wetSnow', 
         'winterStreet', 'zoomInZoomOut']

algo_paths = ['am', 'asd', 'eig', 'ga', 'gmm', 'mc',
              'mog', 'sd', 'sfd', 'vm', 'zmm']

new_input_path = 'combined/inputs'
new_groundtruth_path = 'combined/groundtruth'

i = 0
for path in paths:

    for algo_path in algo_paths:
        j = i
        old_algo_path = 'results/' + path + '/' + algo_path
        new_algo_path = 'combined/' + algo_path

        for filename in sorted(os.listdir(old_algo_path)):
            first_arg = old_algo_path + '/' + filename
            second_arg = new_algo_path + '/' + algo_path + '_' + str(j) + '.png'
            shutil.copyfile(first_arg, second_arg)
            j += 1

    j = i
    old_input_path = 'dataset/' + path + '/input'

    for filename in sorted(os.listdir(old_input_path)):
        # print(filename)
        first_arg = old_input_path + '/' + filename
        second_arg = new_input_path + '/in_' + str(j) + '.jpg'
        shutil.copyfile(first_arg, second_arg)
        j += 1
    
    old_groundtruth_path = 'dataset/' + path + '/groundtruth'

    for filename in sorted(os.listdir(old_groundtruth_path)):
        first_arg = old_groundtruth_path + '/' + filename
        second_arg = new_groundtruth_path + '/gt_' + str(i) + '.png'
        shutil.copyfile(first_arg, second_arg)
        i += 1

