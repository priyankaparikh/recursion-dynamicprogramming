def mirror(self, root):
    if root:
        mirror(root.left)
        mirror(root.right)
