
class LRU:
    
    def __init__(self, maxcap):
        self.max_cap = maxcap
        self.curr_cap = 0
        self.dict = {}
        
    def max_capacity(self):
        return self.max_cap
    
    def size(self):
        return len(self.dict)
    
    def get(self, key):
        if key in self.dict:
            return self.dict[key]
        return -1
    
    def put(self, key, value = 0):
        if value < 0:
            return print("Error: value less than zero")
        if key in self.dict:
            self.dict[key] = value
        if self.curr_cap != self.max_cap:
            self.dict[key] = value
            self.curr_cap += 1
        else:
            sortlist = sorted(self.dict.items(), key=lambda x: x[1])#
            sortlist[0] = (key, value)
            self.dict = dict(sortlist)
 
class maxheap():
    
    def __init__(self, dictlist):
        self.tree = []
        self.dict = dictlist
        
    def is_empty(self):
        return len(self.tree) == 0

    def parent(self, i):
        if i == 0:
            return
        return self.tree[(i - 1) // 2]

    def left_child(self, i):
        c = 2 * i + 1
        if c >= len(self.tree):
            return
        return self.tree[c]

    def right_child(self, i):
        c = 2 * i + 2
        if c >= len(self.tree):
            return
        return self.tree[c]

    def insert(self, item):
        self.tree.append(item)
        self._percolate_up(len(self.tree) - 1)

    def _percolate_up(self, i):
        if i == 0:
            return

        parent_index = (i - 1) // 2

        if self.dict[self.tree[parent_index]] < self.dict[self.tree[i]]:
            self.tree[i], self.tree[parent_index] = self.tree[parent_index], self.tree[i]
            self._percolate_up(parent_index)

    def extract_max(self):
        if len(self.tree) < 1:
            return None
        if len(self.tree) == 1:
            return self.tree.pop()

        root = self.tree[0]
        self.tree[0] = self.tree.pop()

        self._percolate_down(0)

        return root

    def _percolate_down(self, i):
        if self.right_child(i) is None or self.left_child(i) is None:
            return
            
        if self.dict[self.tree[i]] >= max(self.dict[self.left_child(i)], self.dict[self.right_child(i)]):
            return

        max_child_index = 2 * i + 1 if self.dict[self.left_child(i)] > self.dict[self.right_child(i)] else 2 * i + 2

        self.tree[i], self.tree[max_child_index] = self.tree[max_child_index], self.tree[i]
        self._percolate_down(max_child_index)
            
class MFE:
    
    def __init__(self, word_list):
        self.dict = {}
        self.insert_list(word_list)
        
        
    def insert_list(self, word_list):
        for word in word_list:
            word = word.lower().rstrip()
            if word in self.dict:
                self.dict[word] += 1
            else:
                self.dict[word] = 1
                
    def get_most_freq_elem(self):
        heap = maxheap(self.dict)
        for word in self.dict:
            heap.insert(word)
        while not heap.is_empty() or heap is None:
            i = heap.extract_max()
            print(i, " : ", self.dict[i])
    
def main():
    lru=LRU(3)
    lru.put('yellow', 3)
    lru.put('black', 2)
    lru.put('red', 0)
    print(lru.dict)
    
    word_file = open("sample.txt", "r")
    mfe=MFE(word_file)
    mfe.get_most_freq_elem()    
    
    
    
main()
