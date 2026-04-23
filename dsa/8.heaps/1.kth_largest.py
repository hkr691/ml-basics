import heapq

class KLargestElement:

  def get_kth_largest(self, array, k):    
    if not array or k > len(array):
      return -1
    
    min_heap = []
    
    for num in array:
      if len(min_heap) < k:
        heapq.heappush(min_heap, num)
      else:
        heapq.heappushpop(min_heap, num)
    
    return min_heap[0]

