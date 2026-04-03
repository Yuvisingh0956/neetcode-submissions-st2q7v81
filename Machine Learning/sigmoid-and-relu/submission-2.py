# import numpy as np
# import math
# from numpy.typing import NDArray


# class Solution:
    
#     def sigmoid(self, z: NDArray[np.float64]) -> NDArray[np.float64]:
#         # z is a 1D NumPy array
#         # Formula: 1 / (1 + e^(-z))
#         # return np.round(your_answer, 5)
#         for i in range (len(z)):
#             z[i] = np.round(1/ (1 + (math.e ** (-1* z[i]))),5)
#         return z

#     def relu(self, z: NDArray[np.float64]) -> NDArray[np.float64]:
#         # z is a 1D NumPy array
#         # Formula: max(0, z) element-wise
#         for i in range (len(z)):
#             z[i] = max(0, z[i])
#         return z



import numpy as np
from numpy.typing import NDArray


class Solution:
    
    def sigmoid(self, z: NDArray[np.float64]) -> NDArray[np.float64]:
        # z is a 1D NumPy array
        # Formula: 1 / (1 + e^(-z))
        # return np.round(your_answer, 5)
        return np.round(1.0 / (1.0 + np.exp(-z)), 5)

    def relu(self, z: NDArray[np.float64]) -> NDArray[np.float64]:
        # z is a 1D NumPy array
        # Formula: max(0, z) element-wise
        return np.maximum(0, z)
