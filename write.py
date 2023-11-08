class DLinkedNode:
    def __init__(self, key=0, value=0):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.size = 0
        self.cache = {}
        self.head = DLinkedNode()
        self.tail = DLinkedNode()
        self.head.next = self.tail
        self.tail.prev = self.head
    
    def get(self, key):
        if key not in self.cache:
            return -1
        node = self.cache[key]
        self.MoveToHead(node)
        return node.value
    
    def MoveToHead(self, node):
        self.RemoveNode(node)
        self.AddToHead(node)
    
    def RemoveNode(self, node):
        nxt = node.next
        pre = node.prev
        pre.next = nxt
        nxt.prev = pre
    
    def AddToHead(self, node):
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node
        
    def put(self, key, value):
        if key in self.cache:
            node = self.cache[key]
            self.MoveToHead(node)
            node.value = value
        else:
            node = DLinkedNode(key, value)
            self.cache[key] = node
            self.size += 1
            self.AddToHead(node)
            if self.size > self.capacity:
                node = self.RemoveTail()
                self.cache.pop(node.key)
                self.size -= 1
    
    def RemoveTail(self):
        node = self.tail.prev
        self.RemoveNode(node)
        return node
                
                
            
            
        