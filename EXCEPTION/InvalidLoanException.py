#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class InvalidLoanException(Exception):
    def __init__(self, message="Invalid Loan ID"):
        self.message = message
        super().__init__(self.message)
    

