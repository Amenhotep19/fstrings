"""
This is a script to convert km to miles.
"""

def get_km():
    i = 0
    while type(i) != float:
        i = input("Enter number of kilometers now. Only numbers are accepted.")
        try:
            i = float(i)
        except ValueError:
            pass
    return i

def convert(km):
    j = km * 0.621371
    return j
    
def main():
    km = get_km()
    miles = convert(km)
    print(f"{km} kilometers is {round(miles, 4)} miles.")
    
if __name__ == "__main__":
    main()