# Definition for a binary tree node.
class Node(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

  def isSameTree(p, q):
      """
      :type p: Node
      :type q: Node
      :rtype: bool
      """
      trav_p = self.traversal(p)
      trav_q = self.traversal(q)
      return trav_p == trav_q


  def traversal(self, root):
      # Breadth-First-Traversal except None is included when child is missing to prevent
      #   2  and 2
      #  /        \
      # 1          1
      # To both be projected to [2, 1]
      if root is None:
          return [None]
      else:
          return [root.val] + self.traversal(root.left) + self.traversal(root.right)



        
