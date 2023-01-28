# Instance variable: Name,Amount,Address,AccountNo
# Instance Method : CreateAccount,DisplayAccountinfo()
# Class Variable: Bank_Name,ROI_On_FD
# class Method: DisplayBankInformation
# Static Method : DisplayKYCInfo

class Bank_Account:

    Bank_Name = "HDFC bank PVT LTD"
    ROI_On_FD = 6.7  # Rate of interest

    def __init__(self):  # Default constructor no parameters it is automatically called
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

    @classmethod  # Decorator
    def DisplayBankInformation(cls):
        print("Welcome to Banking Console")
        print("Name of our bank is: ", cls.Bank_Name)
        print("Rate of Interest we offer on fixed deposit is: ", cls.ROI_On_FD)

    @staticmethod
    def DisplayKYCInfo():
        print("Please consider below KYC Information")
        print("According to the rules of Government of India you have to submit following documents")
        print("1.Clear and recent passport Size photo")
        print("2.Photo of Aadhar card")  # opencv
        print("3.Photo of PAN card")

    def Deposit(self, value):
        self.Amount = self.Amount+value

    def Withdraw(self, value):
        self.Amount = self.Amount-value


def main():
    print("-------------------------------------------")
    print("----------Banking Application --------------")
    print("----------------------------------------------------------------")
    print("-----------Calling Static method to display KYC info----------------")

    Bank_Account.DisplayKYCInfo()

    # without creating obj we can aceess class variable
    print("----------------------------------------------------------------")
    print("-----Accessing instance variable from main------")
    print("----------------------------------------------------------------")
    print("Name of Bank: ", Bank_Account.Bank_Name)
    print("Rate of interest on Fixed Deposit: ", Bank_Account.ROI_On_FD)

    print("----------------------------------------------------------------")
    print("---------- Calling the class method to display Bank informatrion ----------")
    print("----------------------------------------------------------------")

    Bank_Account.DisplayBankInformation()

    print("----------------------------------------------------------------")
    print("---------- Creating the objects of class ----------")
    print("----------------------------------------------------------------")

    User1 = Bank_Account()
    User2 = Bank_Account()

    print("----------------------------------------------------------------")
    print("Createing the first account")
    print("----------------------------------------------------------------")
    print("----------------------------------------------------------------")
    print("---------- Enter details for first account holder ----------")
    print("----------------------------------------------------------------")

    User1.CreateAccount()

    print("----------------------------------------------------------------")
    print("Createing the second account")
    print("----------------------------------------------------------------")
    print("----------------------------------------------------------------")
    print("---------- Enter details for second account holder ----------")

    User2.CreateAccount()

    print("----------------------------------------------------------------")
    print("---------- Calling instance method to display information of first account ----------")

    User1.DisplayAccountInfo()

    print("---------- Calling instance method to display information of second account ----------")

    User2.DisplayAccountInfo()

    print("---------- Depositing 500 in User1 ----------")

    User1.Deposit(500)

    print("---------- Depositing 1200 in User2 ----------")

    User2.Deposit(1200)

    print("Amount of {} after deposit is {}: ".format(User1.Name, User1.Amount))
    print("Amount of {} after deposit is {}: ".format(User2.Name, User2.Amount))

    print("---------- Withdraw 200 in User1 ----------")

    User1.Withdraw(200)

    print("---------- Withdraw 3000 in User2 ----------")
    User2.Withdraw(3000)
    # print("Amount of User1 after is : ",User1.Amount)
    # print("Amount of User2 after is : ",User2.Amount)
    print("Amount of {} after withdraw is {}: ".format(User1.Name, User1.Amount))
    print("Amount of {} after withdraw is {}: ".format(User2.Name, User2.Amount))

    print("----------------------------------------------------------------")
    print("---------- End of banking appplication ----------")
    print("----------------------------------------------------------------")


if __name__ == "__main__":
    main()
