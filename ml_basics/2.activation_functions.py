import numpy as np
from numpy.typing import NDArray

class BasicActivationFuctions:
  def sigmoid(self, z: NDArray[np.float64]) -> NDArray[np.float64]:
    z = np.asarray(z, dtype=np.float64)
    z_clipped = np.clip(z, -500, 500)
    return np.round(1 / (1 + np.exp(-z_clipped)), 5)
    
  def relu(self, z: NDArray[np.float64]) -> NDArray[np.float64]:
    z = np.asarray(z, dtype=np.float64)
    return np.maximum(0, z)
    
