#bank_details 
class Bank:
    bankName="ICICI"
    branch="Hyderabad"
    ifsc_code="ICICI349000244"
    phone="4349458292"
    mail="userhelpdesk@icici.bank.in"
    min_bal=2000

    def __init__(self,name,age,ph_no,pan_no,balance):
        self.name=name
        self.age=age
        self.ph_no=ph_no
        self.pan_no=pan_no
        self.balance=balance
    def withdraw(self,w_money):
        if w_money>=Bank.min_bal and w_money<=self.balance:
            self.balance-=w_money
        else:
            print("Insufficient Balance")
    def deposit(self,d_money):
        if d_money>0:
            self.balance+=d_money
        else:
            print("invalid amount to debit")
    def display(self):
        print(self.name,self.age,self.ph_no,self.pan_no,self.balance)
    @classmethod
    def update_min_bal(cls,new_min_bal):
        cls.min_bal=new_min_bal
        print("updated_min_balance: ",new_min_bal)
print("b1")
b1=Bank("Usha",21,"4682249765","3699FYKST579",70000)
b1.display()
b1.withdraw(2000)
b1.display()
b1.deposit(10000)
b1.display()
Bank.update_min_bal(3000)
print("b2")
b2=Bank("Kiran",20,"4642249747","3699FGYHJ4",3500)
b2.display()
b2.withdraw(600)
b2.display()
b2.deposit(90000000)
b2.display()
Bank.update_min_bal(4000)
print("b3")
b3=Bank("Sai",24,"4425349765","317KHK8K579",3000) # why is it accepting balance less than min_bal
b3.display()
b3.withdraw(10)
b3.display()
b3.deposit(-334)
b3.display()
Bank.update_min_bal(3500)