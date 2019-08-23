class MinHeap:
    def __init__(self):
        self.arr = []

    def insert(self, val):
        self.arr.append(val)
        self.bubble_up(len(self.arr) - 1)

    def bubble_up(self, idx):
        # Stop if reached root
        if not idx == 0:
            parent_idx = (idx - 1) // 2
            # Only continue if current is smaller then parent
            if self.arr[idx] < self.arr[parent_idx]:
                # Swap !
                self.arr[idx], self.arr[parent_idx] = self.arr[parent_idx], self.arr[idx]
                self.bubble_up(parent_idx)

    def get_min(self):
        min_val = self.arr[0]
        # Rebalance by getting last element and putting it to right position
        last_val = self.arr.pop()
        if len(self.arr):
            self.arr[0] = last_val
            self.bubble_down(0)
        return min_val

    def bubble_down(self, idx):
        i_l = 2 * idx + 1
        i_r = 2 * idx + 2
        if i_l > len(self.arr) - 1:
            # Left child outside of array --> current is leaf
            return
        elif i_l == len(self.arr) - 1:
            # Only left child (right child position would be at i_l + 1
            # which is out of array
            if self.arr[i_l] < self.arr[idx]:
                # If needed (leaf is smaller then current), swap
                self.arr[i_l], self.arr[idx] = self.arr[idx], self.arr[i_l]
        else:
            # Both children exist, the only way to respect the heap is to insure
            # that the smallest of the 3 is at the top
            if self.arr[i_l] < self.arr[idx] or self.arr[i_r] < self.arr[idx]:
                # current is not smallest of the two children --> swap needed
                # given that we know that smallest is not at idx
                # it is enough to check which of the children is the smallest
                # to get the smallest of the current and two children
                if self.arr[i_l] < self.arr[i_r]:
                    self.arr[i_l], self.arr[idx] = self.arr[idx], self.arr[i_l]
                    # Current went down, but might have broken the min rule
                    # one level down --> need to check if rule verified at new position
                    self.bubble_down(i_l)
                else:
                    self.arr[i_r], self.arr[idx] = self.arr[idx], self.arr[i_r]
                    self.bubble_down(i_r)

if __name__ == "__main__":
    heap = MinHeap()
    vals = [2, 3, 5, 12, 24, 5, 7]
    for val in vals:
        heap.insert(val)
    print(heap.arr)
    for idx in range(len(vals)):
        min_v = heap.get_min()
        print(vals, min_v, heap.arr)

