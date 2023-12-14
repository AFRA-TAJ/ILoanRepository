#!/usr/bin/env python
# coding: utf-8

# In[6]:


class Customer:
    def __init__(self, customer_id, name, email, phone_num, address, credit_score):
        self.customer_id = customer_id
        self.name = name
        self.email = email
        self.phone_num = phone_num
        self.address = address
        self.credit_score = credit_score
        
    def get_customer_id(self):
        return self.customer_id
    def get_name(self):
        return self.name
    def get_email(self):
        return self.email
    def get_phone_num(self):
        return self.phone_num
    def get_address(self):
        return self.address
    def get_credit_score(self):
        return self.credit_score
    
    def set_customer_id(self):
        self.customer_id = customer_id
    def set_name(self):
        self.name = name
    def set_email(self):
        self.email = email
    def set_phone_num(self):
        self.phone_num = phone_num
    def set_address(self):
        self.address = address
    def set_credit_score(self):
        self.credit_score = credit_score
        
    def print_info(self):
        print(f"Customer ID:{self.customer_id}")
        print(f"Name:{self.name}")
        print(f"Email:{self.email}")
        print(f"Phone Number:{self.phone_num}")
        print(f"Address:{self.address}")
        print(f"Credit Score:{self.credit_score}")
customer_instance1=Customer(1,"diya","diya@example.com",1234567876,"123 street",670)
customer_instance2=Customer(2,"priya","priya@example.com",8299967876,"456 street",870)
customer_instance3=Customer(3,"joe","diya@example.com",9934567876,"789 street",750)
customer_instance1.print_info()
customer_instance2.print_info()
customer_instance3.print_info()


# In[ ]:




