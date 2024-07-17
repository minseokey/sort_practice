# 최적 : O(nlogn)
# 최악 : O(n^2)
# 공간복잡도 : avg O(logn), worst O(n) -> 추가공간이 아닌, 재귀로 인한 스택 공간 사용
# in_place sorting, UnStable Sort

import Base


class Quick(Base.Sort):
    def logic(self):

        def quick_sort(left, right):
            if left >= right:
                return

            pivot = self.base[left]
            ll, rr = left, right

            while ll < rr:
                while ll < rr and pivot < self.base[rr]:
                    rr -= 1

                while ll < rr and pivot >= self.base[ll]:
                    ll += 1

                if ll < rr:
                    self.swap(ll, rr)

            self.swap(left, rr)

            quick_sort(left, rr - 1)
            quick_sort(rr + 1, right)

        quick_sort(0, len(self.base)-1)


quick = Quick([9, 1, 8, 2, 7, 3, 6, 4, 5])
quick.sorting()
quick.result()
