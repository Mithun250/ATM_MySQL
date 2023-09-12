import mysql.connector
from datetime import datetime

mithun=mysql.connector.connect(host='localhost',user='root',password='Nuhtim25*',database='atm')
suresh=mithun.cursor()
# suresh.execute("create table atm_data( Account_ID int primary key, Name varchar(30), Age int, Email varchar(20),Phone_Number int, Balance float) ")
# mithun.commit()

# suresh.execute("""INSERT INTO atm_data VALUES (12345678, 'Mithun', 21, 'mithun25@mail.com', 918277734, 60000),    
#     (23456789, 'John', 28, 'john@example.com', 987654321, 75000),
#     (34567890, 'Emily', 24, 'emily@testmail.com', 876542109, 55000),
#     (45678901, 'Sarah', 32, 'sarah@example.com', 765431098, 90000),
#     (56789012, 'David', 22, 'david@testmail.com', 654210987, 62000),
#     (67890123, 'Lisa', 27, 'lisa@example.com', 543219876, 72000),
#     (78901234, 'Michael', 31, 'michael@testmail.com', 421098765, 85000),
#     (89012345, 'Jessica', 29, 'jessica@example.com', 310987654, 68000),
#     (90123456, 'Alex', 26, 'alex@testmail.com', 210986543, 58000),
#     (12345098, 'Sophia', 25, 'sophia@example.com', 18765432, 64000)""")
# mithun.commit()


# suresh.execute("create table audit_data( Account_ID int, Name varchar(30),Phone_Number int , Withdraw_Amount int, Withdraw_Datetime TIMESTAMP,Before_ACC_Balance float, After_withdraw_Balance float) ")

# mithun.commit()

def withdraw(account_id,amount):
    suresh.execute("select * from atm_data where Account_ID= %s",(account_id,))
    account=suresh.fetchone()

    if account:
        if account[5]>=amount:
            new_balance=account[5]-amount
            update_balance = "Update atm_data SET Balance = %s Where Account_ID = %s"
            suresh.execute(update_balance,(new_balance,account_id))
            mithun.commit()
            
            audit="insert into audit_data (Account_ID, Name, Phone_Number, Withdraw_Amount, Withdraw_Datetime,Before_ACC_Balance,After_withdraw_Balance) values(%s,%s,%s,%s,%s,%s,%s)"
            audit_data=(account_id,account[1],account[4],amount,datetime.now(),account[5],new_balance)
            suresh.execute(audit,audit_data)
            mithun.commit()

            print("Withdraw Successfull")
        else:
            print("Insufficient Balance")
    else:
        print("Account was not Found")
    

account_id=int(input("Enter the Account ID: "))
amount=int(input("Enter the withdraw amount: "))

withdraw(account_id,amount)

