pin_Atm = 2526

n=int(input("Enter a 4-Digit PIN:"))

balance = 10000  

if n==pin_Atm:
        print("WELCOME")
        while True:
             print("\n1. Check Balance")
             print("2. Withdraw Money")
             print("3. Deposit Money")
             print("4. Exit")

             Choice=int(input("Enter your choice(1/2/3/4):"))

             if Choice==1:
                   print("Your current balance is : $",balance)
             elif Choice==2:
                   amount=int(input("Enter the amount to withdraw:"))
                   if amount % 100 != 0:
                        print("Please enter the amount in multiples of 100.")
                   elif amount <= balance:
                        balance -= amount
                        print(f"${amount} withdrawn successfully")
                   else:
                        print("Insufficient balance")
             elif Choice==3:
                   print("Enter the amount to deposit:")
                   amount=int(input())  
                   if amount % 100 != 0:
                        print("Please enter the amount in multiples of 100.")
                   else:
                        balance += amount
                        print(f"${amount} deposited successfully")
             elif Choice==4:
                   print("Thank you for using the ATM")
                   break
             else:
                   print("Invalid choice")

else:
    print("PIN INVALID")


