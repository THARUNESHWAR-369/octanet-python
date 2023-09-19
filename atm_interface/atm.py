from user import User

class ATM:
    def __init__(self):
        self.users = {}
        self.users["user1"] = User("user1", "1234")
        self.users["user2"] = User("user2", "5678")

    def create_user(self, user_id, pin):
        if user_id not in self.users:
            self.users[user_id] = User(user_id, pin)
            return True
        else:
            return False

    def login(self, user_id, pin):
        if user_id in self.users:
            user = self.users[user_id]
            if user.authenticate(user_id, pin):
                return user
        return None

    def display_menu(self):
        print("ATM INTERFACE")
        print("1. DEPOSIT")
        print("2. WITHDRAW")
        print("3. TRANSFER")
        print("4. HISTORY")
        print("5. QUIT")

    def run(self):
        while True:
            print("\n\tWelcome to the ATM\n")
            user_id = input("Enter your User ID: ")
            pin = input("Enter your PIN: ")
            user = self.login(user_id, pin)

            if user:
                print(f"\nWelcome, {user_id}!\n")
                while True:
                    self.display_menu()
                    choice = input("Enter your choice: ")

                    if choice == '1':
                        amount = float(input("Enter the deposit amount: "))
                        user.deposit(amount)
                    elif choice == '2':
                        amount = float(input("Enter the withdrawal amount: "))
                        user.withdraw(amount)
                    elif choice == '3':
                        target_id = input("Enter the target user's User ID: ")
                        target_user = self.users.get(target_id)
                        if target_user:
                            amount = float(input("Enter the transfer amount: "))
                            user.transfer(target_user, amount)
                        else:
                            print("Target user not found.")
                    elif choice == '4':
                        user.display_transaction_history()
                    elif choice == '5':
                        print("Thank you for using the ATM. Goodbye!")
                        return
                    else:
                        print("Invalid choice. Please try again.")
            else:
                print("Invalid User ID or PIN. Please try again.")

if __name__ == "__main__":
    atm = ATM()
    atm.run()
