import numpy as np
from numpy.typing import NDArray

class Softmax:
  def softmax(self, z: NDArray[np.float64]) -> NDArray[np.float64]:
    z = np.asarray(z)
    row_max = np.max(z, axis=-1, keepdims=True)
    shifted = z - row_max
    exps = np.exp(shifted)
    return np.round(exps / np.sum(exps, axis=-1, keepdims=True), 5)
