"""	Write an iterator class reverse_iter, that takes a list and iterates it from the reverse direction	"""


class reverse_iter:
    def __init__(self, n):
        self.i = len(n)
        self.n = n

    def __iter__(self):
        return self

    def next(self):
        if self.i > 0:
            i = self.n[self.i - 1]
            self.i -= 1
            return i
        else:
            raise StopIteration()


it = reverse_iter([1, 2, 3, 4])

print it.next()
print it.next()
print it.next()
print it.next()
print it.next()
