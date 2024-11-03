class Monster:

    def __init__(self, health, energy):
        
        self.health = health
        self.energy = energy

    def attack(self, amount):

        print("The monster has attacked!")
        print(f"{amount} damage was dealt")
        self.energy -= 20

    def move(self, speed):

        print("The monster has moved")
        print(f"It has a speed of {speed}")
        

class Shark(Monster):

    def __init__(self, health, energy, speed):
        
        super().__init__(health, energy)
        self.speed = speed
    
    def bite(self):
        
        print("The shark has bitten")
    
    def move(self):
        
        print("The shark has moved")
        print(f"The speed of the shark is {self.speed}")

class Scorpion(Monster):

    def __init__(self, health, energy, poison_damage):
        super().__init__(health, energy)
        self.poison_damage = poison_damage
    
    def attack(self):
        print("The scorpion has attacked")
        print(f"It has dealt {self.poison_damage} poison damage")
    


shark = Shark(speed = 120, health = 100, energy = 80)
print(shark.speed)
print(shark.health)
print(shark.energy)

scorpion = Scorpion(poison_damage = 50, health = 100, energy = 80)
scorpion.attack()
scorpion.move(5)
print(scorpion.health)