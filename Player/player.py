class Player:

    def __init__(self):
        self.x = 1800
        self.y = 1800
        self.car = False
        self.fire = False
        self.sector = (self.x // 300, self.y // 300)
        self.vx = 0
        self.vy = 0
    
    def move(self):
        if ((self.x + self.vx) // 300 >= 3) and ((self.y + self.vy) // 300 >= 2) \
            and ((self.x + self.vx) // 300 <= 44) and ((self.y + self.vy) // 300 <= 29):
            self.x += self.vx
            self.y += self.vy
        self.sector = (self.x // 300, self.y // 300)
        