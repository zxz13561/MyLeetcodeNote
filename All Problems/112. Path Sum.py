from CreateBinaryTree import CreateBinaryTree


class Solution(object):
    def hasPathSum(self, root, targetSum) -> bool:
        if not root:
            return False

        if not root.left and not root.right and root.val == targetSum:
            return True

        targetSum -= root.val

        return self.hasPathSum(root.left, targetSum) or self.hasPathSum(root.right, targetSum)


if __name__ == '__main__':
    i_targetSum = 22
    t_data = [5, 4, 8, 11, None, 13, 4, 7, 2, None, None, None, 1]
    get = CreateBinaryTree()
    i_root = get.new_tree(t_data)

    run = Solution()
    print(run.hasPathSum(i_root, i_targetSum))
