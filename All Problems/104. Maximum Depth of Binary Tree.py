class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def max_depth(self, root) -> int:
        if not root:
            return 0
        leftMaxDepth = self.maxDepth(root.left)
        rightMaxDepth = self.maxDepth(root.right)
        rootDepth = max(leftMaxDepth, rightMaxDepth) + 1
        return rootDepth


if __name__ == '__main__':
    call_def = Solution()
    print(call_def.max_depth(3))
