package amazon;

import java.util.LinkedHashMap;
import java.util.Map;

class LRUCache {
    private final Map<Integer, Integer> cache;
    private final int capacity;

    public LRUCache(int capacity) {
        this.cache = new LinkedHashMap<>(capacity);
        this.capacity = capacity;
    }

    public int get(int key) {
        if (cache.get(key) == null) return -1;
        Integer value = cache.get(key);
        cache.put(key, value);
        return value;
    }

    public void put(int key, int value) {
        if (cache.size() >= capacity) {
        }
    }
}

/**
 * Your LRUCache object will be instantiated and called as such:
 * LRUCache obj = new LRUCache(capacity);
 * int param_1 = obj.get(key);
 * obj.put(key,value);
 */