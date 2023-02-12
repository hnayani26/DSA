class Solution(object):
    def goodNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
            
        def dfs(root,max_val):
            if root is None:
                return 0 
            
            total = 0
            
            if(root.val>=max_val):
                total+=1
                max_val=root.val            #state
                
            total+= dfs(root.left,max_val)
            total+= dfs(root.right,max_val)        
            
            return total #return total
        
        return dfs(root,-9999999999)
            