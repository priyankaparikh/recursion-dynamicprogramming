def root_leaf_sum(self, root, target, result):
    """ O(N)to search for a root to leaf path that returns true for a
    specific sum """

    if not root:
        return False

    #check if current node is a leaf node
    if not root.left and if not root.right:
        if root.data == target:
            result += root.data
            return True

        else:
            return False

    if root_leaf_sum(root.left, target, result):
        if root.data == target:
            result += root.left.data
            return True

    if root_leaf_sum(root.right, target, result):
        if root.data == target:
            result += root.left.data
            return True

    return False
