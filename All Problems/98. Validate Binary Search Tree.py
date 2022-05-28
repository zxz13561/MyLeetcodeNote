from SelfCreateFunction.CreateBinaryTree import CreateBinaryTree


class Solution(object):
    def isValidBST(self, root):
        return self.check_valid(root, float("-inf"), float("inf"))

    def check_valid(self, node, min_val, max_val):
        if node is None:
            return True
        if node.val >= max_val:
            return False
        if node.val <= min_val:
            return False
        left = self.check_valid(node.left, min_val, node.val)
        right = self.check_valid(node.right, node.val, max_val)
        return left and right


if __name__ == '__main__':
    tree_data = [0, -1]
    i_root = CreateBinaryTree().new_tree(tree_data)

    run = Solution()
    print(run.isValidBST(i_root))
