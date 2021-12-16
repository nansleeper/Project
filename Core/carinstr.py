"""
class Car():
    def __init__(globalcent):
        self.globalcent = globalcent - глобальные координаты (x, y)
        self.localcent = globalcent - player.coards - локальные координаты
        self.v - скорость
        self.angle - угол в градусах по часовой стрелке
        self.stop - видит ли перед собой преграду в виде другой машины
        self.hit - столкнулась ли машина
        self.playerstatus - True если playerr управляет ею
        self.sector - сектор в глобальных координатах
        self.rotatetime - время, которое машина поворачивает



    def collisions(obj):
        проверяет столкнулась ли машина с obj(другая машина)
            *******
        self.hit = True

    def stop(obj):
        проверяет есть ли машина перед ней на определенном расстоянии interval 
        если есть - self.stop = True

    def rotate((x0, y0 , alpha0), (x1, y1, alpha1))
        self.time += 1
        машина за self.rotatetime плавно поворачивает из одного положения в другое
        if self.rotatetime <

    def move(delta_v_player):

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