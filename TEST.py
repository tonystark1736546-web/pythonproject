from pympler import asizeof


class NormalUser:
    def __init__(self, name, age):
        self.name = name
        self.age = age
for i in range(100000):
    a = NormalUser("k", 5)
print(asizeof.asizeof(a))
class NormalUser11:
    __slots__ = ['name', 'age']
    def __init__(self, name, age):
        self.name = name
        self.age = age
for i in range(100000):
    b = NormalUser11("k", 5)
print(asizeof.asizeof(b))