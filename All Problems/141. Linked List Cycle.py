import List_Node

class Solution(object):
    def hasCycle(self, head) -> bool:
        check_list = []
        while head.next.val is not None:
            if head not in check_list:
                check_list.append(head)
            else:
                return True
            head = head.next
        return False

    def Faster_solution(self, head):
        fast, slow = head, head
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False


if __name__ == '__main__':
    vals = [3, 2, 0, -4]
    input_head = List_Node.ListNode(vals[0])
    next_node = input_head

    next_node.next = List_Node.ListNode(vals[1])
    temp_node = next_node.next

    next_node.next.next = List_Node.ListNode(vals[2])
    next_node.next.next.next = List_Node.ListNode(vals[3])
    next_node.next.next.next.next = temp_node

    run = Solution()
    print(run.Faster_solution(input_head))
