def make_division_by(n):
    assert type(n) == int, "solo puedes utilizar numeros "
    def division_by(x):
        assert type(x) == int, "solo puedes utilizar numeros "
        return x / n
    return division_by

division_by_3= make_division_by(3)
print(division_by_3(18))
division_by_5= make_division_by(5)
print(division_by_5(100))
division_by_18= make_division_by(18)
print(division_by_18(54))