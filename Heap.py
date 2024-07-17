# 최적 : O(nlogn)
# 최악 : O(nlogn)
# 공간복잡도 : O(logn + n) -> 추가공간 n, 재귀로 인한 스택 공간 nlogn 사용
# not in_place sorting, Stable Sort

import Base


class Heap(Base.Sort):
    def logic(self):
        n = len(self.base)

        def heapify(length, root):
            # root -> 부분 트리의 루트... 여기서는 최대가 되어야 한다.
            # length -> 부분 트리의 길이
            largest = root

            # 왼쪽자식, 오른쪽 자식의 인덱스
            left = (2 * root) + 1
            right = (2 * root) + 2

            # 만약 왼쪽자식이 헤드보다 크다면 교체
            if left < length and self.base[left] > self.base[largest]:
                largest = left

            # 만약 오른쪽 자식이 헤드보다 커도 교체
            if right < length and self.base[right] > self.base[largest]:
                largest = right

            # 만약 교체가 일어났다면? ->  실제 배열도 교체
            if largest != root:
                self.base[root], self.base[largest] = self.base[largest], self.base[root]
                # 교환후 힙 속성 유지를 위해 heapify
                heapify(length, largest)

        def heap_sort():
            # 초기 heapq 설정
            # n//2-1 부터 -- 를 하는 이유는 리프는 heapify 를 할 이유가 없기 때문.
            for i in range(n//2-1, -1, -1):
                heapify(n, i)

            #
            for i in range(n-1, 0, -1):
                self.base[i], self.base[0] = self.base[0], self.base[i]
                heapify(i, 0)

        heap_sort()


heap = Heap([9, 1, 8, 2, 7, 3, 6, 4, 5])
heap.sorting()
heap.result()