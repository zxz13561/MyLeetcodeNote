import List_Node

class Solution(object):
    def reverse_list(self, head):
        node_list = []

        while head:
            node_list.append(head.val)
            head = head.next

        if len(node_list) < 1:
            return

        node_list = node_list[::-1]
        re_head = List_Node.ListNode(node_list[0])
        temp_re = re_head

        for node_val in node_list[1:]:
            temp_re.next = List_Node.ListNode(node_val)
            temp_re = temp_re.next

        return re_head

    def less_memory(self, head):
        prev = None
        curr = head

        while curr:
            temp = curr.next
            curr.next = prev
            prev, curr = curr, temp

        return prev


if __name__ == '__main__':
    head_list = [1, 2]
    input_head = List_Node.ListNode(head_list[0])
    temp_node = input_head
    for val in head_list[1:]:
        temp_node.next = List_Node.ListNode(val)
        temp_node = temp_node.next

    run_function = Solution()
    input_head = run_function.reverse_list(input_head)

    while input_head:
        print(input_head.val)
        input_head = input_head.next