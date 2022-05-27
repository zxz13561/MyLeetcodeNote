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


def delete_duplicates(head: ListNode) -> ListNode:
    cur = head
    while cur:
        print(cur.val)
        while cur.next and cur.next.val == cur.val:
            cur.next = cur.next.next
        cur = cur.next
    return head


if __name__ == '__main__':
    list_s = SingleLinkedList()
    for num in [1, 1, 2, 3, 3, 4]:
        list_s.append(num)

    delete_duplicates(list_s.head)
    print(list_s)
