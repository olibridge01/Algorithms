class TreeNode:
    def __init__(self, val=None, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def dfs(node, max_val):
    """Depth-First Search to find maximum node value."""

    # Base case
    if node is None:
        return max_val
    
    # Check if current node is new maximum value
    max_val = max(max_val, node.val)

    #  Recurse down left side, then right side
    max_val = dfs(node.left, max_val)
    max_val = dfs(node.right, max_val)

    return max_val