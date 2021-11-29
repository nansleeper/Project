class Player:

    def __init__(self):
        self.x = 0
        self.y = 0
        self.car = False
        self.fire = False
        self.sector = (self.x // 300 + 1, self.y // 300 + 1)
        