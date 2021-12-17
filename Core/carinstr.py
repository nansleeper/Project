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
        self.sector - сектор в глобальных координатах (x, y)
        self.tex = textur
        self.t_unable - время, которое машина брошена
        self.rotate = False поворачивает ли машина
        self.traectory = [x, y, alpha] точка стремления в глобальных координатах


    def collisions(obj):
        проверяет столкнулась ли машина с obj(другая машина), домами(напиши мне, обсудим) (объект с центром в obj.cent и шириной obj.hitbox)
            *******
        self.hit = True

    def stop(obj, MAP_SECTOR):
        проверяет есть ли машина перед ней на определенном расстоянии interval 
        если есть - self.stop = True
        self.t_unbale += 1
        if MAP_Sector = "cross":  если на перекрестке стоп если не его очередь ехать
            if abs(MAP_Sector.angle - self.angle) > 45 and self.rotate == False:
                self.stop = True

    def move(dv = (0 w, 0 a, 0 s, 0 d)) 
        if not (self.playerstatus or self.stop):
            траектори - к этому положения устремить машину
        elif self.unable:
            self.t_unable += 1
        else:
            человек управляет машиной с помощью dv (второстепенная задача)



    
        


    

        

    def draw
        отрисовка машины







"""