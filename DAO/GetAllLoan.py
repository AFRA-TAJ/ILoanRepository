#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from entity import Loan
class Loan:
    def getAllLoan(loans):
        for loan in loans:
            print(f"Loan ID: {loan.loan_id}, Principal Amount: {loan.principal_amt}, Interest Rate: {loan.interest_rate}%, Loan Term: {loan.loan_term} months, Loan Type:{loan.loan_type}, Loan Status: {loan.loan_status}")

            
loan1=Loan((1,"diya",30000,0.5,12,"CarLoan","Approved")
loan2=Loan(2,"priya",40000,0.5,24,"HomeLoan","Pending")
loan3=Loan(3,"joe",50000,0.5,6,"CarLoan","Pending")
all_loans=[loan1,loan2,loan3]
Loan.getAllLoan(all_loans)

