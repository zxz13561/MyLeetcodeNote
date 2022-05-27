from Tree_Node import TreeNode


class Solution(object):
    def levelOrder(self, root):
        if not root:
            return root

        node_q = [root]
        return_list = []

        while node_q:
            temp_val = []
            stack_list = []
            for node in node_q:
                temp_val.append(node.val)

                if node.left:
                    stack_list.append(node.left)

                if node.right:
                    stack_list.append(node.right)

            node_q = stack_list
            return_list.append(temp_val)
        return return_list


if __name__ == '__main__':
    input_root = TreeNode(3)
    r_node = TreeNode(20)
    r_node.left = TreeNode(15)
    r_node.right = TreeNode(7)
    input_root.right = r_node
    input_root.left = TreeNode(9)

    run = Solution()
    print(run.levelOrder(input_root))
