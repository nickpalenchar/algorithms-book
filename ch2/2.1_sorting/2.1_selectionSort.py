from example import Example

class Selection(Example):

    @classmethod
    def sort(cls, a: list) -> None:
        for i in range(len(a)):
            # because the example mutates a as we go along, we cannot use enumerate,
            # which would return a copy of the list and never update with our mid-iteration
            # exchanges.
            _min = i
            for j in range(i, len(a)):
                if cls.less(a[j], a[_min]):
                    _min = j
            cls.exch(a, i, _min)

a = [4, 8, 2, 9, 0, 10, 8]
b = [2, 4, 9]
c = [1, 1, 1, 1, 1]
e = [10, 9]

for l in [a, b, c, e]:
    Selection.sort(l)
    print(l)

