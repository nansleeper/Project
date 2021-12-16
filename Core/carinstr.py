"""
class Car():
    def __init__(globalcent, textur, angle):
        self.globalcent = globalcent - глобальные координаты (x, y)
        self.cent = globalcent - player.coards - локальные координаты (изначально 0, потом в move пересчитать)
        self.v = 1 - скорость
        self.angle = angle - угол в градусах по часовой стрелке
        self.stop - видит ли перед собой преграду в виде другой машины
        self.hit - столкнулась ли машина
        self.playerstatus - True если playerr управляет ею 
        self.unable - True - если машина брошена
        self.sector - сектор в глобальных координатах
        self.tex = textur
        self.t_unable - время, которое машина брошена
        self.rotate


    def collisions(obj):
        проверяет столкнулась ли машина с obj(другая машина), домами(напиши мне, обсудим) (объект с центром в obj.cent и шириной obj.hitbox)
            *******
        self.hit = True

    def stop(obj):
        проверяет есть ли машина перед ней на определенном расстоянии interval 
        если есть - self.stop = True
        self.t_unbale += 1

    def move((x, y, alpha), dv = (0 w, 0 a, 0 s, 0 d)) - положение стремления
        if not (self.playerstatus or self.stop):
            к этому положения устремить машину
        elif self.unable:
            self.t_unable += 1
        else:
            человек управляет машиной с помощью dv



    
        


    

        

    def draw
        отрисовка машины







"""