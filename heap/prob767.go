import "container/heap"

type CharCount struct {
    char byte
    count int
}
    
type MaxHeap []CharCount
    
func (h MaxHeap) Len() int {
    return len(h)
}
    
func (h MaxHeap) Less(i, j int) bool {
    return h[i].count > h[j].count
}
    
func (h MaxHeap) Swap(i, j int) {
    h[i], h[j] = h[j], h[i]
}
    
func (h *MaxHeap) Push(x interface{}) {
    *h = append(*h, x.(CharCount))
}
    
func (h *MaxHeap) Pop() interface{} {
    old := *h
    n := len(old)
    ans := old[n-1]
    *h = old[:n-1]
    return ans
}


func reorganizeString(s string) string {
    
    n := len(s)
    if n == 1 {
        return s
    }
    
    cnts := map[byte]int{}
    
    for i := 0; i < n; i++ {
        c := s[i]
        cnt, ok := cnts[c]
        if ! ok {
            cnts[c] = 1
        } else {
            cnts[c] = cnt + 1
        }
    }
    
    h := make(MaxHeap, len(cnts))
    i := 0
    for key, val := range cnts {
        h[i] = CharCount{
            char:key,
            count:val,
        }
        i++
    }

    heap.Init(&h)
    
    ans := ""
    
    for len(h) > 0 {
        if len(h) >= 2 {
            item1 := heap.Pop(&h)
            item2 := heap.Pop(&h)
            c1 := item1.(CharCount).char
            c2 := item2.(CharCount).char
            ans = ans + string(c1) + string(c2)
            cnts[c1] -= 1
            cnts[c2] -= 1
            if cnts[c1] > 0 {
                heap.Push(&h, CharCount{
                    char: c1,
                    count: cnts[c1],
                })
            }
            if cnts[c2] > 0 {
                heap.Push(&h, CharCount{
                    char: c2,
                    count: cnts[c2],
                })
            } 
        } else {
            item := heap.Pop(&h)
            if item.(CharCount).count > 1 {
                return ""
            } else {
                return ans + string(item.(CharCount).char)
            }
        }
    }
    
    
    return ans
    
}

