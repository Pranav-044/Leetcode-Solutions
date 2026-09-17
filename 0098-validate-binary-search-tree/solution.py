class Solution:
    def isValidBST(self, root: TreeNode | None) -> bool:
        if root == None:
            return True

        is_bst=True

        def dfs(root,checks,prev,left,right):
            nonlocal is_bst

            if(root == None):
                return

            if(left and root.val>=prev):
                is_bst=False

            elif(left and root.val<prev):
                for i in range(len(checks)):
                    if(checks[i][1]=="right" and root.val<=checks[i][0]):
                        is_bst=False
                        break
                    elif(checks[i][1]=="left" and root.val>=checks[i][0]):
                        is_bst=False
                        break

            elif(right and root.val<=prev):
                is_bst=False

            elif(right and root.val>prev):
                for i in range(len(checks)):
                    if(checks[i][1]=="right" and root.val<=checks[i][0]):
                        is_bst=False
                        break
                    elif(checks[i][1]=="left" and root.val>=checks[i][0]):
                        is_bst=False
                        break

            prev=root.val

            dfs(root.left,checks+[(prev,"left")],prev,1,0)
            dfs(root.right,checks+[(prev,"right")],prev,0,1)

            return is_bst

        return dfs(root,[],root.val,0,0)
