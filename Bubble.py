# 최적 : O(n^2)
# 최악 : O(n^2)
# 공간복잡도 : O(n)
# in_place sorting, Stable Sort

import Base


class Bubble(Base.Sort):

    def logic(self):
        for i in range(len(self.base)):
            for j in range(1, len(self.base)-i):
                if self.base[j-1] > self.base[j]:
                    self.swap(j-1, j)


bubble = Bubble([9, 1, 8, 2, 7, 3, 6, 4, 5])
bubble.sorting()
bubble.result()
