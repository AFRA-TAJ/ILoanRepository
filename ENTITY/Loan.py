#!/usr/bin/env python
# coding: utf-8

# In[1]:


class Loan:
    def __init__(self, loan_id,customer,principal_amt,interest_rate,loan_term,loan_type,loan_status):
        self.loan_id=loan_id
        self.customer=customer
        self.principal_amt=principal_amt
        self.interest_rate=interest_rate
        self.loan_term=loan_term
        self.loan_type=loan_type
        self.loan_status=loan_status
        
    def get_loan_id(self):
        return self.loan_id
    def get_customer(self):
        return self.customer
    def get_principal_amt(self):
        return self.principal_amt
    def get_interest_rate(self):
        return self.interest_rate
    def get_loan_term(self):
        return self.loan_term
    def get_loan_type(self):
        return self.loan_type
    def get_loan_status(self):
        return self.loan_status
    
    def set_loan_id(self):
        self.loan_id=loan_id
    def set_customer(self):
        self.customer=customer
    def set_principal_amt(self):
        self.principal_amt=principal_amt
    def set_interest_rate(self):
        self.interest_rate=interest_rate
    def set_loan_term(self):
        self.loan_term=loan_term
    def set_loan_type(self):
        self.loan_type=loan_type
    def set_loan_status(self):
        self.loan_status=loan_status
        
    def print_info(self):
        print(f"Loan ID:{self.loan_id}")
        print(f"Customer:{self.customer}")
        print(f"Principal Amt:{self.principal_amt}")
        print(f"Interest Rate:{self.interest_rate}")
        print(f"Loan Term:{self.loan_term}")
        print(f"Loan Type:{self.loan_type}")
        print(f"Loan Status:{self.loan_status}")
loan_instance1=Loan(1,"diya",30000,0.5,12,"CarLoan","Approved")
loan_instance2=Loan(2,"priya",40000,0.5,24,"HomeLoan","Pending")
loan_instance3=Loan(3,"joe",50000,0.5,6,"CarLoan","Pending")
loan_instance1.print_info()
loan_instance2.print_info()
loan_instance3.print_info()


# In[ ]:




