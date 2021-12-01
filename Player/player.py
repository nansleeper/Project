class Player:

    def __init__(self):
        self.x = 900
        self.y = 900
        self.car = False
        self.fire = False
        self.sector = (self.x // 300, self.y // 300)
        self.vx = 0
        self.vy = 0
    
    def move(self):
        self.x += self.vx
        self.y += self.vy
        self.sector = (self.x // 300, self.y // 300)
        