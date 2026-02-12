#library book system
class library_book:
    libraryName="BVRIT"
    Location="Hyderabad"
    fine_per_day=10
    days=5
    def __init__(self,name,roll_no,ph_no):
        self.name=name
        self.roll_no=roll_no
        self.ph_no=ph_no

    def issue_book(self,book_no,book_name,issue_date,issued_days):
        self.book_no=book_no
        self.book_name=book_name
        self.issue_date=issue_date
        self.issued_days=issued_days
        self.is_issued=True
        print(book_name,"-",book_no,"book is issued to" ,self.name)
    def cal_fine_amt(self):
        fine_days=self.issued_days-library_book.days
        fine=fine_days*library_book.fine_per_day
        print("book is late for days:", fine_days)
        return fine 
    def return_book(self):
        if (self.is_issued==True):
            fine=self.cal_fine_amt()
            print("total_fine",fine)
            self.is_issued=False
        else:
            print("book not issued")
    @classmethod
    def updated_fine_per_day(cls,new_fine):
        cls.fine_per_day=new_fine
        print("new fine_per_day:" ,cls.fine_per_day)
        
s1=library_book("Usha","4b9","23117432430")
s1.issue_book("3A","life","1-02-2026",8)
s1.return_book()
library_book.updated_fine_per_day(20)

s2=library_book("Kiran","3h8","2324748290")
s2.issue_book("3","life","1-02-2026",7)
s2.return_book()
library_book.updated_fine_per_day(30)