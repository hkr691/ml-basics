import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        max_heap = []
        for point in points:
            if len(max_heap) < k:
                heapq.heappush(max_heap, (-self.Equilidean_distance(point), point))
            else:
                heapq.heappushpop(max_heap, (-self.Equilidean_distance(point), point))
        return [point for _,point in max_heap]

    
    def Equilidean_distance(self, point: List[int]):
        dist = point[0] ** 2 + point[1] ** 2
        return dist
