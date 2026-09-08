import numpy as np

arr = np.array([[1,2,3],[4,5,6]])
print("Array:\n", arr)
print("Indexing arr[0,1]:", arr[0,1])
print("Slicing first row:", arr[0, 0:2])
print("Reshape 3x2:\n", arr.reshape(3,2))
print("Add 10:\n", arr + 10)
print("Mean:", np.mean(arr))
