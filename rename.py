import os
import shutil

# combined all separate algorithm foreground masks into one image

paths = ['badminton', 'canoe', 'park', 'parking', 'pedestrians',
         'peopleInShade', 'tramCrossroad_1fps', 'turbulence3', 'wetSnow', 
         'winterStreet', 'zoomInZoomOut']

new_input_path = 'combined/inputs'
new_groundtruth_path = 'combined/groundtruth'

i = 0
for path in paths:
    j = i

    old_input_path = path + '/input'

    for filename in sorted(os.listdir(old_input_path)):
        # print(filename)
        first_arg = old_input_path + '/' + filename
        second_arg = new_input_path + '/in_' + str(j) + '.jpg'
        shutil.copyfile(first_arg, second_arg)
        j += 1
    
    old_groundtruth_path = path + '/groundtruth'

    for filename in sorted(os.listdir(old_groundtruth_path)):
        first_arg = old_groundtruth_path + '/' + filename
        second_arg = new_groundtruth_path + '/gt_' + str(i) + '.png'
        shutil.copyfile(first_arg, second_arg)
        i += 1

