units = float(input("Enter the number of units consumed: "))
cost_per_unit = 5.0
bill_amount = units * cost_per_unit
print("\nElectricity Bill")
print("----------------")
print(f"Units Consumed : {units}")
print(f"Rate per Unit  : ₹{cost_per_unit}")
print(f"Total Bill     : ₹{bill_amount}")
