class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


if __name__ == '__main__':
    # tree_data = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P']
    tree_data = [5, 4, 8, 11, None, 13, 4, 7, 2, None, None, None, 1]
    node_queue = {}  # setting queue

    # set up first node and value
    root = TreeNode(tree_data[0])
    root.val = tree_data[0]
    node_queue[0] = root

    # first node level and first queue element
    level = 1
    count = 0

    # setting up start queue index and end index
    start = 2 ** level - 1
    end = 2 ** level + start
    print(start, end, level)

    while 2 ** level <= len(tree_data):
        # default to left node first
        isLeft = True
        isRight = False

        # loop element in list
        for i in range(start, end):
            # set left node
            if isLeft and i <= len(tree_data) - 1:
                # get parent node from queue, and setting left node
                node_queue[count].left = TreeNode(tree_data[i])

                # write left node into queue as new element
                node_queue[i] = node_queue[count].left

                # change to right
                isLeft = False
                isRight = True

                # continue for loop
                continue

            # set right node
            if isRight and i <= len(tree_data) - 1:
                # get parent node from queue, and setting right node
                node_queue[count].right = TreeNode(tree_data[i])

                # write left node into queue as new element
                node_queue[i] = node_queue[count].right

                # change to left
                isLeft = True
                isRight = False

                # because is finish left and right node, change to another parent node
                count += 1

        # set new start index and end index
        start = end
        end = 2 ** level + start + 2

        # shift down node level
        level += 1
        print(start, end, level)

    print(root)
