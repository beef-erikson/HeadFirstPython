class CountFromBy:
    # initialize
    def __init__(self, v: int=0, i: int=1) -> None:
        self.val = v
        self.inc = i

    # representation
    def __repr__(self) -> str:
        return str(self.val)

    # increases val by inc
    def increase(self) -> None:
        self.val += self.inc


# Examples
h = CountFromBy(100, 10)
print(h.val, h.inc)
h.increase()
print(h.val)
print(h)
print()

i = CountFromBy()
print(i)
i.increase()
print(i)
print()

j = CountFromBy(100, 10)
print(type(j))
print(id(j))
print(hex(id(j)))
