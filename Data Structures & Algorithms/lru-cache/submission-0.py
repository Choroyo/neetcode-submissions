class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
    
    def get(self, key: int) -> int:
        if key in self.cache:
            return self.cache[key]
        else:
            return -1
        

    def put(self, key: int, value: int) -> None:
        if len(self.cache) < self.capacity:
            self.cache[key] = value
        else:
            oldKey = min(self.cache.keys())
            self.cache[key] = self.cache.pop(oldKey)                
            self.cache[key] = value
