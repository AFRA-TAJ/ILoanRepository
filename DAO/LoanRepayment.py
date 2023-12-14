#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from entity import Loan
from Exception import InvalidLoanException
import math
class Loan:   
    def calculateEMI(self):
        P=self.principal_amt
        R=self.interest_rate/12/100
        N=self.loan_term
        emi=(P*R*(pow(1+R,N)))/(pow(1+R,N)-1)
        return emi
    
    def loanRepayment(self,amount):
        try:
            emi_amt=self.calculateEMI()
            if amount < emi_amt:
                raise InvalidLoanException("Payment is less than 1 emi")
            no_of_emi_paid = int(amount/emi_amt)
            self.no_of_emi_paid += no_of_emi_paid

            print(f"{no_of_emi_paid} EMIs paid successfully.")
            return no_of_emi_paid
        except InvalidLoanException as e:
            print(e)
            return None
    
loan_instance = Loan(1, "josh", 90000, 0.05, 6, "CarLoan", "Pending")
paid_emis = loan_instance.loanRepayment(2000)
print(f"Total EMIs paid: {paid_emis}")

