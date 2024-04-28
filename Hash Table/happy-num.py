class Solution:
    def isHappy(self, n: int) -> bool:
        if n==1:
            return True

        seen = set()
        add = 0
        while n not in seen:
            seen.add(n)
            sep = [int(d) for d in str(n)]
            for i in range(len(sep)):
                add = add + (sep[i]**2)
                i = i+1
            if add == 1:
                return True
                break
            else:
                n = add
                add = 0
        return False