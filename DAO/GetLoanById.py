#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from exception import InvalidLoanException
from entity import Loan
class Loan:
    def getLoanById(self,loan_id):
        for loan in all_loans:
            if loan.loan_id == loan_id:
                print(f"Loan ID: {loan.loan_id}, Principal Amount: {loan.principal_amt}, Interest Rate: {loan.interest_rate}%, Loan Term: {loan.loan_term} months, Loan Type:{loan.loan_type}, Loan Status: {loan.loan_status}")
                return
        raise InvalidLoanException(f"LoanID {loan_id} not found.")
            
loan1=Loan(1,"diya",30000,0.5,12,"CarLoan","Approved")
loan2=Loan(2,"priya",40000,0.5,24,"HomeLoan","Pending")
loan3=Loan(3,"joe",50000,0.5,6,"CarLoan","Pending")
all_loans=[loan1,loan2,loan3]
try:
    loan1.getLoanById(1)
except InvalidLoanException as e:
    print(e)
    

