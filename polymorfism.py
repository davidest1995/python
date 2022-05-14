class Persona():
    def __init__(self, nombre):
        self.nombre= nombre

    def avanza(self):
        print("Esta caminando")

class Ciclista(Persona):

    def __init__(self, nombre):
        super().__init__(nombre)

    def avanza(self):
        print ('Esta rodando en la bici')

def run():
    persona= Persona('David')
    persona.avanza()

    ciclista = Ciclista('Carlitos')
    ciclista.avanza()


if __name__ == '__main__':
    run()