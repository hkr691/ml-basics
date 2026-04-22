class SearchSortedArray:
  def get_index(self, array, target):
    
    if not array:
      return -1
    
    l, r = 0, len(array)  - 1
    
    while l <= r:
      mid = (l + r) // 2
      if array[mid] == target:
        return mid
      
      if array[l] <= array[mid]: #left half is sorted
        if array[l] <= target and array[mid] > target:
          r = mid -1
        else:
          l = mid + 1
      
      else:
        if array[mid] < target and array[r] >= target:
          l = mid + 1
        else:
          r = mid - 1
    return -1

    
