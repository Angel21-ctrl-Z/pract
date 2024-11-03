class hero:

    def __init__(self, damage, monster):

        self.damage = damage
        self.monster = monster
    
    def attack(self):
         
        self.monster.take_damage(self.damage)

class Monster:

    def __init__(self, health, energy):
        
        self.health = health
        self.energy = energy
    
    def update_energy(self, amount):

        self.energy += amount
    
    def take_damage(self, amount):
        
        self.health -= amount

monster = Monster(health = 100, energy = 50)

Hero = hero(damage = 15, monster = monster)


print(monster.health)

Hero.attack()

print(monster.health)