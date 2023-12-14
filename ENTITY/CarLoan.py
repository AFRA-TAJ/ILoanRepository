#!/usr/bin/env python
# coding: utf-8

# In[2]:


from entity import Loan


# In[ ]:


class CarLoan(Loan):
    def __init__(self,loan_id,customer,principal_amt,interest_rate,loan_term,loan_type,loan_status,car_model,car_value):
        super().__init__(loan_id,customer,principal_amt,interest_rate,loan_term,"CarLoan",loan_status)
        self.car_model=car_model
        self.car_value=car_value
        
    def get_car_model(self):
        return self.car_model
    def get_car_value(self):
        return self.car_value
    
    def set_car_model(self):
        self.car_model=car_model
    def set_car_value(self):
        self.car_value=car_value
        
    def print_info(self):
        super().print_info()
        print(f"Car Model:{self.car_model}")
        print(f"Car Value:{self.car_value}")
carloan_instance1=CarLoan(1,"dev",40000,0.05,6,"CarLoan","Pending","SWIFT",55000) 
carloan_instance2=CarLoan(2,"kaif",50000,0.5,12,"CarLoan","Approved","HONDA",70000) 
carloan_instance3=CarLoan(3,"faiz",20000,0.5,18,"CarLoan","Pending","KIA",95000)
carloan_instance1.print_info()
carloan_instance2.print_info()
carloan_instance3.print_info()

