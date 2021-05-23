# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

#
# 
# @param root TreeNode类 
# @param sum int整型 
# @return bool布尔型
#
class Solution:
    def hasPathSum(self , root , Sum):
        if not root:
            return False
        if (root.val == Sum):
            if not root.left and not root.right :
                return True
        if root.val < Sum:
            if root.left:
                self.hasPathSum(root.left, Sum - root.val)
            if root.right:
                self.hasPathSum(root.right, Sum - root.val)
        else:
            return False
        # write code here