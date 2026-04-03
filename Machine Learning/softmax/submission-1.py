import numpy as np
from numpy.typing import NDArray


class Solution:

    def softmax(self, z: NDArray[np.float64]) -> NDArray[np.float64]:
        # z is a 1D NumPy array of logits
        # Hint: subtract max(z) for numerical stability before computing exp
        # return np.round(your_answer, 4)
        z_stable = z - np.max(z)
        sum = 0
        for i in z_stable: sum += np.exp(i)
        res = np.zeros_like(z)
        for i in range (len(z_stable)): 
            res[i] = np.round (np.exp(z_stable[i]) / sum, 4)
        return res