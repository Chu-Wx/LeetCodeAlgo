def findNode(self, head, val):
        while head and head.val != val: 
            head = head.next
        return head
