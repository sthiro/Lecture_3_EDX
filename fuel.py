    
while True:    
    try:

        fuel_list = input("Fraction: ").split("/")
        is_decimal = fuel_list[0].isdecimal() and fuel_list[1].isdecimal() # Checks whether input are whole number
        
        x, y = int(fuel_list[0]), int(fuel_list[1]) # X / Y Format

        output = (x / y) * 100 # Calculates percentage
        
        if output > 100: continue
        elif output <= 1:
            print("E")
        elif output >= 99:
            print("F")
        else:
            print(round(output), "%", sep="")

        break

    except (ValueError, ZeroDivisionError):
        continue