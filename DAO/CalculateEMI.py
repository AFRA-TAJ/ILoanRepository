#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from entity import Loan
from exception import InvalidLoanException
import math
class Loan:
    def calculateEMI(self,loan_id):
            try:
                loan=self.getLoan(loan_id)
                if loan is None:
                    raise InvalidLoanException("Invalid Loan ID")

                r=loan.interest_rate / 12 / 100
                n=loan.loan_term * 12
                p=loan.principal_amt
                emi=(p*r*math.pow((1+r),n))/(math.pow((1+r),n)-1)
                return emi
            except InvalidLoanException as e:
                print(e)
                return None
        
    def getLoan(self,loan_id):
        if loan_id == self.loan_id:
            return self
        else:
            return None
loan_instance=Loan(4,"joe",50000,0.05,6,"CarLoan","Pending")
emi_amount = loan_instance.calculateEMI(4)
print(f"EMI Amount: {emi_amount}")

