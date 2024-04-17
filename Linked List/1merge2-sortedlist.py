#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        head = list1
        prev = None
        
        while list1 is not None and list2 is not None:
            if list1.val <= list2.val:
                prev = list1
                list1 = list1.next
            else:
                if prev is None:
                    prev = list2
                    list2 = list2.next
                    prev.next = list1
                    head = prev
                else:
                    prev.next = list2
                    list2 = list2.next
                    prev.next.next = list1
                    prev = prev.next
        
        if list2 is not None:
            if prev is None:
                head = list2
            else:
                prev.next = list2

        return head