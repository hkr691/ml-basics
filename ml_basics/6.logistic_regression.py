from numpy.typing import NDArray
import numpy as np

class LogisticRegression:
  def __init__(self, iterations: int, learning_rate: float):
    self.iterations = iterations
    self.learning_rate = learning_rate
    self.weights: NDArray[np.float64] = None
    self.bias = 0.0
  
  def _sigmoid(self, z: NDArray[np.float64]) -> NDArray[np.float64]:
    z_clipped = np.clip(z, -500, 500)
    return 1 / (1 + np.exp(-z_clipped))
  
  
  def fit(self, X: NDArray[np.float64], y: NDArray[np.float64]) -> None:
    X, y = np.asarray(X), np.asarray(y)
    m, n = X.shape
    
    self.weights = np.zeros(n)
    self.bias = 0.0
    
    for _ in range(self.iterations):
      linear = np.dot(X, self.weights) + self.bias
      y_pred = self._sigmoid(linear)
      
      error = y_pred - y
      dw = (1 / m) * np.dot(X.T, error)
      db = (1 / m) * np.sum(error)
      
      self.weights -= self.learning_rate * dw
      self.bias -= self.learning_rate * db

  def predict_prob(self, X: NDArray[np.float64]) -> NDArray[np.float64]:
    X = X.asarray(X)
    linear_model = np.dot(X, self.weights) + self.bias
    return self._sigmoid(linear_model)
  
  def predict(self, X: NDArray[np.float64], threshold: float = 0.5) -> NDArray[np.int64]:
    probabilities = self.predict_prob(X)
    return (probabilities > threshold).astype(np.int64)
