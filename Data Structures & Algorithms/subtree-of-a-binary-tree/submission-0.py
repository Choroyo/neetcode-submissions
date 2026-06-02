# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot:
            return True

        if not root:
            return False

        if self.sameTree(root, subRoot):
            return True
        
        return (self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot))
        



    def sameTree(self, curr, currSub):
        if not curr and not currSub:
            return True
        
        if not curr or not currSub:
            return False
        
        if curr.val != currSub.val:
            return False
        
        return (self.sameTree(curr.left, currSub.left) and self.sameTree(curr.right, currSub.right))