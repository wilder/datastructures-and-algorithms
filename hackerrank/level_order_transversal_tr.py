def levelOrder(root):
    if root:
        from Queue import Queue
        queue = Queue()
        queue.put(root)

        while not queue.empty():
            current = queue.get(False)
            print current.data,
            if current.left:
                queue.put(current.left)
            if current.right:
                queue.put(current.right)
