def traverse_tree(tree, depth=1):
    results = []
    if depth == 0:
        return ['']
    elif depth == 1:
        return tree.keys()
    else:
        results.extend(tree.keys())
        for key in tree.keys():
            results.extend([key + rem for rem in traverse_tree(tree[key], depth=depth-1)])
    return results

def construct_tree(tiles, res=None):
    for char_idx in range(len(tiles)):
        rem_tiles = tiles[:char_idx] + tiles[char_idx + 1:]
        res[tiles[char_idx]] = construct_tree(rem_tiles, {})
    return res



tiless = ['AAB', 'AB']
for tiles in tiless:
    tree = construct_tree(tiles, {})
    print(tree)
    results = traverse_tree(tree, depth=len(tiles))
    print(results)
    print(len(set(results)))
    
