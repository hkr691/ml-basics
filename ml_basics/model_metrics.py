from typing import List

class Metrics:
  def accuracy(self, y_actual: List, y_pred: List) -> float:
    if not y_actual or not y_pred or len(y_actual) != len(y_pred):
      raise ValueError("Inputs need to non empty and of same lengths")
    
    correct_preds = sum(actual == pred for actual, pred in zip(y_actual, y_pred))
    return correct_preds / len(y_actual)
  
  def precision(self, y_actual: List, y_pred: List) -> float:
    if not y_actual or not y_pred or len(y_actual) != len(y_pred):
      raise ValueError("Inputs need to non empty and of same lengths")
    
    tp = sum(actual == 1 and pred == 1 for actual, pred in zip(y_actual, y_pred))
    total_pos_pred = sum(pred == 1 for pred in y_pred)
    
    if total_pos_pred == 0: return 0
    return tp / total_pos_pred
  
  def recall(self, y_actual: List, y_pred: List) -> float:
    if not y_actual or not y_pred or len(y_actual) != len(y_pred):
      raise ValueError("Inputs need to non empty and of same lengths")
    
    tp = sum(actual == 1 and pred == 1 for actual, pred in zip(y_actual, y_pred))
    fn = sum(actual == 1 and pred == 0 for actual, pred in zip(y_actual, y_pred))
    
    if (tp + fn == 0): return 0
    return tp / (tp + fn)
  
  def f1_score(self, y_actual: List, y_pred: List) -> float:
    p = self.precision(y_actual, y_pred)
    r = self.recall(y_actual, y_pred)
    
    if p + r == 0: return 0
    return (2 * p * r) / (p + r)
