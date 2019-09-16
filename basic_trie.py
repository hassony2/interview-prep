def construct_trie(suffixes, dico=None):
    if dico is None:
        dico = {}
    cont_suffixes = [suffix for suffix in suffixes if len(suffix)]
    first_lets = set([suffix[0] for suffix in cont_suffixes])
    for lett in first_lets:
        let_dic = {}
        let_suff = [suff[1:] for suff in cont_suffixes if suff[0] == lett]
        construct_trie(let_suff, dico=let_dic)
        dico[lett] = let_dic
    # We need a way to mark the end of a word
    # otherwise ['a', 'aa'] -> {'a': {'a'}: {}} -> ['aa']
    # Instead we mark end of words
    # ['a', 'aa'] -> {'a': {'end': {}, 'a': {'end': {}}}} -> ['a', 'aa']
    if len(cont_suffixes) < len(suffixes):
        dico['end'] = None
    return dico


def traverse_trie(trie):
    if not trie:
        return ['']
    else:
        all_res = []
        for key in trie.keys():
            if key == 'end':
                all_res.extend([''])
            else:
                all_res.extend([key + suffix for suffix in traverse_trie(trie[key])])
        return all_res
 

arr = ['aa', 'aab', 'bc', '', 'abc', 'abd', 'aedg']
trie = construct_trie(arr)
print(arr)
print(trie)
arrec = traverse_trie(trie)
print(arrec)
