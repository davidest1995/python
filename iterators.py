import time

class FiboIter():
    def __init__(self, max):
        self.max:int = max

    def __iter__(self):
        self.n1 = 0
        self.n2 = 1
        self.counter = 0
        return self
    def __next__(self):
        if self.counter == 0:
            self.counter += 1
            return self.n1 
        elif self.counter == 1:
            self.counter += 1
            return self.n2
        else: 
            self.aux = self.n1 + self.n2
            if self.aux >= self.max:
                raise StopIteration
            self.n1, self.n2 = self.n2, self.aux
            self.counter += 1
            return self.aux
                

if __name__ == "__main__":
    max = int(input("Ingresa el número máximo al que quieres que llegue la serie:  "))
    fibonacci = FiboIter(max)
    for element in fibonacci:
        print (element)
        time.sleep(1)