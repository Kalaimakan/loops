# Build a Login System with Maximum Retry Limit
User_Name="Kalai"
Password="Kalai1510"
max_attempts=3
attempts=0

while attempts<max_attempts:
    user_name=input("Enter your User Name : ")
    password=input("Enter your password : ")

    if User_Name==user_name and Password==password:
        print("-----Login Successful. You are Good to Go 😊-----")
        break
    else:
        attempts=attempts+1
        left_attempts=max_attempts-attempts
        print(f"-----You Have Only {left_attempts} Attempts Left 🙁.-----")
        
        if attempts==max_attempts:
            print("-----Login Failed. Get out of Here 🤬🤬-----")
            print("-----Tooo Many Failed attempts so exiting the program.-----")
            exit()
    continue

#============================git testing===========================    

# Implement a Menu Loop Using while True

balance=100000
while True:
    print(f"-----Welcome,🫡-----")
    print("01.Check Balance.")
    print("02.Withdraw.")
    print("03.Deposit")
    print("04.View All Account.")
    print("05.Exit")

    choose=int(input("Choose a Number between 1 to 5 : "))

    if choose==1:
        print(f"-----Your Balance is Rs.{balance}.00------")
        
    elif choose==2:
        Withdraw_Amount=int(input("Enter The Withdraw Amount : "))
        if Withdraw_Amount<=balance:
            balance-=Withdraw_Amount
            print(f"-----Withdrawal successful. Your Current Balance isRs.{balance}.00-----")
        else:
            print("-----Insufficient funds 😟-----")
        
    elif choose==3:
        Deposit_Amount=int(input("Enter Your Deposit Amount : "))
        if Deposit_Amount>=0:
            balance+=Deposit_Amount
            print(f"------Deposit Successful. Your Current Balance is Rs.{balance}.00-----")
        else:
            print("-----Invaild Amount 😟. Please Enter The correct Amount.-----")
            
    elif choose==4:
        Account_list=[1000,1500,800]
        for i in range(len(Account_list)):
            print(f"Account 0{i+1} : ${Account_list[i]}")
        
    elif choose==5:
        print("-----Thankyou for Using the ATM 🫡.------")
        exit()
    else:
        print("--------I already Told you choose the number between 1 to 5 🤬--------")