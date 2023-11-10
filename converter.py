global dollar
global euro
    
def converter():
    global dollar
    dollar = 4.80
    global euro
    euro = 5.60
    
    print("D - Dollar  |  E - Euro")
    op = str(input('You want to convert to Dollar or Euro? '))
    
    if op == 'D':
        real = float(input("Type the number in Brazilian Real: "))
        converter = real / dollar
        print("Alright, you have {:.2f} dollars now!".format(converter))
    elif op == 'E':
        real = float(input("Type the number in Brazilian Real: "))
        converter = real / euro
        print("Good, you have {:.2f} euros now!".format(converter))
    else:
        print("Invalid Option!")

converter()
    
    
    