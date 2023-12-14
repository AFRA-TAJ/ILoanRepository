#!/usr/bin/env python
# coding: utf-8

# In[5]:


from entity import Loan
class HomeLoan(Loan):
    def __init__(self,loan_id,customer,principal_amt,interest_rate,loan_term,loan_type,loan_status,property_address,property_value):
        super().__init__(loan_id,customer,principal_amt,interest_rate,loan_term,"HomeLoan",loan_status)
        self.property_address=property_address
        self.property_value=property_value
        
    def get_property_address(self):
        return self.property_address
    def get_property_value(self):
        return self.property_value
    
    def set_property_address(self):
        self.property_address=property_address
    def set_property_value(self):
        self.property_value=property_value
        
    def print_info(self):
        super().print_info()
        print(f"Property Address:{self.property_address}")
        print(f"Property Value:{self.property_value}")
homeloan_instance1=HomeLoan(1,"abi",30000,0.5,12,"HomeLoan","Pending","123 main street",5500000) 
homeloan_instance2=HomeLoan(2,"eve",40000,0.5,24,"HomeLoan","Approved","323 main street",5000000) 
homeloan_instance3=HomeLoan(3,"josh",50000,0.5,6,"HomeLoan","Pending","67 main street",7500000) 
homeloan_instance1.print_info()
homeloan_instance2.print_info()
homeloan_instance3.print_info()


# In[ ]:





# In[ ]:




