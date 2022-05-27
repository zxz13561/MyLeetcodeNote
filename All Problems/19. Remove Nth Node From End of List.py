class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class SingleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, data):
        # 建立 class Node 的instance(實體)
        new_node = ListNode(data)

        # 如果head == None 代表為第一個Node
        if self.head is None:
            self.head = new_node
            self.tail = new_node

        else:
            self.tail.next = new_node
            self.tail = self.tail.next


def remove_nth_form_end(head, n):
    fast, slow = head, head
    for _ in range(n):
        fast = fast.next
        print(fast.val)
    if not fast:
        return fast.next
    while fast.next:
        fast, slow = fast.next, slow.next
        print(fast.val, slow.val)
    print(slow.next.val)
    slow.next = slow.next.next
    print(slow.next.val)
    return head


if __name__ == '__main__':
    list_s = SingleLinkedList()
    for num in [1, 2, 3, 4, 5]:
        list_s.append(num)

    print(remove_nth_form_end(list_s.head, 2))
