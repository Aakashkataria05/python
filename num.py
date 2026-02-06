import numpy as np
numpy_array = np.array([1,2,3,4,5])
# print(numpy_array)

# ones_array = np.ones((2,3))
# print(ones_array)

# filled_array = np.full((2,4),9)
# print(filled_array.shape)
# print(filled_array.size)
# print(filled_array.astype(str))

new_arr = np.insert(numpy_array, 3, 100)
print(new_arr)