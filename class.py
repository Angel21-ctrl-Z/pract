class wall:
    def __init__(self, depth, height, width):
        self.depth = depth
        self.height = height
        self.width = width
        self.volume = depth * height * width

wall = wall(100, 30, 10)

print(wall.__dict__)

class monster:

    def __init__(self, func):
        self.func = func

class attack:

    def bite():
        print ("ouch")
    
    def strike():
        print("bonk")

    def slash():
        print("BLLOODD!!!")

    def kick():
        print("not there!!!")

class donkey(monster):

    def __init__(self, func, health, energy):
        super().__init__(func)
        self.health = health
        self.energy = energy
    
    def update_energy(self, amount):
        self.energy += amount
    
    def __str__(self):
        return super().__str__()
    

Donkey = donkey(func = attack.kick, health = 30, energy = 10)
Donkey.func()
print(Donkey.__dict__)
print(Donkey)


