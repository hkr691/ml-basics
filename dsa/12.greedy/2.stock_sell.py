class Solution:
  def bestTime(self, stocks):
    if not stocks:
      return 0
    
    min_price = stocks[0]
    max_profit = 0
    
    for stock in stocks:
      min_price = min(min_price, stock)
      max_profit = max(max_profit, stock - min_price)
    
    return max_profit