from SelfCreateFunction.CreateBinaryTree import CreateBinaryTree


class Solution(object):
    def findTarget(self, root, k):
        global node_list
        node_list = []

        self.search_node(root)
        for index, val in enumerate(node_list):
            if k - val in node_list[index + 1:]:
                return True
        return False

    def search_node(self, root):
        if not root:
            return

        node_list.append(root.val)
        self.search_node(root.left if root.left else None)
        self.search_node(root.right if root.right else None)


if __name__ == '__main__':
    #tree_data = [5, 3, 6, 2, 4, None, 7]
    #tree_data = [1]
    tree_data = [0, -2, 3, None, -1, None, 4]
    i_root = CreateBinaryTree().new_tree(tree_data)
    i_k = -2

    run = Solution()
    print(run.findTarget(i_root, i_k))
