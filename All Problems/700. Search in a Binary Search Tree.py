import Tree_Node
from CreateBinaryTree import CreateBinaryTree
from Tree_Node import TreeNode


class Solution(object):
    def searchBST(self, root: TreeNode, val) -> Tree_Node.TreeNode:
        print(root.val)
        if not root:
            return []
        elif root.val == val:
            return root
        elif root.val > val:
            return self.searchBST(root.left, val) if not root.left else []
        else:
            return self.searchBST(root.right, val) if not root.right else []


if __name__ == '__main__':
    data_list = [4, 2, 7, 1, 3]
    i_root = CreateBinaryTree().new_tree(data_list)
    i_val = 5

    run = Solution()
    node = run.searchBST(i_root, i_val)
    re_l = node.left
    re_r = node.right
    re_val = node.val
    print(re_val, re_l.val, re_r.val)
