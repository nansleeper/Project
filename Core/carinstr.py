"""
class Car():
    def __init__(globalcent, textur):
        self.globalcent = globalcent - глобальные координаты (x, y)
        self.localcent = globalcent - player.coards - локальные координаты
        self.v - скорость
        self.angle - угол в градусах по часовой стрелке
        self.stop - видит ли перед собой преграду в виде другой машины
        self.hit - столкнулась ли машина
        self.playerstatus - True если playerr управляет ею
        self.sector - сектор в глобальных координатах
        self.rotatetime - время, которое машина поворачивает
        self.tex = textur
        self.time = 0 - личное время для проведения некорых процессов



    def collisions(obj):
        проверяет столкнулась ли машина с obj(другая машина), домами(напиши мне, обсудим) (объект с центром в obj.cent и шириной obj.hitbox)
            *******
        self.hit = True

    def stop(obj):
        проверяет есть ли машина перед ней на определенном расстоянии interval 
        если есть - self.stop = True

    def rotate((x0, y0 , alpha0), (x1, y1, alpha1))
        if self.rotatetime < 50
            self.time += 1
            машина за self.rotatetime = 50 плавно поворачивает из одного положения в другое
        else:
            self.time = 0

    def move(delta_v_player, param1 = 0, param2 = 0):
        if self.time != 0: 
            self.rotate(param1, param2)
        else:
            self.collisions
            self.stop
            if playerstatus:
                if not (self.hit and self.stop):
                    пересчет координат по скоростям
                else:
                    машина стоит
            else:
                delta_v_player - массив из 2 чисел, изменением скоростей персонажа по стрелкам
                преобразовать горизонтальные в изменение угла, а вертикальные в скорость (x, y)
            
                if not self.hit:
                    пересчет координат

    
        


    

        

    def draw
        отрисовка машины







"""