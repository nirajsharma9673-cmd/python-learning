try:
    with open(r"C:\Users\niraj\python learning\File i\o\intorduction.txt", "r") as file:
        data = file.read()
        words = data.split()

        for value in words:
            if value == "start":
                raise ValueError("The word 'start' is found")
        print(file.tell())

except SyntaxError as e:
    print(e)

finally:
    print("Program executed completely")
    
    

    