#!/usr/bin/env python
# coding: utf-8

# In[1]:


class Loan:
    def loan_apply(self, loan_type):
        user_confirmation = input(f"Do you want to apply for a {loan_type} loan? (yes/no): ")

        if user_confirmation.lower() == 'yes':
            print(f"{loan_type} Loan Applied successfully!")

            if loan_type.lower() == 'car':
                car_model = input("Enter the car model you want to purchase: ")
                loan_amount = float(input("Enter the car loan amount you are applying for: "))
                print(f"Details:\nCar Model: {car_model}\nLoan Amount: ${loan_amount}")
            elif loan_type.lower() == 'home':
                property_type = input("Enter the type of property you want to purchase: ")
                loan_amount = float(input("Enter the home loan amount you are applying for: "))
                print(f"Details:\nProperty Type: {property_type}\nLoan Amount: ${loan_amount}")
            else:
                print("Invalid loan type.")
        else:
            print("Loan application cancelled.")

loan_type = input("Which type of loan would you like to apply for? (car/home): ")
loan = Loan()
loan.loan_apply(loan_type)


# In[ ]:




