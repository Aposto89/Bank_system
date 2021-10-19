# This is bank account management system.
# Please update the connecting data: host, user, password and database

import mysql.connector
mydb = mysql.connector.connect(host="localhost", user="root", password="type your password", database="new_bank")

def openAcc():

    n = input("Enter account holder: ")
    ac = input("Enter the account No: ")
    db = input("Enter the date of birth (yyyy-mm-dd): ")
    add = input("Enter the address: ")
    cn = 'wrong'
    while cn.isdigit() == False:
      cn = input("Enter the contact number: ")
      if cn.isdigit() == False:
        print("Sorry, but you did not enter an integer. Please try again.")
    ob = 'wrong'
    while ob.isdigit() == False:
        ob = input("Enter the opening balance: ")
        if ob.isdigit() == False:
            print("Sorry, but you did not enter an amount. Please try again.")
    data1 = (n, ac, db, add, cn, ob)
    data2 = (n, ac, ob)
    sql1 = 'insert into accounts values (%s, %s, %s, %s, %s, %s)'
    sql2 = 'insert into amount values (%s, %s, %s)'
    x = mydb.cursor()
    x.execute(sql1, data1)
    x.execute(sql2, data2)
    mydb.commit()
    print("Data entered successfully..")
    main()

def despoAmo():
    amount_str = 'wrong'
    while amount_str.isdigit() == False:
        amount_str = input("Enter the amount you want to deposit: ")

        if amount_str.isdigit() == False:
            print("Sorry, but you did not enter an amount. Please try again.")
    amount = int(amount_str)
    ac = input("Enter the Account number: ")
    a = 'select balance from amount where Acc_number=%s'
    data = (ac,)
    x = mydb.cursor()
    x.execute(a, data)
    result = x.fetchone()
    t = result[0]+amount
    sql3 = 'update amount set balance=%s where Acc_number = %s'
    d = (t,ac)
    x.execute(sql3,d)
    mydb.commit()
    print("The amount was deposited successfully ..")
    main()

def withdrAwamount():
    amount_str = 'wrong'
    while amount_str.isdigit() == False:
        amount_str = input("Enter the amount you want to deposit: ")

        if amount_str.isdigit() == False:
            print("Sorry, but you did not enter an amount. Please try again.")
    amount = int(amount_str)
    ac = input("Enter the account number: ")
    a = 'select balance from amount where Acc_number=%s'
    data = (ac,)
    x = mydb.cursor()
    x.execute(a, data)
    result = x.fetchone()
    t = result[0] - amount
    sql3 = 'update amount set balance=%s where Acc_number = %s'
    d = (t, ac)
    x.execute(sql3, d)
    mydb.commit()
    print("The amount was withdraw successfully ..")
    main()

def balEnq():
    ac = input("Enter the account number: ")
    a = 'select * from amount where Acc_number = %s'
    data=(ac,)
    x = mydb.cursor()
    x.execute(a, data)
    result = x.fetchone()
    print("Balance for account:",ac,"is",result[-1])
    main()

def disDetails():
    ac = input("Enter the account number: ")
    a = 'select * from amount where Acc_number = %s'
    data = (ac,)
    x = mydb.cursor()
    x.execute(a, data)
    result = x.fetchone()
    for i in result:
        print(i)
    main()

def closeAcc():
    ac = input("Enter the account number: ")
    sql1 = 'delete from accounts where Acc_number = %s'
    sql2 = 'delete from amount where Acc_number = %s'
    data = (ac,)
    x = mydb.cursor()
    x.execute(sql1,data)
    x.execute(sql2,data)
    mydb.commit()
    print("The account was closed..")
    main()




def main():
    print('''
 ******************************************
 ** THIS IS A SIMPLE BANK ACCOUNT SYSTEM ** 
 ******************************************
 
    1. OPEN NEW ACCOUNT
    2. DEPOSIT AMOUNT
    3. WITHDRAW AMOUNT
    4. BALANCE ENQUIRY
    5. DISPLAY CUSTOMER DETAILS
    6. CLOSE ACCOUNT''')


    choice = 'WRONG'
    within_range = False

    while choice.isdigit() == False or within_range == False:
      choice = input("\nEnter the task number you want to perform (1-6): ")
      if choice.isdigit() == False:
        print("Sorry, but you did not enter an integer. Please try again.")
      elif choice.isdigit() == True:
          if int(choice) in range(0, 7):
              within_range = True
          else:
              within_range = False
    if choice == '1':
      openAcc()
    elif choice == '2':
      despoAmo()
    elif choice == '3':
      withdrAwamount()
    elif choice == '4':
      balEnq()
    elif choice == '5':
      disDetails()
    elif choice == '6':
      closeAcc()
    else:
      print("Invalid Choice")
      main()
main()
