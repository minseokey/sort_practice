# 최적 : O(nlogn)
# 최악 : O(nlogn)
# 공간복잡도 : O(logn + n) -> 추가공간 n, 재귀로 인한 스택 공간 nlogn 사용
# not in_place sorting, Stable Sort

import Base


class Merge(Base.Sort):

    def logic(self):
        def merge_sort(start, end):
            if end - start < 2:
                return
            mid = (start + end) // 2

            # divide
            merge_sort(start, mid)
            merge_sort(mid, end)

            # conquer
            merge(start, mid, end)

        def merge(start, mid, end):
            new_base = []
            lo, hi = start, mid

            # 경쟁 처리
            while lo < mid and hi < end:
                if self.base[lo] < self.base[hi]:
                    new_base.append(self.base[lo])
                    lo += 1
                else:
                    new_base.append(self.base[hi])
                    hi += 1

            # 남은거 처리
            while lo < mid:
                new_base.append(self.base[lo])
                lo += 1

            while hi < end:
                new_base.append(self.base[hi])
                hi += 1

            # 갈아끼우기
            for i in range(start, end):
                self.base[i] = new_base[i - start]

        return merge_sort(0, len(self.base))


merge = Merge([9, 1, 8, 2, 7, 3, 6, 4, 5])
merge.sorting()
merge.result()
