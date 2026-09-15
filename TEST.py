from pympler import asizeof


class NormalUser:
    def __init__(self, name, age):
        self.name = name
        self.age = age
for i in range(100000):
    a = NormalUser("k", 5)
print(asizeof.asizeof(a))