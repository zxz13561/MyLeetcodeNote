class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def Create_Node(self, val_list):
        head = ListNode(val_list[0])
        temp_node = head

        for val in val_list[1:]:
            temp_node.next = ListNode(val)
            temp_node = temp_node.next

        return head
