class RemoveKthLast:
    def remove_kth_last(self, head, k):
        #have a dummy node to point to head to return head after element removed
        dummy = ListNode(-1)
        dummy.next = head
        leader, trailer = dummy, dummy

        for _ in range(k):
            leader = leader.next
            if not leader: #if k is larger than list length
                return head
        
        while leader.next:
            leader = leader.next
            trailer = trailer.next
        
        #deleting list node
        trailer.next = trailer.next.next
        return dummy.next
        
