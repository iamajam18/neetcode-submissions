class Solution:
    def isHappy(self, n: int) -> bool:
        store = {'0':0, '1':1, '2':4,'3':9, '4':16, '5':25, '6':36, '7':49, '8':64, '9':81}
        seen = set()
        while n!=1 and n not in seen:
            seen.add(n)
            m = str(n)
            total = 0
            for char in m:
                total += store[char]
            n = total
        return n==1