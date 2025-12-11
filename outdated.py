#Input date format ==> 9/8/1636 or September 8, 1636 MM/DD/YYYY
#Output date format ==> 1636-09-08  YYYY-MM-DD

#print(f"{n:02}")
#wherein, if n is a single digit, it will be prefixed with one 0, per docs.python.org/3/library/string.html#format-string-syntax.

#Assume that every month has no more than 31 days
#no need to validate whether a month has 28, 29, 30, or 31 days.

months=  [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

def format_converted(date_str):

    try:
        month, day, year = date_str.split("/") # Unformatted date 
        month, day, year = int(month), int(day), int(year)

    except ValueError: # If it's in text format like September 8, 1636

        date = date_str.split(" ") #Make a list 
        
        month = months.index(date[0]) + 1 # Finds index in months list and add 1 to make jan as first index ,not as 0 index
        # .index raises Value error if there is no such item
        # in this case it works for wrong format too

        day = int(date[1][:-1]) # slicing to avoid comma "," in day
        year = int(date[2])

        # Validation and Raising my own error
    if (not 0 < month <= 12) or (not 0 < day <= 31) or (not year >= 0):
        raise ValueError("Invalid Date format")

    return f"{year:04}-{month:02}-{day:02}"
    


def main():
    while True:
            try:

                date = input("Date: ")

                formatted_date = format_converted(date)

                print(formatted_date)
                break

            except ValueError: 
                 
                 continue

main()