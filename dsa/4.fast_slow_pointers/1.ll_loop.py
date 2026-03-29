class LinkedListLoop:

  def loop_exists(self, head):
    if not head:
      return False
    slow = head
    fast = head
    #check both fast and fast.next to avoid null pointers
    
    while fast and fast.next:
      slow = slow.next
      fast = fast.next.next
      if slow == fast:
        return True
    return False

"""
time complexity: O(n) every node visited once
space complexity = O(1) not additional space since we don't use set to keep tracak of visited
"""
