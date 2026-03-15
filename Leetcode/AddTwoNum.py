# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val      # значение в узле (цифра)
        self.next = next    # ссылка на следующий узел

class Solution:
    def addTwoNumbers(self, l1: ListNode|None, l2: ListNode|None) -> ListNode:
        dummy = ListNode(0) # фиктивный узел
        curr = dummy        # ссылка на узел (т.е. будем менять его и создавать новые узлы)
        extra = 0           # доп.цифра (то что будем держать в уме)

        while l1 or l2 or extra:
            x = l1.val if l1 else 0
            y = l2.val if l2 else 0

            total = x + y + extra   # Сумма
            digit = total % 10      # следующее значение узла
            extra = total // 10     # держим в уме для следующей суммы

            curr.next = ListNode(digit)
            curr = curr.next

            # двигаем указатели по входным спискам вперёд
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        return dummy.next   # начинаем с первого полезного узла (т.е. 0 мы не считаем)


# Превращаем обычный список в связный
def make_list(nums):
    dummy = ListNode(0)
    cur = dummy
    for n in nums:
        cur.next = ListNode(n)
        cur = cur.next
    return dummy.next


#  Превращаем связный список обратно в обычный
def print_list(node):
    result = []
    while node:
        result.append(node.val)
        node = node.next
    print(result)


l1 = make_list([2, 4, 3])
l2 = make_list([5, 6, 4])

res = Solution()

print(l1)
print_list(res.addTwoNumbers(l1, l2))
