class LinkedListMidpoint:
  def get_midpoint(self, head):
    if not head:
      return head
    slow, fast = head, head
    
    while fast and fast.next:
      slow = slow.next
      fast = fast.next.next
    return slow #returns second middle node if len of ll is even
