rows=int(input("How many rows: "))
columns=int(input("How many Colomns: "))
symbol=input("Enter the symbol: ")

for i in range(rows):
    for j in range(columns):
        print(symbol,end="")
    print()