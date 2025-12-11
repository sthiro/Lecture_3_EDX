grocery = {}

while True:
    try:
        item = input().upper() # make the input text upper case

        if item not in grocery.keys(): # Check whether it's not in grocery values
            grocery[item] = 1 # To aboid starting with 0

        else:
          grocery[item] = grocery[item] + 1

    except EOFError:

        sorted_name = sorted(grocery) # Returns List for sorted grocery dict keys

        for name in sorted_name:
            print(grocery[name], name)

        break   
