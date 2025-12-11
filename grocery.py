grocery = {}

while True:
    try:
        item = input().upper() # make the input text upper case

        if item not in grocery.values(): # Check whether it's not in grocery values
            grocery[len(grocery)] = item

        else:
            index_val = list(grocery.values()).index(item) #Get an list like index for dic for a perticular value
            grocery.update({index_val +1 :item}) # updating number fail need to check that NOTE



    except EOFError:

        print(grocery)
        break