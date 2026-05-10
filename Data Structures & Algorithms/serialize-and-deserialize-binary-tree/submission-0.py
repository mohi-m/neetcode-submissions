# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:

        que = deque()
        que.append(root)
        res = []
        
        while que:
            node = que.popleft()

            if not node:
                res.append("N")
                continue
            
            que.append(node.left)
            que.append(node.right)
            res.append(str(node.val))

        return ",".join(res)

        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:

        tree = data.split(",")
        if tree[0] == "N":
            return None
        root = TreeNode(int(tree[0]))
        que = deque()
        que.append(root)
        index = 1
        while que:
            node = que.popleft()
            if tree[index] != "N":
                node.left = TreeNode(int(tree[index]))
                que.append(node.left)
            index += 1
            if tree[index] != "N":
                node.right = TreeNode(int(tree[index]))
                que.append(node.right)
            index += 1
        
        return root
        





