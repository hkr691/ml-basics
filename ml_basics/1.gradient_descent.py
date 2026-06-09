class GradientDescent:
  def compute(self, iterations: int, learning_rate: float, init: int) -> float:
    if iterations < 0:
      raise ValueError("Number of Iterations cannot be negative")
    if learning_rate <= 0:
      raise ValueError("Learning rate should strictly be poistive")
    
    
    minimizer = float(init)
    
    for _ in range(iterations):
      derivative = 2 * minimizer
      update = learning_rate * derivative
      
      #early stopping
      if abs(update) <= 1e-7:
        break
      minimizer -= update
    
    return round(minimizer, 5)
