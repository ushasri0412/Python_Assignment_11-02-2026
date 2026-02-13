import logging
logging.basicConfig(
    filename="hostel_accomodation.log",
    level=logging.INFO,
    format="%(asctime)s-%(levelname)s- %(message)s"
)
class HostelRoom:
    Room_rent_per_day=100
    HOSTEL_NAME="USHA"

    def __init__(self,name,room_no):
        self.name=name
        self.room_no=room_no
        self.is_room_allocated=False
        self.is_room_vacated=False

    def allocate_room(self):
        if not self.is_room_allocated:
            self.is_room_allocated=True
            logging.info("room is allocated to %s and room-no is %s",self.name,self.room_no)
        else:
            logging.info("room already allocated to %s",self.name)
    def vacate_room(self):
        if not self.is_room_vacated and self.is_room_allocated:
            self.is_room_vacated=True
            logging.info("room is vacated by %s",self.name)
        elif not self.is_room_allocated:
            logging.info("room not allocated to %s",self.name)
        else:
            logging.info("room already vacated by %s",self.name)
    def month_room_rent(self,months):
        self.months=months
        rent=(HostelRoom.Room_rent_per_day*30)*months
        logging.info("room rent for %s months is %s",months,rent)
    @classmethod
    def update_room_rent(cls,new_rent_per_day):
        cls.Room_rent_per_day=new_rent_per_day
        logging.info("updated room rent is %s",cls.Room_rent_per_day)
h1=HostelRoom("usha","43h1")
h1.allocate_room()
h1.month_room_rent(3)
h1.update_room_rent(200)

h2=HostelRoom("Kiran","43h3")
h1.allocate_room()
h1.vacate_room()
h1.month_room_rent(7)
h1.update_room_rent(300)
