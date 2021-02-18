class Heap(object):
    def __init__(self, value_getter, key_getter):
        self.collection = []
        self._value_getter = value_getter
        self._key_getter = key_getter
        self._pos = {}

    def insert(self, node):
        curr_idx = len(self.collection)
        key = self._key_getter(node) if self._key_getter else curr_idx
        self.collection.append(node)
        self._pos[key] = curr_idx
        last = len(self.collection) - 1
        self._bubble_up(last)

    def is_empty(self):
        return len(self.collection) == 0

    def _pop_last(self):
        last = self.collection.pop()
        del self._pos[self._key_getter(last)]
        return last

    def bubble_up_from_key(self, key):
        idx = self._pos[key]
        self._bubble_up(idx)

    def dequeue_min(self):
        if self.is_empty():
            return None
        smallest = self.collection[0]
        last = self._pop_last()
        if self.is_empty():
            return last
        self.collection[0] = last
        self._pos[self._key_getter(last)] = 0
        self._sift_down(0)
        return smallest

    def _bubble_up(self, node):
        parent = self._parent(node)
        while parent is not None:
            if self._get_val(node) < self._get_val(parent):
                self._swap(node, parent)
                node = parent
                parent = self._parent(node)
            else:
                return

    def _sift_down(self, node):
        node_val = self._get_val(node)
        left = self._left_child(node)
        if not left:
            return
        left_val = self._get_val(left)
        right = self._right_child(node)
        right_val = self._get_val(right)
        if right_val is None:
            min_idx = left
        else:
            min_idx = left if left_val < right_val else right
        min_val = self._get_val(min_idx)
        if min_val > node_val:
            return
        self._swap(node, min_idx)
        self._sift_down(min_idx)

    def _swap(self, a, b):
        node_a, node_b = self.collection[a], self.collection[b]
        self._pos[self._key_getter(node_a)], self._pos[self._key_getter(node_b)] = b, a
        self.collection[a], self.collection[b] = self.collection[b], self.collection[a]

    def _get_val(self, idx):
        if idx is None:
            return None
        return self._value_getter(self.collection[idx])

    def _parent(self, i):
        idx = (i - 1) // 2
        if idx > -1:
            return idx
        return None

    def _child(self, i, offset):
        idx = 2 * i + offset
        if idx < len(self.collection):
            return idx
        return None

    def _left_child(self, i):
        return self._child(i, 1)

    def _right_child(self, i):
        return self._child(i, 2)

    def _log(self):
        print("collection", self.collection)


def nshortestpaths(G, a, b):
    dist = [float('inf') for _ in G]
    prev = [() for _ in G]
    dist[a] = 0

    nodes = [{"index": i} for (i, _) in enumerate(G)]
    H = Heap(lambda x: dist[x["index"]], lambda x: x["index"])
    for node in nodes:
        H.insert(node)

    while not H.is_empty():
        u = H.dequeue_min()["index"]
        for (v, l) in G[u]:
            test_dist = dist[u] + l
            if test_dist < dist[v]:
                dist[v] = test_dist
                prev[v] = (u,)
                H.bubble_up_from_key(v)
            elif test_dist == dist[v]:
                prev[v] += (u,)

    def numPaths(node):
        if node == a:
            return 1
        num_paths = 0
        for p in prev[node]:
            num_paths += numPaths(p)
        return num_paths

    return numPaths(b)
