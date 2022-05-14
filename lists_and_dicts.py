def run():
    my_list= [1, "hello", True, 4.5]
    my_dict={"firtname": "David Esteban", "lastname" : "Arenas Ossa" }


    super_list = [
        {"firstname": "David Esteban", "lastname" : "Arenas Ossa" },
        {"firstname": "Carolina", "lastname" : "Cifuentes Yepes" },
        {"firstname": "Dennis Eugenia", "lastname" : "Ossa Jimenez" },
        {"firstname": "Martin Darío", "lastname" : "Arenas Ballesteros" }, 
    ]

    super_dict= {
        "natural_nums" : [1, 2, 3, 4, 5],
        "integer_nums" : [-2, -1, 0, 1, 2],
        "floating_nums" :[1.2 , 3,4, 4,6, 6,8],
    }

    for key, value in super_dict.items():
        print(key," = ", value)

    for i in super_list:
        print(i)

    print(my_list)
if __name__ == '__main__':
    run()
