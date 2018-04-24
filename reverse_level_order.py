def traverse(self, root):
    """ use a stack and a qeue for this algorithm. time O(n), space O(N)"""
    if root = null:
        return

    s = stack()
    q = queue()

    q.add(root)

    while not q.isempty():
        root = q.top()
        if root.right:
            q.add(root.right)
        if root.left:
            q.add(root.left)
        s.push(root)

    while no s.isempty():
        print (s.pop().data)
