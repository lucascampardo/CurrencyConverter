def converter(amount, currency_rate):
    try:
        amount = float(amount)
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        return 
    
    converted_amount = amount / currency_rate
    return converted_amount

def main():
    exchange_rates = {'D': 4.80, 'E': 5.60}
    
    print("D - Dollar  |  E - Euro")
    opt = input("You want to convert to Dollar or Euro? ").upper()
    
    if opt in exchange_rates:
        try:
            amount = float(input("Type the number in Brazilian Real: "))
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            return 
        
        converted_amount = converter(amount, exchange_rates[opt])
        print("You have {:.2f} now!".format(converted_amount, opt))
    else: 
        print("Invalid Option!")
        
if __name__ == "__main__":
    main()
