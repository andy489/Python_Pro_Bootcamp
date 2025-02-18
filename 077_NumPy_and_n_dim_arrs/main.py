import numpy as np
import random as rand

import matplotlib.pyplot as plt
import scipy
from PIL import Image  # for reading image files
from matplotlib.image import AxesImage

# Create new ndarray from scratch
my_array = np.array([1.1, 9.2, 8.1, 4.7])

# Show rows and columns
# print(my_array.shape)

# Accessing elements by index
element_by_ind_1d = my_array[2]
# print(element_by_ind_1d)

# Show dimensions of an array
dimension = my_array.ndim
# print(dimension)

array_2d = np.array([[1, 2, 3, 9], [5, 6, 7, 8]])

# print(f'array_2d has {array_2d.ndim} dimensions')
# print(f'Its shape is {array_2d.shape}')
# print(f'It has {array_2d.shape[0]} rows and {array_2d.shape[1]} columns')
# print(array_2d)

element_by_ind_2d = array_2d[1, 2]  # Short fot array_2d[1][2]
# print(element_by_ind_2d)

entire_row_access = array_2d[1, :]  # Short fot array_2d[1][:]
# print(entire_row_access)

# An array of 3 dimensions (or higher) is often referred to as a ”tensor”.
# That’s also where Tensorflow, the popular machine learning tool, gets its name.

mystery_array = np.array([[[0, 1, 2, 3],
                           [4, 5, 6, 7]],

                          [[7, 86, 6, 98],
                           [5, 1, 0, 4]],

                          [[5, 36, 32, 48],
                           [97, 0, 27, 18]]])

# print(f'We have {mystery_array.ndim} dimensions')
# print(f'The shape is {mystery_array.shape}')

# Axis 0: 3rd element. Axis 1: 2nd Element. Axis 3: 4th Element
# print(mystery_array[2, 1, 3])

# Retrieve all the elements on the 3rd axis that are at position 2
# on the first axis and position 1 on the second axis.
# print(mystery_array[2, 1, :])

# All the first elements on axis number 3
# print(mystery_array[:, :, 0])

a = np.arange(10, 30)
# print(a)

last_3 = a[-3:]
# print(last_3)

my_slice = a[3:6]
# print(my_slice)

except_first_12 = a[12:]
# print(except_first_12)

even_subset = a[::2]
# print(even_subset)

reverse = a[::-1]
reverse_again = np.flip(a)
# print(reverse)
# print(reverse_again)

b = np.array([6, 0, 9, 0, 0, 5, 0])
# print(b)

non_zero_b = b[b != 0]
non_zero_b_indexes = np.nonzero(b)  # tuple
# print(non_zero_b)
# print(b[non_zero_b_indexes])

# from numpy.random import random
# z = random((3,3,3))

m = np.random.random((3, 3, 3))
# print(m)

x = np.linspace(0, 100, num=9)
# print(x)
# print(x.shape)

y = np.linspace(start=-3, stop=3, num=9)
plt.plot(x, y)
# plt.show()

noise = np.random.random((128, 128, 3))
# print(noise.shape)
plt.imshow(noise)
# plt.show()

v1 = np.array([4, 5, 2, 7])
v2 = np.array([2, 1, 3, 3])

v3 = v1 + v2
v4 = v1 * v2

# print(v3)
# print(v4)

list1 = [4, 5, 2, 7]
list2 = [4, 5, 2, 7]
list3 = list1 + list2
# print(list3)

# print(array_2d)
# print(array_2d + 10)
# print(array_2d * 5)

a1 = np.array([[1, 3],
               [0, 1],
               [6, 2],
               [9, 7]])

b1 = np.array([[4, 1, 3],
               [5, 8, 5]])

c1 = np.matmul(a1, b1)
c2 = a1 @ b1
# print(a1.shape)
# print(b1.shape)
# print(f"Matrix c has {c1.shape[0]} rows and {c1.shape[1]} columns.")
# print(c1)
# print(c2)

import scipy.datasets
import pooch

img = scipy.datasets.face()
# print(img.shape)
# print(type(img))
# print(img)

sRGB_array = img / 255
# print(sRGB_array)

grey_vals = np.array([0.2126, 0.7152, 0.0722])
img_gray = sRGB_array @ grey_vals

# plt.imshow(img_gray, cmap="gray")
# plt.imshow(np.flip(img_gray), cmap="gray")
# plt.imshow(np.rot90(img), cmap="gray")
solar_img = 255 - img
plt.imshow(solar_img)
# plt.show()


file_name = "yummy_macarons.jpg"

my_img = Image.open(file_name)
img_array = np.array(my_img)
print(img_array.shape)

# plt.imshow(img_array)
plt.imshow(255-img_array)
plt.show()