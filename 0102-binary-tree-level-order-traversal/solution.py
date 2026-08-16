# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # def Depth(root):
        #     if (root == None):
        #         return 0
        #     return 1+max(Depth(root.left),Depth(root.right))
        final=[]
        def b_order(root,k):
            if(root == None):
                return
            if(k == len(final)):
                final.append([])
            final[k].append(root.val)
            k+=1
            b_order(root.left,k)
            b_order(root.right,k)
        b_order(root,0)
        return final
        
        
