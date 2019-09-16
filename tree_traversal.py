def bfs(node):
    queue = [node]
    traversed = []
    while queue:
        node = queue.pop(0)
        traversed.append(node.val)
        for child in node.children:
            queue.append(child)
    return traversed


def dfs(node):
    if node.children:
        # Preorder
        traverse = [node.val]
        for child in node.children:
            traverse.extend(dfs(child))
    else:
        return [node.val]
    return traverse


class Node(object):
    def __init__(self, val, children=None):
        if children is None:
            self.children = []
        else:
            self.children = children
        self.val = val

root = Node(1, children=[Node(2), Node(3), Node(4, [Node(5)]), Node(6, [Node(7, [Node(8), Node(9), Node(10)])]), Node(11)])
res = bfs(root)
print(f'bfs : {res}')
res = dfs(root)
print(f'dfs : {res}')

