# https://practice.geeksforgeeks.org/problems/serialize-and-deserialize-a-binary-tree/1?page=1&category[]=Tree&curated[]=1&sortBy=submissions
'''
class Node:
    def __init__(self,val):
        self.data = val
        self.left = None
        self.right = None
'''

#Function to serialize a tree and return a list containing nodes of tree.
def serialize(root, A):
    #code here
    if not root:
        return A
    A.append(root.data)
    cur = [root]
    while cur:
        node = cur.pop(0)
        if node.left:
            cur.append(node.left)
            A.append(node.left.data)
        else:
            A.append(None)

        if node.right:
            cur.append(node.right)
            A.append(node.right.data)
        else:
            A.append(None)

    return A


#Function to deserialize a list and construct the tree.
def deSerialize(A):
    #code here
    if not A:
        return None

    root = Node(A[0])

    cur = [root] # store real nodes with left and right children need be filled
    i = 1
    while cur:
        node = cur.pop(0)
        if A[i] is None:
            node.left = None
        else:
            node.left = Node(A[i])
            cur.append(node.left)
        if A[i+1] is None:
            node.right = None
        else:
            node.right = Node(A[i+1])
            cur.append(node.right)
        i += 2

    return root
