class Weight(object):
    def __init__(self, weight):
        self.weight = weight

    def __add__(self, other):
        if type(other) == int:
            return Weight(
                self.weight + other)

        return Weight(
            self.weight + other.weight)

    def __str__(self):
        return 'Weight(%s)' % self.weight


w1 = Weight(20)
w2 = Weight(60)

w3 = 50 + w1

print(w3)