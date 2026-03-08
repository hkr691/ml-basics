class ReverseLinkedList:
    def reverse(self, head):
        # reverse direction of arrow pointing in the linked list
        curr, prev = head, None
        while curr:
            # keep track of next node not to break link with next element
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        return prev