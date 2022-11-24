class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        """
        if root == None:
            return 0;
        depth = 1
        
        queue = []
        queue.append(root)
        
        while(queue):
            size = len(queue)
            while(size!=0):
                node = queue[0]
                queue.pop(0)
                
                if node.left == None and node.right == None:
                    return depth
                 
                if node.left != None:
                    queue.append(node.left)
                    
                if node.right != None:
                    queue.append(node.right)
                
                size -= 1
            depth += 1
            
        return depth