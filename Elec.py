units = float(input("Enter the number of units consumed: "))
cost_per_unit = 5.0
bill_amount = units * cost_per_unit
discount = 0
if bill_amount > 1000:
    discount = bill_amount * 0.10  # 10% discount
    bill_amount -= discount
print("\nElectricity Bill")
print("----------------")
print(f"Units Consumed : {units}")
print(f"Rate per Unit  : ₹{cost_per_unit}")
print(f"Discount       : ₹{discount}")
print(f"Total Bill     : ₹{bill_amount}")
