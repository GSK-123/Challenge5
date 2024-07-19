class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root is None:
            return []

        stack, output = [], []
        previous = None
        current = root

        while stack or current:
            if current:
                stack.append(current)
                current = current.left
            else:
                peek = stack[-1]
                if peek.right and previous != peek.right:
                    current = peek.right
                else:
                    output.append(peek.val)
                    previous = stack.pop()

        return output