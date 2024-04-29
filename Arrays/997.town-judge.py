class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        seen = set()
        count = 0
        arr = []
        if n==1:
            return n
        else:
            for inner_list in trust:
                a_i = inner_list[0]
                seen.add(a_i)
            
            for inner_list in trust:
                b_i = inner_list[1]
                if b_i not in seen:
                    arr.append(b_i)
                count = defaultdict(int)
                for num in arr:
                    count[num] += 1
                for x, freq in count.items():
                    if freq == n-1:
                        return b_i

            return -1