import matplotlib.pyplot as plt
import numpy as np
from scipy.ndimage import morphology

image = np.load('ps.npy.txt')

mask1 = np.array([[1,1,1,1],
                  [1,1,1,1],
                  [1,1,0,0],
                  [1,1,0,0],
                  [1,1,1,1],
                  [1,1,1,1]]) 

mask2 = np.array([[1,1,1,1],
                  [1,1,1,1],
                  [0,0,1,1],
                  [0,0,1,1],
                  [1,1,1,1],
                  [1,1,1,1]])

mask3 = np.array([[1,1,0,0,1,1],
                  [1,1,0,0,1,1],
                  [1,1,1,1,1,1],
                  [1,1,1,1,1,1]])

mask4 = np.array([[1,1,1,1,1,1],
                  [1,1,1,1,1,1],
                  [1,1,0,0,1,1],
                  [1,1,0,0,1,1]])

mask5 = np.array([[1,1,1,1,1,1],
                  [1,1,1,1,1,1],
                  [1,1,1,1,1,1],
                  [1,1,1,1,1,1]])


masks = np.array([mask1, mask2, mask3, mask4, mask5])
summ = 0

for i in range (5):
    result = morphology.binary_hit_or_miss(image, masks[i])
    print("Symbol %i, quantity =" % (i+1), np.sum(result))
    summ +=np.sum(result)
     
print("Total sum =", summ)

plt.imshow(image)
plt.show()