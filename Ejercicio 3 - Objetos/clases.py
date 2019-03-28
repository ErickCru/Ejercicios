class Cuadrado():
    
    lado = 0
    '''
    Constructor para la clase cuadrado
    al cual se le envia como parametro un número
    el cual nos dice la medida de un lado del cuadrado.
    '''
    def __init__(self, lado):
        self.lado = lado

    # Método para calcular el área del cuadrado
    def area_cuadrado(self):
        return self.lado * self.lado

    def perimetro_cuadrado(self):
        return self.lado * 4

class Cubo(Cuadrado):

    def __init__(self, lado):
        self.lado = lado

    def volumen_cubo(self):
        return self.area_cuadrado() * self.lado

    def perimetro_cubo(self):
        return self.lado * 12
