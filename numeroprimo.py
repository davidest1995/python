from sre_parse import State


def primo(value:int) -> bool:
    result_list = [i for i in range(1,value+1) if value % i ==0]
    result_final= len(result_list) == 2
    if result_final == True:
        print(value, "Es un número primo.")
    else:
        print(value, "no es un número primo, sus divisores son: ")
        print(result_list)

def run():
    input_x = input("Ingresa un número: ")
    value:int = int(input_x)
    if value >= 1:
        primo(value)

if __name__ == "__main__":
    run()