#patient_Details
class Hospital:
    Hospital_name="ABCD HOSPITAL"
    Doctor_name ="Dr.kjfnsow"
    consultation_fee=2000
    Help_line="740301381489"
    mail="wiejffkwfw@gmail.com"

    def __init__(self,p_id,name,age,ph_no,aadhar_no,balance):
        self.p_id=p_id
        self.name=name
        self.age=age
        self.ph_no=ph_no
        self.aadhar_no=aadhar_no
        self.balance=balance
        self.is_admitted =False

    def display(self):
        print("patient_id:",self.p_id,"name:",self.name,"age:" ,self.age,"phone_number:" ,self.ph_no,"Aadhar_no:" ,self.aadhar_no,"hospital_card_balance:" ,self.balance)

    def admit(self,disease,room_no,days_in_room):
        self.disease=disease
        self.room_no=room_no
        self.days_in_room=int(days_in_room)
        self.room_charges=2000 # per day
        self.is_admitted=True
        print("disease:" ,self.disease,"room_no:",self.room_no,"Admitted for(in days):",self.days_in_room)
    
    def cal_bill(self):
        bill=(self.days_in_room*self.room_charges)+ Hospital.consultation_fee
        print("Total Bill :" ,bill) 
        return bill
        #balance_remain-=bill

    def discharge(self,paid_amount):
        bill=self.cal_bill()
        total_balance=self.balance+paid_amount
        if (self.is_admitted==True):
            if self.balance >= bill:
                self.balance-=bill
                print("payment cleared")
                self.is_admitted=False
            elif total_balance>bill:
                self.balance=total_balance-bill
                print("payment cleared- can discharge")
                self.is_admitted=False

            else:
                print("pending payment")
        else:
            print("patient already discharged")
    @classmethod
    def new_con_fee(cls,new_fee):
        cls.consultation_fee=new_fee
        print(new_fee)
p1=Hospital(1,"usha",21,47947844,7846349108,10000)
p1.display()
p1.admit("fever",101,3)
p1.discharge(0)
Hospital.new_con_fee(3000)
print("next patient")
p2=Hospital(2,"kiran",20,479485744,7842424548,10000)
p2.display()
p2.admit("eye_sight_check",102,5)
p2.discharge(2000)
Hospital.new_con_fee(1000)