from SelfCreateFunction.CreateBinaryTree import CreateBinaryTree


class Solution(object):
    def sumOfLeftLeaves(self, root):
        if not root.right and not root.left:
            return 0

        leaf_val = []
        if root.left:
            self.find_leaf(root.left, leaf_val, True)
        if root.right:
            self.find_leaf(root.right, leaf_val)

        return sum(leaf_val)

    def find_leaf(self, Node, leaf_val, isLeft=False):
        if Node.left:
            self.find_leaf(Node.left, leaf_val, True)
        if Node.right:
            self.find_leaf(Node.right, leaf_val)
        if not Node.left and not Node.right and isLeft:
            leaf_val.append(Node.val)


if __name__ == '__main__':
    tree_data = [1, 2]
    i_head = CreateBinaryTree().new_tree(tree_data)

    run = Solution()
    print(run.sumOfLeftLeaves(i_head))
