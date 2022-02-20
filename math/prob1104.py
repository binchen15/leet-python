class Solution:
    def pathInZigZagTree(self, label: int) -> List[int]:       
        
        def findRow(label):
            "find 1 based row of the labeled node"
            i = 1
            while 2 ** i - 1 < label:
                i += 1
            return i
        
        def findColumn(label):
            "return 1 based column of the labeled node"
            row = findRow(label)
            n = 2 ** (row-1) # length of the current row
            prev = n - 1
            if row % 2 == 1:
                col = label - prev
            else:
                col = n - (label - prev) + 1    
            return col
        
        def findParentColumn(column):
            return (column+1) // 2
        
        def findLabel(row, column):
            n = 2**(row-1)  # length of current row
            prev = n - 1
            if row % 2 == 1:
                label = prev + column
            else:
                label = prev + (n-column) + 1
            return label
                              
        def findParentLabel(label):
            row = findRow(label)
            col = findColumn(label)
            parent_col = findParentColumn(col)
            label = findLabel(row-1, parent_col)
            return label
        
        ans = [label]
        
        while label > 1:
            label = findParentLabel(label)
            ans.insert(0, label)
            
        return ans
