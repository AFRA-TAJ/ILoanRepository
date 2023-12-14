#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from entity import Loan
from exception import InvalidLoanException
import math
class Loan:
    def calculateinterest(self,loan_id):
        try:
            loan = self.getLoan(loan_id)
            if loan is None:
                raise InvalidLoanException("Invalid Loan ID")
            interest = (loan.principal_amt*loan.interest_rate*loan.loan_term)/12
            return interest
        
        except InvalidLoanException as e:
            print(e)
            return None
        
    def getLoan(self,loan_id):
        if loan_id == self.loan_id:
            return self
        else:
            return None
loan_instance=Loan(1,"diya",30000,0.5,12,"CarLoan","Approved")
interest_amount = loan_instance.calculateinterest(1)
print(f"Interest Amount: {interest_amount}")

