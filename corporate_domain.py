import logging
logging.basicConfig(
    filename="Payroll_system.log",
    level=logging.INFO,
    format="%(asctime)s-%(levelname)s- %(message)s"
)
class Employee:
    COMPANY_NAME ="CSP"
    JOB="MANAGER"
    Hra_percentage=10
    leave_ded_per_day=100

    def __init__(self,emp_id,emp_name,basic_sal):
        self.emp_id=emp_id
        self.emp_name=emp_name
        self.basic_sal=basic_sal
        self.leave_ded=0
       
    def apply_leave_ded(self,days):
        self.days=days
        self.leave_ded=Employee.leave_ded_per_day*days
        logging.info("succefully applied leave detection for %s days",days)
    def cal_sal(self):
        hra=(self.basic_sal*Employee.Hra_percentage)/100
        total_sal=(self.basic_sal+hra)-self.leave_ded
        logging.info("Gross Salary of %s is: %s",self.emp_name,total_sal)
    def display_payslip(self):
        logging.info(
            "PAY SLIP \n"
            "EMPLOYEE_ID: %s \n"
            "EMPLOYEE_NAME: %s\n"
            "EMPLOYEE_BASIC_SAL: %s \n"
            "EMPLOYEE_LEAVE_DEDUCTION: %s\n"
            "EMPLOYEE_TOTAL_GROSS_SAL: %s",
            self.emp_id,
            self.emp_name,
            self.basic_sal,
            self.leave_ded
        )
    @classmethod
    def update_hra_per(cls,new_hra_per):
        cls.Hra_percentage=new_hra_per
        logging.info("Updated HRA percentage is %s",cls.Hra_percentage)
e1=Employee(1,"Usha",10000)
e1.cal_sal()
e1.apply_leave_ded(4)
e1.display_payslip()
Employee.update_hra_per(20)