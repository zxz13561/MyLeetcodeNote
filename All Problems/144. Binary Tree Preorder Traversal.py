from Tree_Node import TreeNode


class Solution(object):
    def preorderTraversal(self, root):
        res, stack, curr = [], [], root
        while curr or stack:
            if curr:
                res.append(curr.val)
                stack.append(curr.right)  # Save right node into stack list
                curr = curr.left  # next loop check left node is existed
            else:
                curr = stack.pop()  # if left node not exist, swap to right node
        return res


if __name__ == '__main__':
    input_root = TreeNode(1)
    l_node = TreeNode(2)
    l_node.left = TreeNode(3)
    l_node.right = TreeNode(4)
    r_node = TreeNode(5)
    r_node.left = TreeNode(6)
    r_node.right = TreeNode(7)
    input_root.left = l_node
    input_root.right = r_node
    """
           1
        /     \ 
       2       5   
     /   \   /   \ 
    3     4 6     7
    check this function using deep first search
    """

    run = Solution()
    print(run.preorderTraversal(input_root))
