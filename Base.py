import TimeCounter


class Sort:
    def __init__(self, base):
        self.base = base
        self.swap_counter = 0
        self.timer = TimeCounter.Timer()

    def swap(self, i, j):
        self.base[i], self.base[j] = self.base[j], self.base[i]
        self.swap_counter += 1

    def logic(self):
        pass

    def sorting(self):
        self.timer.start()

        # 소팅 로직
        self.logic()

        self.timer.end()
        self.timer.print()

    def result(self):
        print("result : ", end="")
        print(self.base)
        print("swap : " + str(self.swap_counter))
