class Shark:

    def __init__(self, name, health, power, aps):

        self.name = name

        self.health = health
        self.power = power
        self.aps = aps
        self.dps = self.power * self.aps

    def fight(self, other):

        if self.dps > other.dps:
            print(f"{self.name} is the wiiinnner")
        if self.dps < other.dps:
            print(f"{other.name} is the wiiinnner")
        if self.dps == other.dps:
            print("both are loooossserr")
    
shark_1 = Shark("bruce", 150, 25, 1)
shark_2 = Shark("luke", 100, 50, 2)

shark_2.fight(shark_1)