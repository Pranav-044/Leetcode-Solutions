class Solution:
    def gardenNoAdj(self, n: int, paths: List[List[int]]) -> List[int]:
        matrix=[[] for _ in range(n+1)]
        for i,j in paths:
            matrix[i].append(j)
            matrix[j].append(i)
        node=1
        colors=[-1]*(n+1)
        def isPossible(node,color):
            for i in matrix[node]:
                if colors[i] == color:
                    return False
            return True
        def final(node):
            if(node == n+1):
                return True
            for color in range(1,5):
                if(isPossible(node,color)):
                    colors[node] = color
                    if(final(node+1)):
                        return True
                    colors[node]=-1
            return False
        final(node)
        return colors[1:]
