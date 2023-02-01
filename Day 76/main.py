# --- USING NUMPY TO WORK WITH NUMERICAL DATA ---

# --- Import Statements ---

import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
from numpy.random import random
from scipy import misc

# --- Understanding NumPy's ndarray ---
# NumPy's most amazing feature is the powerful ndarray.

# --- 1-Dimensional Arrays (Vectors) ---

# Create a new ndarray from scratch:
my_array = np.array([1.1, 9.2, 8.1, 4.7])

# Show rows & columns:
print(my_array.shape)

# Accessing elements of the array by index:
print(my_array[2])

# Show the dimensions of the array:
print(my_array.ndim)

# --- 2-Dimensional Arrays (Matrices) ---

# Create a new ndarray (2D) from scratch:
array_2d = np.array([
    [1, 2, 3, 9],
    [5, 6, 7, 8],
])

# Use f-strings to print information about the array:
print(f'array_2d has {array_2d.ndim} dimensions.')
print(f'Its shape is {array_2d.shape}.')
print(f'It has {array_2d.shape[0]} rows and {array_2d.shape[1]} columns.')
print(array_2d)

# Access the 3rd value of the array in the 2nd row:
print(array_2d[1, 2])

# Access all the values in the 1st row of the array:
print(array_2d[0, :])

# --- N-Dimensional Arrays (Tensors) ---
# How many dimensions does the array below have?
# What is its shape?
# Try to access the value "18" in the last line of code.
# Try to retrieve a 1-dimensional vector with values: '[97, 0, 27, 18]'
# Try to retrieve a (3, 2) matrix with values:
#   '[[0, 4], [7, 5], [5, 97]]'
mystery_array = np.array([
    [
        [0, 1, 2, 3],
        [4, 5, 6, 7],
    ],
    [
        [7, 86, 6, 98],
        [5, 1, 0, 4],
    ],
    [
        [5, 36, 32, 48],
        [97, 0, 27, 18],
    ],
])

print(f'We have {mystery_array.ndim} dimensions.')
print(f'The shape is {mystery_array.shape}.')

# Axis 0: 3rd element. Axis 1: 2nd element Axis 3: 4th element.
print(mystery_array[2, 1, 3])

# Retrieve all the elements on the 3rd axis that are at position 2 on the 1st
# axis & position 1 on the 2nd axis:
print(mystery_array[2, 1, :])

# Retrieve the all the 1st elements on axis number 3:
print(mystery_array[:, :, 0])

# --- NUMPY MINI-CHALLENGES ---

# --- Challenge 1 ---

# Use the arrange() function to create a vector "a" with values ranging from
# 10 to 29.
a = np.arange(10, 30)
print(a)

# --- Challenge 2 ---

# Use Python slicing techniques on "a" to create an array containing only the
# last 3 values of "a". Create a subset with only the 4th, 5th, & 6th values.
# Create a subset of "a" containing all the values except for the first 12
# values. Create a subset that only contains the even numbers.

# Last 3 values:
print(a[-3:])

# Subset with 4th, 5th, & 6th values:
print(a[3:6])

# All values except for the first 12 values:
print(a[12:])

# All even numbers:
print(a[::2])

# --- Challenge 3 ---

# Reverse the order of the values in "a" so that the first element comes last.
print(np.flip(a))

# --- Challenge 4 ---

# Print out all the indices of the non-zero elements in this array:
#   [6, 0, 9, 0, 0, 5, 0]
b = np.array([6, 0, 9, 0, 0, 5, 0])
nz_indices = np.nonzero(b)
print(nz_indices)

# --- Challenge 5 ---

# Use NumPy to generate a 3x3x3 array with random numbers:
z = random((3, 3, 3))
print(z)

# --- Challenge 6 ---

# Use the linspace() function to create a vector "x" of size 9 with values
# spaced out evenly between 0 to 100 (both included).
x = np.linspace(0, 100, num=9)
print(x)
print(x.shape)

# --- Challenge 7 ---

# Use the linspace() function to create another vector "y" of size 9 with
# values between -3 to 3 (both included). Then, plot "x" & "y" on a line
# chart using MatplotLib.
y = np.linspace(start=-3, stop=3, num=9)
print(y)
plt.plot(x, y)
plt.show()

# --- Challenge 8 ---

# Use NumPy to generate an array called "noise" with shape 128x128x3 that has
# random values. Then use MatplotLib's imshow() method to display the array
# as an image.
noise = np.random.random((128, 128, 3))
print(noise.shape)
plt.imshow(noise)

# --- Linear Algebra With Vectors ---

v1 = np.array([4, 5, 2, 7])
v2 = np.array([2, 1, 3, 3])
print(v1 + v2)

# --- Python Lists vs. ndarrays ---

list1 = [4, 5, 2, 7]
list2 = [2, 1, 3, 3]
print(list1 + list2)

# --- BROADCASTING AND SCALARS ---

array_2d = np.array([
    [1, 2, 3, 4],
    [5, 6, 7, 8],
])
print(f'Dimensions: {array_2d.ndim}.')
print(f'Shape: {array_2d.shape}.')
print(array_2d + 10)
print(array_2d * 5)

# --- Matrix Multiplication with @ and the matmul() method ---

a1 = np.array([
    [1, 3],
    [0, 1],
    [6, 2],
    [9, 7],
])
b1 = np.array([
    [4, 1, 4],
    [5, 8, 5],
])

print(f'{a1.shape}: a has {a1.shape[0]} rows and {a1.shape[1]} columns.')
print(f'{b1.shape}: b has {b1.shape[0]} rows and {b1.shape[1]} columns.')
print('Dimensions of result: (4x2)*(2x3)=(4x3)')

# Multiply "a1" with "b1". Use the matmul() function or the "@" operator.
c = np.matmul(a1, b1)
print(f'Matrix c has {c.shape[0]} rows and {c.shape[1]} columns')
print(c)

print(a1 @ b1)

# --- MANIPULATING IMAGES AS NDARRAYS ---

img = misc.face()
plt.imshow(img)

# What is the data type of "img"? Also, what is the shape of "img" & how many
# dimensions does it have? What is the resolution of the image?
print(type(img))
print(img.shape)
print(img.ndim)

# Convert the image to black & white. The values in our "img" range from 0 to
# 255. Divide all the values by 255 to convert them to sRGB, where all the
# values are between 0 and 1. Next, multiply the sRGB array by the
# "grey_vals" to convert the image to greyscale. Finally, use MatplotLib's
# imshow() method together with the colormap parameter set to gray (
# "cmap=gray") to look at the results.
grey_vals = np.array([
    0.2126, 0.7152, 0.0722
])
sRGB_array = img / 255
img_gray = sRGB_array @ grey_vals
#   img_gray = np.matmul(sRGB_array, grey_vals) is also acceptable.
plt.imshow(img_gray, cmap='gray')
plt.imshow(img_gray)

# Manipulate the images by doing some operations on the underlying ndarrays.
# Change the values in the ndarray so that:
# The grayscale image is flipped upside down.
# The color image is rotated.
# Invert the color image; do this by converting all the pixels to their
# opposite values.

np.flip(a1)
plt.imshow(np.flip(img_gray), cmap='gray')
print(a1)
print('a1 array rotated:')
np.rot90(a1)
plt.imshow(np.rot90(img))
solar_img = 255 - img
plt.imshow(solar_img)

# --- WORKING WITH IMAGES ---

file_name = 'yummy_macarons.jpg'

# Use the Pillow module to open the image:
my_img = Image.open(file_name)
img_array = np.array(my_img)
print(img_array.ndim)
print(img_array.shape)
plt.imshow(img_array)
plt.imshow(255 - img_array)
