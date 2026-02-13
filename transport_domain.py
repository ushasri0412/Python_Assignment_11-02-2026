import logging
logging.basicConfig(
    filename="railway.log",
    level=logging.INFO,
    format="%(asctime)s-%(levelname)s- %(message)s"
)
class Ticket:
    TRAIN_NAME="GODAVARI"
    TRAIN_NO="309741354"
    Base_fare=100
    
    def __init__(self,cus_name,age,gender):
        self.cus_name=cus_name
        self.age=age
        self.gender=gender
        self.ticket_booked=False
        self.ticket_cancelled=False
    def book_ticket(self):
        if not self.ticket_booked:
            self.ticket_booked=True
            logging.info("Ticket booked on %s's name",self.cus_name)
        else:
            logging.info("Ticket already booked on %s's name",self.cus_name)
    def cancel_ticket(self):
        if self.ticket_booked and not self.ticket_cancelled:
            self.ticket_cancelled=True
            logging.info("Ticket on name %s is cancelled successfully",self.cus_name)
        elif self.ticket_cancelled:
            logging.info("Ticket already cancelled on %s's name",self.cus_name)
        else:
            logging.info("Ticket not booked on %s's name",self.cus_name)
    def cal_fare(self,charges):
        if not self.ticket_cancelled:
            self.charges=charges
            if self.age>60 or self.age<5:
                fare=self.charges+Ticket.Base_fare
                total_fare=fare-(50*fare)/100
                logging.info("Ticket fare booked by %s is %s",self.cus_name,total_fare)
            elif(self.gender=="F" or self.gender=="f"):
                fare=self.charges+Ticket.Base_fare
                total_fare=fare-(20*fare)/100
                logging.info("Ticket fare booked by %s is %s",self.cus_name,total_fare)
            else:
                total_fare=self.charges+Ticket.Base_fare
                logging.info("Ticket fare booked by %s is %s",self.cus_name,total_fare)
        else:
            logging.info("Ticket cancelled")
    @classmethod
    def update_base_fair(cls,new_fare):
        cls.Base_fare=new_fare
        logging.info("New Base Fare is %s", cls.Base_fare)
t1=Ticket("Usha",21,"F")
t1.book_ticket()
t1.cal_fare(1000)
Ticket.update_base_fair(200)

    

        




