exchange_rate = 150
usd_amount = float(input("Enter amout in USD:"))
etb_amount = usd_amount * exchange_rate
print("CURRENCY EXCHANGE")
print(f"USD Amount: {usd_amount} USD")
print(f"Exchange Rate: 1 USD = {exchange_rate} ETB")
print(f"ETB Amount: {etb_amount} ETB")