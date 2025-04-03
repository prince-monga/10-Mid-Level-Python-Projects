from forex_python.converter import CurrencyRates

cr = CurrencyRates()

try:
    amount = float(input("Enter amount: "))
    from_currency = input("Enter your currency (e.g., USD): ").upper()
    to_currency = input("In which currency you want to change (e.g., INR): ").upper()

    if amount <= 0:
        print("Amount must be greater than zero!")
    else:
        result = cr.convert(from_currency, to_currency, amount)
        print(f"{amount} {from_currency} is equal to {result:.2f} {to_currency}")

except Exception as e:
    print("Error:", e)
