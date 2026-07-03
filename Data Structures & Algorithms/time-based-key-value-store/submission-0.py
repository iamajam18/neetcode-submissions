class TimeMap:

    def __init__(self):
        self.keyStore = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.keyStore:
            self.keyStore[key] = []
        self.keyStore[key].append([value,timestamp])

    def get(self, key: str, timestamp: int) -> str:
        res,values = '',self.keyStore.get(key,[])
        left,right = 0,len(values) -1
        while left<=right:
            k =(left+right)//2
            if values[k][1] <= timestamp:
                res = values[k][0]
                left = k+1
            else:
                right = k-1
        return res
