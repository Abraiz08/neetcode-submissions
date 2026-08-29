import heapq
import math
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distances = []
        for point in points:
            distance = math.sqrt(((point[0]**2)-(0**2))+((point[1]**2)-(0**2)))
            distances.append([-distance, point])
            
        
        heapq.heapify(distances)
        while len(distances) > k:
            heapq.heappop(distances)
        return [distance[1] for distance in distances]