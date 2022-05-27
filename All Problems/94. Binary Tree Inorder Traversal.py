from Tree_Node import TreeNode


class Solution(object):
    def inorderTraversal(self, root):
        if not root:
            return root

        result_list = []
        q_node = []
        stack_nodes = []
        current_node = root
        while True:
            if current_node:
                q_node.insert(0, current_node)
                stack_nodes.append(current_node.right)
                current_node = current_node.left
            else:
                current_node = stack_nodes.pop()

    def epic_solution(self, root):
        return self.epic_solution(root.left) + [root.val] + self.epic_solution(root.right) if root else []


if __name__ == '__main__':
    input_root = TreeNode(1)
    r_node = TreeNode(2)
    r_node.left = TreeNode(3)
    input_root.right = r_node

    run = Solution()
    print(run.epic_solution(input_root))
