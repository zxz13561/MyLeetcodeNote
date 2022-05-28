from SelfCreateFunction.CreateBinaryTree import CreateBinaryTree


class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        if p < root.val and q > root.val:
            return root.val

        LCA = root.val

        if root.right and p == root.right.val:
            LCA = root.val

        if root.left and p == root.left.val:
            LCA = root.val

        if p < root.val:
            self.lowestCommonAncestor(root.left if root.left else None, p, q)

        if p > root.val:
            self.lowestCommonAncestor(root.right if root.right else None, p, q)

        return LCA


if __name__ == '__main__':
    tree_data = [6, 2, 8, 0, 4, 7, 9, None, None, 3, 5]
    i_root = CreateBinaryTree().new_tree(tree_data)
    i_p = 3
    i_q = 8

    run = Solution()
    print(run.lowestCommonAncestor(i_root, i_p, i_q))
