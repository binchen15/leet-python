import "sort"

func maximumUnits(boxTypes [][]int, truckSize int) int {
    
    ans := 0
    n := len(boxTypes)
    
    sort.Slice(boxTypes, func(i, j int) bool {
        return boxTypes[i][1] > boxTypes[j][1]
    })
    
    i := 0
    nboxes := 0
    for nboxes < truckSize && i < n {
        box := boxTypes[i]
        if box[0] > 0 {
            if box[0] <= truckSize - nboxes {
                nboxes += box[0]
                ans += box[0]*box[1]
                box[0] = 0
                i += 1
            } else {
                delta := truckSize - nboxes
                ans += box[1] * delta
                break
            }
        } else {
            i += 1
        }
    }
    
    
    return ans
    
    
}
