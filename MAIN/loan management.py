#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from ENTITY.Customer import Customer
from ENTITY.Loan import Loan
from ENTITY.HomeLoan import HomeLoan
from ENTITY.CarLoan import CarLoan
from DAO.ApplyLoan import loan_apply
from DAO.CalculateInterest import calculateinterest
from DAO.CalculateEMI import calculateEMI
from DAO.LoanStatus import loanstatus
from DAO.LoanRepayment import loanRepayment
from DAO.GetByLoanId import getByLoanId
from DAO.GetAllLoan import getAllLoan
from Exception.InvalidLoanException import InvalidLoanException
import math

class LoanManagement:
    def _init_(self):
        self.ApplyLoan = loan_apply()
        self.CalculateInterest = calculateinterest()
        self.CalculateEMI = calculateEMI()
        self.LoanStatus = loanstatus()
        self.LoanRepayment = loanRepayment()
        self.GetByLoanId = getByLoanId()
        self.GetAllLoan= getAllLoan()

    def display_menu(self):
        print("\nLoan Management System Menu:")
        print("1. Apply for a Loan")
        print("2. Calculate Insterst")
        print("3. Calculate EMI")
        print("4. Loan Status")
        print("5. Loan Repayment")
        print("6. Get Loan by ID")
        print("7. Get All Loan")
        print("8. Exit")

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
        
    def loanstatus(self):
        if self.customer.credit_score > 650:
            self.loan_status = "Approved"
            print("Loan Approved!")
        else:
            self.loan_status = "Rejected"
            print("Loan Rejected.")
            
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
        
    def getAllLoan(loans):
        for loan in loans:
            print(f"Loan ID: {loan.loan_id}, Principal Amount: {loan.principal_amt}, Interest Rate: {loan.interest_rate}%, Loan Term: {loan.loan_term} months, Loan Type:{loan.loan_type}, Loan Status: {loan.loan_status}")

    def getLoanById(self,loan_id):
        for loan in all_loans:
            if loan.loan_id == loan_id:
                print(f"Loan ID: {loan.loan_id}, Principal Amount: {loan.principal_amt}, Interest Rate: {loan.interest_rate}%, Loan Term: {loan.loan_term} months, Loan Type:{loan.loan_type}, Loan Status: {loan.loan_status}")
                return
        raise InvalidLoanException(f"LoanID {loan_id} not found.")
        

    def main(self):
        while True:
            self.display_menu()
            choice = input("Enter your choice: ")

            if choice == "1":
                self.loan_apply()
            elif choice == "2":
                self.calculateinterest()
            elif choice == "3":
                self.calculateEMI()
            elif choice == "4":
                self.loanstatus()
            elif choice == "5":
                self.loanRepayment()
            elif choice == "6":
                self.getAllLoan()
            elif choice == "7":
                self.getByLoanId()
            elif choice == "8":
                print("Exiting Loan Management System.")
                break
            else:
                print("Invalid choice. Please enter a valid option.")

if _name_ == "_main_":
    loan_management = LoanManagement()
    loan_management.main()

