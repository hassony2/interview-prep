class HashTable:
    def __init__(self, table_size=10):
        self.table_size = table_size
        self.table = [[] for _ in range(self.table_size)]

    def hash_func(self, key):
        return key % self.table_size

    def set(self, key, value):
        hash_k = self.hash_func(key)
        chain = self.table[hash_k]
        for chain_idx, (chain_k, _) in enumerate(chain):
            if chain_k == key:
                chain[chain_idx] = (key, value)
                return
        chain.append((key, value))

    def get(self, query):
        hash_k = self.hash_func(query)
        chain = self.table[hash_k]
        for key, val in chain:
            if key == query:
                return val
        keys = [key for key, _ in chain]
        raise KeyError('key {query} with hash {hash_k} not in {keys}'.format(query=query, hash_k=hash_k, keys=keys))


    def delete(self, key):
        hash_k = self.hash_func(key)
        chain = self.table[hash_k]
        for chain_idx in range(len(chain)):
            if key == chain[chain_idx][0]:
                val = chain.pop(chain_idx)[1]
                return val
        raise KeyError('key {key} not found at hash_bin with key {hash_k}'.format(key=key, hash_k=hash_k))

if __name__ == "__main__":
    dico = HashTable(3)
    key_vals = [(1923, 1822), (2328, 3), (12789, 2), (12, 2), (2, 5), (2, 6), (34, 8)]
    for key, val in key_vals:
        dico.set(key, val)
    val = dico.get(2)
    assert val == 6
    val = dico.get(2328)
    assert val == 3
    val = dico.delete(2328)
    print('Should raise KeyError next !')
    val = dico.get(2328)
