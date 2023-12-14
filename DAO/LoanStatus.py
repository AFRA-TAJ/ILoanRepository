#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from entity import Customer
from entity import Loan
class Loan:
    def loanstatus(self):
        if self.customer.credit_score > 650:
            self.loan_status = "Approved"
            print("Loan Approved!")
        else:
            self.loan_status = "Rejected"
            print("Loan Rejected.")

loan.loanstatus()

