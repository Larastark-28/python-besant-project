#ATM MCHINE 

print("\n")
print("******IOB BANK ATM******")
pin=int(input("Enter your pin number :"))
balance=20000
if pin==2003:
    print("1.Withdraw")
    print("2.Balance")
    print("3.Deposit")
    choice=int(input("Enter your choice :"))
    if choice==1:
        withdraw=int(input("Enter your withdraw amount :"))
        if withdraw<20000:
            balance-=withdraw
            print("Collect your cash")
            print(f"Your balance is {balance}")
        else:
            print("invalid cash amount")
    elif choice==2:
        print(f"Your total balance is RS.{balance}")
    elif choice==3:
        deposit=int(input("Deposit your cash :"))
        balance+=deposit
        press=input(f"Your deposit cash is {balance} press y to continue n to cancel :")
        if press=='y':
            print("Successfully deposited")
        elif press=='n':
            print("Transaction cancelled")
        else:
            print("invalid choice")
    else:
        print("invalid choice")
else:
    print("invalid pin")
