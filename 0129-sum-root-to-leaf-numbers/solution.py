# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: TreeNode | None) -> int:
        ans=0
        string=0
        def dfs(root,num):
            if(root is None):
                return
            nonlocal ans
            if(root.left is None and root.right is None):
                ans+=num*10+root.val
                return
            print(num)
            num=num*10+root.val
            dfs(root.left,num)
            dfs(root.right,num)
        dfs(root,string)
        return ans
            
        
