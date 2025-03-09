class MinPQ():
    def __init__(self) -> None:
        self.heap = [None]
        self.key_index = {}
    
    def __len__(self):
        return len(self.heap) - 1
    
    def _swap(self, i, j):
        self.key_index[self.heap[i]], self.key_index[self.heap[j]] = j, i
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]
    
    def minimum(self):
        if len(self) < 1:
            raise RuntimeError("heap underflow")
        return self.heap[1]

    def insert(self, key):
        self.heap.append(key)
        self.key_index[key] = len(self)
        self._decrease_key(len(self))
        # self.check_ri()
    
    def decrease_key(self, key):
        # self.check_ri()
        index = self.key_index.get(key)
        # index = self.key_index[key]
        if index is not None:
            self._decrease_key(index)
        # self.check_ri()

    def _decrease_key(self, i):
        while i > 1:
            p = i // 2
            if self.heap[p] < self.heap[i]:
                break
            self._swap(p, i)
            i = p
    
    def extract_min(self):
        if len(self) < 1:
            raise RuntimeError("heap underflow")
        self._swap(1, len(self))
        min_key = self.heap.pop()
        del self.key_index[min_key]
        self._sink(1)
        # self.check_ri()s
        return min_key
    
    def _sink(self, i):
        while True:
            smallest = i
            l = i * 2
            r = l + 1
            if l < len(self.heap) and self.heap[l] < self.heap[smallest]:
                smallest = l
            if r < len(self.heap) and self.heap[r] < self.heap[smallest]:
                smallest = r
            if smallest == i:
                break
            self._swap(i, smallest)
            i = smallest
    

    def check_ri(self):
        heap = self.heap
        i = 1
        while i <= (len(heap) - 1) // 2:
            l = i * 2
            if heap[i] > heap[l]:
                raise ValueError('Left child is smaller than parent.')
            r = i * 2 + 1
            if r < len(heap) and heap[i] > heap[r]:
                raise ValueError('Right child is smaller than parent.')
            i += 1
            
        for key, index in self.key_index.items():
            if self.heap[index] is not key:
                raise ValueError('Key index mapping is wrong.')

pq = MinPQ()


