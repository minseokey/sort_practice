# 최적 : O(n)
# 최악 : O(n^2)
# 공간복잡도 : O(n)
# in_place sorting, Stable Sort

import Base


class Insertion(Base.Sort):

    def logic(self):
        for i in range(1, len(self.base)):
            now = i
            while now > 0 and self.base[now - 1] > self.base[now]:
                self.swap(now, now - 1)
                now -= 1


insertion = Insertion([9, 1, 8, 2, 7, 3, 6, 4, 5])
insertion.sorting()
insertion.result()
