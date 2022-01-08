type ListNode struct {
    key int
    value int
    prev *ListNode
    next *ListNode
}

type LRUCache struct {
    capacity int
    hmap  map[int]*ListNode
    head *ListNode
    tail *ListNode
}


func Constructor(capacity int) LRUCache {
    cache := LRUCache{
        capacity:capacity,
        hmap: map[int]*ListNode{},
        head: &ListNode{},
        tail: &ListNode{},
    }
    cache.head.next = cache.tail
    cache.tail.prev = cache.head
    return cache
}

func (this *LRUCache) MoveItem(key int) {
    // move key to the end
    node, ok := this.hmap[key]
    if ok {
        node.prev.next = node.next
        node.next.prev = node.prev
        tail := this.tail
        tmp := tail.prev
        tmp.next = node
        node.next = tail
        node.prev = tmp
        tail.prev = node
    }
}

func (this *LRUCache) PopItem() {
    // remove the first element
    head := this.head
    node := head.next
    if node != this.tail {
        head.next = node.next
        node.next.prev = head
    }
    delete(this.hmap, node.key)
}


func (this *LRUCache) Get(key int) int {
    node, ok := this.hmap[key]
    if !ok {
        return -1
    } else {
        val := node.value
        key := node.key
        this.MoveItem(key)
        return val
    }
    
}


func (this *LRUCache) Put(key int, value int)  {
    node, ok := this.hmap[key]
    if ok {
        node.value = value
        this.MoveItem(key)
    } else {
        node = &ListNode{
            key:key,
            value:value,
        }
        tmp := this.tail.prev
        tmp.next = node
        node.next = this.tail
        node.prev = tmp
        this.tail.prev = node
        this.hmap[key] = node
        if len(this.hmap) > this.capacity {
            this.PopItem()
        }
    }
}


/**
 * Your LRUCache object will be instantiated and called as such:
 * obj := Constructor(capacity);
 * param_1 := obj.Get(key);
 * obj.Put(key,value);
 */

