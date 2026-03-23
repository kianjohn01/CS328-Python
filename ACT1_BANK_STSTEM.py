def banking_system():
    balance = 0.0
    
    while True:
        print("\n--- Simple Banking System ---")
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Exit")
        
        choice = input("Select an option (1-4): ")

        if choice == '1':
            print(f"\nYour current balance is: ${balance:,.2f}")
        
        elif choice == '2':
            amount = float(input("Enter amount to deposit: "))
            if amount > 0:
                balance += amount
                print(f"Successfully deposited ${amount:,.2f}")
            else:
                print("Invalid amount. Please deposit a positive value.")
        
        elif choice == '3':
            amount = float(input("Enter amount to withdraw: "))
            if amount > balance:
                print("Insufficient funds!")
            elif amount <= 0:
                print("Invalid amount. Please enter a positive value.")
            else:
                balance -= amount
                print(f"Successfully withdrew ${amount:,.2f}")
        
        elif choice == '4':
            print("Thank you for using our banking system. Goodbye!")
            break
        
        else:
            print("Invalid selection. Please try again.")


if __name__ == "__main__":
    banking_system()
