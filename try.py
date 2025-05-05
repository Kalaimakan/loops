
# User_Name = "Kalai"
# Password = "Kalai1510"
# max_attempts = 3
# attempts = 0

# while attempts < max_attempts:
#     user_name = input("Enter your User Name : ")
#     password = input("Enter your password : ")

#     if User_Name == user_name and Password == password:
#         print("-----Login Successful. You are Good to Go 😊-----")
#         break  # <-- This exits the loop when login is successful
#     else:
#         attempts += 1
#         left_attempts = max_attempts - attempts
#         if left_attempts > 0:
#             print(f"-----You Have Only {left_attempts} Attempts Left 🙁.-----")

# if attempts == max_attempts:
#     print("-----Too Many Failed attempts so exiting the program.-----")
#     print("-----Login Failed. Get out of Here 🤬🤬-----")

# 01.Build a Login System with Maximum Retry Limit
user_name="Kalai06"
password="Kalai2027"
maximum_attempts=3
attempts=0

while attempts<maximum_attempts:
    User_Name=input("Enter User Name : ")
    Password=input("Enter your Password : ")

    if user_name==User_Name and password==Password:
        print("-----you can go now 😊. login successfilly-----")
        break
    else:
        # attempts=attempts+1
        attempts+=1
        balance_attempts=maximum_attempts-attempts
        print(f'-----you have {balance_attempts} attempts left-----')
        
        if balance_attempts==0:
            print("-----Login Failed. Get out of Here 🤬🤬-----")
            print("-----Too many failed attempts 😡. Exiting program-----")
            exit()
    continue
    


# 02.Implement a Menu Loop Using while True
balance=1000
while True:
    print("----------What Do you Want ?----------")
    print("01.Check Balance.")
    print("02.Withdraw Money.")
    print("03.Deposit Money.")
    print("04.View All Accounts.")
    print("05.Exit.")

    choose=int(input("choose betwen 1 to 5) : "))
    if choose==1:
        print(f'--------Your curent Balance is Rs.{balance}.00')
    
    elif choose==2:
        Withraw_money=int(input("Enter the amount you want to Withraw : "))
        # if Withraw_money>balance:
        #     print("-------invalid Amount.--------")
        # else:
        #     new_balance=balance-Withraw_money
        if Withraw_money<=balance:
            balance-=Withraw_money
            print(f"-----Withdrawal successful. Your Current Balance is Rs.{balance}.00-----")
        else:
            print("-----Insufficient funds 😟-----")
   
    elif choose==3:
        deposit_money=int(input("Enter the amount you want to Deposit : "))
        balance=balance+deposit_money
        print(f'Your curent Balance is Rs.{balance}.00')
    
    elif choose==4:
        Account_list=[1000, 1500, 800]
        for i in range(len(Account_list)):
            print(f"Account 0{i+1} : ${Account_list[i]}")
    
    elif choose==5:
        print("-------Thankyou and come Again 😊-------")
        exit()
    
    else:
        print("--------I already Told you choose the number between 1 to 5 🤬--------")
