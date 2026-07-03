class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        store = {}
        for i in matrix:
            for j in i:
                store[j] = 1+store.get(j,0)
        if target in store:
            return True
        else:
            return False
            