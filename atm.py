class Atm:
    def __init__(self,cardnumber,pin):
        self.cardnumber=cardnumber
        self.pin=pin

    def balanceinquiry(self):
        print('your balance is 100$:')

    def cash withdrawl(self,amount):
        new_amount= 100-amount
        print('you withdrawed'"+ str(amount)+"your remaining balance is:"+str (new_amount))

def main():
    name=input("what is your name:")
    print("hello," +name)
    cardnumber=input("input your card number:")
    pin =input("input your pin:")
    new_user=Atm(cardnumber,pin)

    print("choose your activity")
    print("1.balance inquiry")
    print("2.Cash Withdrawl")
    activity=int(input("enter activity choice"))

    if(activity==1):
        newuser.balanceinquiry()
    elif(activity==2):
        amount=int(input("Enter the amount"))
        new_user=cashwithdrawl(amount)
    else:
        print("Enter a valid amount")

if __name__=="__main__"
main()






