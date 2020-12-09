from PIL import Image
import numpy as np
 
# Used to debug input

x = np.load('numpy_new_sets/train_algo/2106.npy')
y = np.load('numpy_new_sets/train_groundtruth/2106.npy')
 
print(x.shape)

img1 = Image.fromarray(x[:,:,0], 'L')
img1.save('concat1.png')
img2 = Image.fromarray(x[:,:,1], 'L')
img2.save('concat2.png')
img3 = Image.fromarray(x[:,:,2], 'L')
img3.save('concat3.png')
img4 = Image.fromarray(y, 'L')
img4.save('concat4.png')