from itertools import groupby

from Tree_Node import TreeNode


class Solution(object):
    def isSymmetric(self, root):
        if not root:
            return root
        elif not root.left and not root.right:
            return True

        node_q = [root]

        while node_q.count(None) != len(node_q):
            stack_list = []
            left_val = []
            right_val = []

            for node in node_q[:len(node_q) // 2]:
                left_val.append(node.val if node else None)
                stack_list.append(node.left if node and node.left else None)
                stack_list.append(node.right if node and node.right else None)

            for node in node_q[len(node_q) // 2:]:
                right_val.append(node.val if node else None)
                stack_list.append(node.left if node and node.left else None)
                stack_list.append(node.right if node and node.right else None)

            if len(node_q) >= 2 and left_val != right_val[::-1]:
                return False

            node_q = stack_list
        return True

    def faster(self, root):
        def check_symmetry(node1, node2):
            if node1 is None and node2 is None:
                return True

            return (node1 and node2) and check_symmetry(node1.left, node2.right) \
                   and check_symmetry(node1.right, node2.left) and node1.val == node2.val

        def is_symmetrical_tree(root):
            if root is None:
                return True

            return check_symmetry(root.left, root.right)

        return is_symmetrical_tree(root)


if __name__ == '__main__':
    input_root = TreeNode(3)

    l_node = TreeNode(2)
    # l_node.left = TreeNode(3)
    l_node.right = TreeNode(4)
    input_root.left = l_node

    r_node = TreeNode(2)
    r_node.left = TreeNode(4)
    # r_node.right = TreeNode(3)
    input_root.right = r_node

    run = Solution()
    print(run.faster(input_root))
