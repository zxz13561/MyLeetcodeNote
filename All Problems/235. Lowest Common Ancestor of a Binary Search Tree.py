from SelfCreateFunction.CreateBinaryTree import CreateBinaryTree


class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        mininum_val = p.val if p.val < q.val else q.val
        maxinum_val = p.val if p.val > q.val else q.val

        while True:
            if mininum_val < root.val < maxinum_val:
                return root
            elif p.val == root.val or q.val == root.val:
                return root
            elif root.val > maxinum_val:
                root = root.left
            else:
                root = root.right


if __name__ == '__main__':
    tree_data = [6, 2, 8, 0, 4, 7, 9, None, None, 3, 5]
    p_data = [4, 3, 5]
    q_data = [2, 0, 4]
    i_root = CreateBinaryTree().new_tree(tree_data)
    i_p = CreateBinaryTree().new_tree(p_data)
    i_q = CreateBinaryTree().new_tree(q_data)

    run = Solution()
    print(run.lowestCommonAncestor(i_root, i_p, i_q).val)
