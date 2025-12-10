def percentage(prompt):

    input_list = input("Fraction: ").split("/")       
    x, y = int(input_list[0]), int(input_list[1]) # X / Y Format

    output = (x / y) * 100 # Calculates percentage

    if output > 100 :
        raise ValueError("percentage value greater than 100")
    if output < 0:
        raise ValueError("Cannot be negative value")
    
    return output

def main():
    while True:    
        try:
            output = percentage("Fraction: ")

            if output <= 1:
                print("E")
            elif output >= 99:
                print("F")
            else: print(round(output), "%", sep="")

        except (ValueError, ZeroDivisionError):
            continue

        else: 
            break

main()