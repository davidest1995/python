def run():


    first_dict = {i : i**3 for i in range(1,101) if (i % 3 !=0)}

    print (first_dict)


if __name__ =="__main__":
    run()