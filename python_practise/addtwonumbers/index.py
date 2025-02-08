from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def _to_integer(x: [ListNode]):
    x_string = ""
    node = x
    while True:
        x_string += str(node.val)
        if node.next:
            node = node.next
        else:
            break
    return int(x_string[::-1])

def _to_listNode(y):
    y_string = str(y)
    y_string = y_string

    i = 0
    _next = None
    y_node = None
    for t in y_string:
        y_node = ListNode(val=int(t), next=_next)
        _next = y_node

    return y_node
        

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l1_int = _to_integer(l1)
        l2_int = _to_integer(l2)

        sum_l = l1_int + l2_int
        return _to_listNode(sum_l)


        