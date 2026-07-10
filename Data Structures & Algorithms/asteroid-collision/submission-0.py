class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for asteroid in asteroids:
            destroyed = False
            while stack and asteroid <0 and stack[-1]>0:
                diff = asteroid + stack[-1]
                if diff <0:
                    stack.pop()
                elif diff>0:
                    destroyed = True
                    break
                else:
                    destroyed = True
                    stack.pop()
                    break
            if not destroyed:
                stack.append(asteroid)
        return stack