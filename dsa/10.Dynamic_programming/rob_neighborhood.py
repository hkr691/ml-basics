class MaxTreasure:
  def rob_neighborhood(self, treasure):
    """
    recursive approach minus the memoization
    """
    if not treasure:
      return 0
    
    def rob_helper(i):
      if i == 0:
        return 0
      if i == 1:
        return treasure[0]
      
      skip = rob_helper(i - 1)
      take = rob_helper(i - 2) + treasure[i -1]
      
      return max(skip, take)
    
    return rob_helper(len(treasure))
  
  def rob_neighborhood(self, treasure):
    """
    recursive approach minus the memoization
    """
    if not treasure:
      return 0
    
    memo = {}
    
    def rob_helper(i):
      if i == 0:
        return 0
      if i == 1:
        return treasure[0]
      
      if i in memo:
        return memo[i]
      
      skip = rob_helper(i - 1)
      take = rob_helper(i - 2) + treasure[i -1]
      memo[i] = max(skip, take)
      
      return memo[i]
    
    return rob_helper(len(treasure))
    
    
