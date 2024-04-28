class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        seen = set()
        for inner_list in paths:
            cityA = inner_list[0]
            seen.add(cityA)
        for inner_list in paths:
            cityB = inner_list[1]
            if cityB not in seen:
                return cityB