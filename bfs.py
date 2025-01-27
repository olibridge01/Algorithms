from collections import deque

class TreeNode:
    def __init__(self, val=None, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def bfs(root):
    """Breadth-First Search to find maximum node value."""

    queue = deque()
    queue.append(root)
    max_val = -float('inf')

    while queue:
        node = queue.popleft()

        max_val = max(max_val, node.val)

        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    
    return max_val