class LRUCache:
    # @param capacity, an integer
    def __init__(self, capacity):
        self.cache = {}
        self.cap = capacity
        self.len = 0
        self.lru = []

    # @return an integer
    def get(self, key):
        val = self.cache.get(key, -1)
        if val > 0:
            self.lru.remove(key)
            self.lru.append(key)
        return val
        
    # @param key, an integer
    # @param value, an integer
    # @return nothing
    def set(self, key, value):
        if key in self.cache:
            self.cache[key] = value
            self.lru.remove(key)
            self.lru.append(key)
        else:
            if self.len >= self.cap:
                dkey = self.lru[0]
                del self.cache[dkey]
                del self.lru[0]
            else:
                self.len += 1
            self.lru.append(key)
            self.cache[key] = value
            
def test():
    cache = LRUCache(2)
    print cache.get(1)
    cache.set(1, 2)
    print cache.cache, cache.len, cache.lru
    cache.set(2, 3)
    print cache.cache, cache.len, cache.lru
    cache.set(1, 4)
    print cache.cache, cache.len, cache.lru
    cache.set(3, 5)
    print cache.cache, cache.len, cache.lru
    print cache.get(2)
    print cache.get(1)
    print cache.cache, cache.len, cache.lru
    
