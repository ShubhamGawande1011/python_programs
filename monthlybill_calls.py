user = float(input("Enter the numbers of calls :"))
calls = float(input("Enter the price of the calls :"))
monthly_bill = calls * user

print(f"the Monthly bills is{monthly_bill} ")

if calls == 100:
    print("minimum rs 200.")
elif calls == 50:
    print("rs 50 per calls")

elif calls == 60:
    print("rs 50 per calls")
elif calls > 200:
    print("rs 0.40 per calls")
