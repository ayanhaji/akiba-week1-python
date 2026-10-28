
customer = input("Enter customer name: ")
product = input("Enter product name: ")
price = float(input("Enter product price in ETB: "))
quantity = int(input("Enter quantity: "))
total = price * quantity


print("RECEIPT")
print(f"Customer: {customer}")
print(f"{'Product'}   {'Price'}   {'Qty'}")
print(f"{product}       {price}     {quantity}")
print(f"{'Total:'}{total} ETB")
print("Thank you for shopping!")
