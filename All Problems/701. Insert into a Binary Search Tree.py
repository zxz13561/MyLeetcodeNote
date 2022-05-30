from SelfCreateFunction.CreateBinaryTree import CreateBinaryTree
from SelfCreateFunction.Tree_Node import TreeNode


class Solution(object):
    def insertIntoBST(self, root, val: int):
        if not root:
            root = TreeNode(val)
            return root

        temp_root = root
        self.insert_node(temp_root, val)

        return root

    def insert_node(self, root, val):
        if val > root.val:
            if root.right:
                return self.insertIntoBST(root.right, val)
            else:
                root.right = TreeNode(val)
                return

        if val < root.val:
            if root.left:
                return self.insertIntoBST(root.left, val)
            else:
                root.left = TreeNode(val)
                return


if __name__ == '__main__':
    data_list = [4, 2, 7, 1, 3]
    i_root = CreateBinaryTree().new_tree(data_list)
    i_val = 5

    run = Solution()
    run.insertIntoBST(i_root, i_val)

    print(i_root)
