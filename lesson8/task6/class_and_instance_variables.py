class Dog:

    kind = 'canine'         # class variable

    def __init__(self, name):
        self.name = name    # instance variable unique to each instance

d = Dog('Fido')
e = Dog('Buddy')

print(d.kind)
print(e.kind)

print(d.name)
print(e.name)


class Dog2:

    tricks = []
    def __init__(self, name):
        self.name = name

    def add_trick(self, trick):
        self.tricks.append(trick)

d2 = Dog2('Fido')
e2 = Dog2('Buddy')
d2.add_trick('roll over')
e2.add_trick('play dead')

print(d2.tricks)