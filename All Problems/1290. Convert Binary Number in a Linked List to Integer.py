from SelfCreateFunction.List_Node import ListNode

class Solution(object):
    def getDecimalValue(self, head):
        node_values = ""
        while head:
            node_values += str(head.val)
            head = head.next
        return int(node_values, 2)


if __name__ == '__main__':
    head_val = [0]
    i_head = ListNode().Create_Node(head_val)

    run = Solution()
    print(run.getDecimalValue(i_head))
