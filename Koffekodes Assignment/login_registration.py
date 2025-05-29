#Login and Registration logic 

#1. name, phone number, email
#2. generate otp and verify

import random

class login_registration():
    def __init__(self, name, ph_number,email):
        self.name = name
        self.ph_number = ph_number
        self.email = email
        self.otp = None
        self.verified = False

    def gen_otp(self):
        self.otp = random.randint(1000, 9999)
        return self.otp
    
    def otp_verification(self,otp):
        if otp == self.otp:
            self.verified = True
            return True
        else:
            return False
        
    def registration(self):
        print("Registration successfull")
        print(f"Name: {self.name}, Phone number: {self.ph_number}, Email: {self.email}")

    def login(self):
        if self.verified:
            print("Login successfull")
        else:
            print("Login Unsuccessful")
                
def main_run_function():
    name = input("Enter name: ")
    ph_number = input("Enter phone number: ")
    email = input('Enter email id: ')
    user = login_registration(name, ph_number, email)
    
    otp = user.gen_otp()
    print(f"OTP is {otp}")
    otp_input = int(input("Enter OTP: "))
    if user.otp_verification(otp_input):
        user.login()
        user.registration()
    else:
        print("Invalid OTP")

main_run_function()

















