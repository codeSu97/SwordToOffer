# Definition for singly-linked list.
from typing import List


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # 辅助栈
    def reversePrint(self, head: ListNode) -> List[int]:
        result = []
        while head:
            result.append(head.val)
            head = head.next
        return result[::-1]

    # 递归
    def reversePrint1(self, head: ListNode) -> List[int]:
        return self.reversePrint1(head.next) + [head.val] if head else []
