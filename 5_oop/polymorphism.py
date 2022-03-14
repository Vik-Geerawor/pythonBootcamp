class Animal:
    def __init__(self, name):
        self.name = name

    def feed(self):
        print(f"{self.name} is feeding")

    def move(self):
        print(f"{self.name} is moving")


class Bird(Animal):
    def __init__(self, name):
        Animal.__init__(self, name)

    # overriding the move method from super class
    def move(self):
        print(f"{self.name} is flying")


if __name__ == '__main__':
    pigeon = Bird('pigeon')
    alien = Animal('predator')

    # move method behaves differently in each case
    pigeon.move()
    alien.move()

