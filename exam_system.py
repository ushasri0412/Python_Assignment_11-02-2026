import logging
logging.basicConfig(
    filename="Exam_system.log",
    level=logging.INFO,
    format="%(asctime)s-%(levelname)s- %(message)s"
)
class Exam:
    school="bvrit"
    date_of_exam="12-02-2026"
    Total_marks =500
    pass_marks=100
    def __init__(self,name,roll_no,standard,subject):
        self.name=name
        self.roll_no=roll_no
        self.standard =standard
        self.subject=subject
        self.is_started=False
        self.is_submitted=False
    def start_exam(self):
        if not self.is_started:
            self.is_started=True
            logging.info("%s :exam started successfully",self.name)
        else:
            logging.error("exam already started") 
    def submit_exam(self):
        if self.is_started and not self.is_submitted:
            self.is_submitted=True
            logging.info("%s: Exam submitted successfully",self.name)
        elif not self.is_started==True:
            logging.info("exam not started")
        else:
            logging.info("exam already submitted")
    def calculate_score(self,obtained_marks):
        self.obtained_marks=obtained_marks
        if(self.obtained_marks< Exam.Total_marks):
            if(self.obtained_marks>Exam.pass_marks):
                logging.info("%s : PASS with marks %s",self.name,self.obtained_marks)
            else:
                logging.info("Fail")
        else:
            logging.warning("Wrong input")
    @classmethod
    def update_pass_marks(cls,new_pass):
        cls.pass_marks=new_pass
        logging.info("%s updated_pass_marks",new_pass)

s1=Exam("usha","224b9","5th","english")
s1.start_exam()
s1.submit_exam()
s1.calculate_score(200)
Exam.update_pass_marks(200)

s2=Exam("fnm","223b9","9th","telugu")
s2.start_exam()
s2.submit_exam()
s2.calculate_score(150)
Exam.update_pass_marks(150)