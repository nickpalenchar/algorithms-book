
class Comparable:
    
    def compareTo(self):
        pass

class Example:

    def sort(self) -> list:
        pass
    
    def less(self, v: Comparable, w: Comparable) -> bool:
        return v.compareTo(w) < 0

    def exch(self, a: list, i: int, j: int) -> None:
        a[i], a[j] = a[j], a[i]


