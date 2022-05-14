# class rectangulo():

#     def __init__(self, base, altura):
#         self.base = base
#         self.altura = altura

#     def area(self):
#         return self.base * self.altura

# class cuadrado(rectangulo):

#     def __init__(self, lado):
#         super().__init__(lado, lado)

# if __name__ == '__main__':
#     rect = rectangulo(base= 4,altura= 5)
#     print (rect.area())

#     square = cuadrado(lado= 5)
#     print(square.area())

class Rectangulo():
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def Area(self):
        return self.base * self.altura

class Cuadrado(Rectangulo):

    def __init__(self,lado):
        super().__init__(lado, lado)

if __name__ == '__main__':
    rectangulo = Rectangulo(base= 20,altura= 5)
    cuadrado= Cuadrado(lado= 5)

    print(cuadrado.Area())
    print(rectangulo.Area())

















