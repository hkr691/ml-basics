from numpy.typing import NDArray
import numpy as np

class LinearRegression:
  def __init__(self, iterations: int, learning_rate: float):
    self.iterations = iterations
    self.learning_rate = learning_rate
    self.weights: NDArray[np.float64] = None
    self.bias = 0.0
  
  
  def fit(self, X: NDArray[np.float64], y: NDArray[np.float64]) -> None:
    X, y = np.asarray(X), np.asarray(y)
    m, n = X.shape
    
    self.weights = np.zeros(n)
    self.bias = 0
    
    for _ in range(self.iterations):
      y_pred = np.dot(X, self.weights) + self.bias
      
      error = y_pred - y
      dW = (2 / m) * np.dot(X.T, error)
      db = (2/ m) * np.sum(error)
      
      self.weights -= self.learning_rate * dW
      self.bias -= self.learning_rate * db
      
      
  def predict(self, X: NDArray[np.float64]) -> NDArray[np.float64]:
    X = np.asarray(X)
    return np.dot(X, self.weights) + self.bias
