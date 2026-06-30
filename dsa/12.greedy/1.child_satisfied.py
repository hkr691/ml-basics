class Solution:
  def findContentChildren(self, greeds, cookies):
    if not greeds or not cookies:
      return 0
      
    greeds.sort()
    cookies.sort()
    satisfied = 0
    i, j = 0, 0
    
    while i < len(greeds) and j < len(cookies):
      if cookies[j] >= greeds[i]:
        satisfied += 1
        i += 1
      j += 1
    
    return satisfied