class MaximiseProfit:
    def __init__(self):
        # test items included (each item has a weight and value)
        weights = [3,1,3,4,2] 
        values = [2,2,4,5,3] 

        size = 7 # size of total weight value to be considered
        r = self.findMaxProfit(weights, values, size)
        print(f"Maximum value: {r[0]}")
        print(f"Items used and their values:")
        for i in r[1]:
            print(f"w: {weights[i]} v: {values[i]}")

    def findMaxProfit(self, w, v, s): #returns greatest value and the index of values used (uses 0/1 knapsack approach)
        m = [[0 for _ in range(s+1)] for _ in range(len(v)+1)]
        for r in range(1, len(m)): #iterates considering each item 
            value, weight = v[r-1], w[r-1] 
            for c in range(len(m[r])): #iterates considering each current size, building up
                if weight <= c and value + m[r-1][c-weight] >= m[r-1][c]:
                    m[r][c] = value+m[r-1][c-weight]
                else:
                    m[r][c] = m[r-1][c]

        #find which items were selected
        items = []
        curIndex = s
        for r in range(len(m)-1, 0, -1):
            if m[r-1][curIndex] != m[r][curIndex]:
                items.append(r-1)
                curIndex -= w[r-1]
        

        return (m[len(v)][s], items)


MaximiseProfit()
