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

# Jun17 2022
class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:

        bt = boxTypes

        # sort boxes by values/units reversely
        bt.sort(key=lambda x : x[1], reverse=True)

        i = 0
        boxes = 0
        units = 0

        while boxes < truckSize and i < len(bt):
            if bt[i][0] + boxes <= truckSize:
                boxes += bt[i][0]
                units += bt[i][0]*bt[i][1]
                i += 1
            else:
                units += (truckSize - boxes) * bt[i][1]
                boxes = truckSize
                break

        return units

