# 최적 : O(n^2)
# 최악 : O(n^2)
# 공간복잡도 : O(n)
# in_place sorting, UnStable Sort

import Base


class Selection(Base.Sort):

    def logic(self):
        for i in range(len(self.base)):
            now = i
            for j in range(i + 1, len(self.base)):
                if self.base[j] < self.base[now]:
                    now = j

            if now != i:
                self.swap(i, now)


select = Selection([9, 1, 8, 2, 7, 3, 6, 4, 5])
select.sorting()
select.result()
