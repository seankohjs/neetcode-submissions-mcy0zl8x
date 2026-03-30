class CountSquares:

    def __init__(self):
        self.pointMap = defaultdict(int)

    def add(self, point: List[int]) -> None:
        self.pointMap[tuple(point)] += 1

    def count(self, point: List[int]) -> int:
        res = 0
        for k in self.pointMap.items():
            x1 = k[0][0]
            y1 = k[0][1]
            x2 = point[0]
            y2 = point[1]
            dx = x1 - x2
            dy = y1 - y2
            if abs(dx) != abs(dy):
                continue
            if dx == 0 or dy == 0:
                continue
            if (x1,y2) not in self.pointMap or (x2,y1) not in self.pointMap:
                continue
            res += self.pointMap[k[0]] * self.pointMap[(x1,y2)] * self.pointMap[(x2,y1)]
        return res