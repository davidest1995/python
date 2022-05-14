
from typing import Literal


def make_repeater_of(n:str)-> str:
    def repeater(string):
        assert type(string) == str, "solo puedes utilizar cadenas "
        return string * n
    return repeater

def run():
    repeat_5=make_repeater_of(5)
    x=input("Ingrese la palabra: ")
    print(repeat_5(x))

    
if __name__ == "__main__":
    run()
