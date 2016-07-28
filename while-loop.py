name = raw_input("What is your UserName: ")
password = raw_input("What is your Password: ")
input1 = None
input2 = None
while input1 != name:
    input1 = raw_input("please enter your currenr username : ")
while input2 != password:
    input2 = raw_input("please enter your current password: ")
print("Welcome back to your system!")

