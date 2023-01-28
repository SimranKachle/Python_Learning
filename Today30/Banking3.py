# Instance variable: Name,Amount,Address,AccountNo
# Instance Method : CreateAccount,DisplayAccountinfo()
# Class Variable: Bank_Name,ROI_On_FD
# class Method: DisplayBankInformation


class Bank_Account:
    
    Bank_Name = "HDFC bank PVT LTD"
    ROI_On_FD=6.7#Rate of interest
    
    def __init__(self):#Default constructor no parameters it is automatically called
        self.Name = ""  # represents string
        self.Amount = 0  # represents int
        self.Address = ""
        self.AccountNo = 0

    def CreateAccount(self):
        print("Enter your name: ")
        self.Name = input()

        print("Enter your initial Amount: ")
        self.Amount = int(input())

        print("Enter your Address: ")
        self.Address = input()

        print("Enter your Account Number: ")
        self.AccountNo = int(input())

    def DisplayAccountInfo(self):
        print("-------------Your Account Information is as below--------------")
        print("Name of Account Holder: ", self.Name)
        print("Account Number: ", self.AccountNo)
        print("Address of Account Holder: ", self.Address)
        print("Cuurent Amount in account: ", self.Amount)

    @classmethod #Decorator
    def DisplayBankInformation(cls):
        print("Welcome to Banking Console")
        print("Name of our bank is: ",cls.Bank_Name)
        print("Rate of Interest we offer on fixed deposit is: ",cls.ROI_On_FD)
        
    
    
    
def main():
    
    print("Name of Bank: ",Bank_Account.Bank_Name)#without creating obj we can aceess class variable
    print("Rate of interest on Fixed Deposit: ",Bank_Account.ROI_On_FD)
    
    Bank_Account.DisplayBankInformation()
    
    User1 = Bank_Account()
    User2 = Bank_Account()

    print("Creating First Account")
    User1.CreateAccount()

    print("Creating Second Account")
    User2.CreateAccount()

    User1.DisplayAccountInfo()
    User2.DisplayAccountInfo()


if __name__ == "__main__":
    main()
