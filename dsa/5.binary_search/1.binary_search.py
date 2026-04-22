class BinarySearch:
  def search(self, arr, target):
    if not arr:
      return None
    
    l, r = 0, len(arr) - 1
    
    while l <= r:
      mid = (l + r) // 2
      if arr[mid] == target:
        return mid
      elif arr[mid] > target:
        r = mid - 1
      else:
        l = mid + 1
    return -1


arr = [1,2,3,4,5,6]
target = 9
bs = BinarySearch()
print(bs.search(arr, target))
