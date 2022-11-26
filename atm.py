import time 

print("please insert your card")

time.sleep(5)

password = 1234

pin = int(input("Enter your atm pin: "))
balance = 5000
if pin == password:
    while True:
    
      print("""
    
       1 == balance
       2 == withdrawl amount
       3 == deposit balance
       4 == exit
    
    """
    )

      try:
            option = int(input("please enter your choice: "))
      except:
            print("please enter valid option: ")
    
      if option == 1:
          print("your current balance is", balance)
    
      if option == 2:
       
           withdrawl_amount = int(input("please enter withdraw_amounnt "))

           balance = balance - withdrawl_amount

           print(withdrawl_amount, "is debited from your account")

           print(f"your current balance is",balance)
      if option == 3:

           deposit_amount = int(input("please enter deposit_amount: "))

           balance = balance + deposit_amount

           print(deposit_amount," is credited to your account")

           print("your current balance is", balance)
    
      if option == 4:
        
          break

else:
    print("Invalid pin")


