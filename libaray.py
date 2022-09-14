from secrets import choice
import pymysql
con=pymysql.connect(host="localhost",user="root",passwd="246810",database="library")

def main():
    print('''               
                                          LIBRARY MANAGEMENT
                                
    1.ADD BOOKS
    2.ISSUE BOOKS
    3.SUBMIT BOOKS
    4.DELETE BOOKS
    5.DISPLAY BOOKS                                    
         ''')

    choice = input('Enter Task No.: ')
    print(">----------------------------------------------------------------------------<")
    if(choice =='1'):
        addbook()
    elif(choice=='2'):
        issueb()
    elif(choice =='3'):
        submitb()
    elif(choice =='4'):
        dbook()
    elif(choice =='5'):
        dispbook()
    else:
        print("wrong choice...")   

def addbook():
    bn=input("Enter the Books Name: ")
    c=input("Enter the Books Code: ")
    t=input("Total Books: ")
    s=input("Enter Books: ")
    data= (bn,c,t,s)
    sql="insert into books values(%s,%s,%s,%s)"
    c=con.cursor()
    c.execute(sql,data)
    con.commit()
    print(">---------------------------------------------------------------------<")
    print("Data Entered Successfully")
    main()

def issueb():
    n=input("Enter Name: ")
    r=input("Enter Reg No: ") 
    co=input("Enter Books Code: ")
    d=input("Enter Date: ")
    a="insert into issue Values(%s,%s,%s,%s)"   
    data=(n,r,co,d)
    c=con.cursor()
    c.execute(a,data)
    con.commit()
    print(">----------------------------------------------------------------------<")
    print("Books issued to: ",n)
    bookup(co,-1)

def submitb():
    n=input("Enter Name: ")
    r=input("Enter Reg No: ") 
    co=input("Enter Books Code: ")
    d=input("Enter Date: ")
    a="insert into submit Values(%s,%s,%s,%s)"   
    data=(n,r,co,d)
    c=con.cursor()
    c.execute(a,data)
    con.commit()
    print(">----------------------------------------------------------------------<")
    print("Books submitted to: ",n) 
    bookup(co,1)   

def bookup(co,u):
    a='select Total from books where BCODE = %s'
    data=(co,)
    c=con.cursor()
    c.execute(a,data)
    myresult=c.fetchone()
    t=myresult[0]+u
    sql="update books set TOTAL = %s where BCODE = %s"
    d=(t,co)
    c.execute(sql,d)
    con.commit()
    main()

def dbook():
    ac=input("Enter Book Code: ")
    a="delete from books where BCODE = %s" 
    data=(ac,)
    c=con.cursor()
    c.execute(a,data)
    con.commit() 
    main() 

def dispbook():
    a="select * from books"
    c=con.cursor()
    c.execute(a)
    myresult=c.fetchall()
    for i in myresult:
        print("Books Name :",i[0])
        print("Books code: ",i[1])
        print("Total: ",i[2])
        print(">------------------------------------------<")
    main()    


def pswd():
    p=input("Password: ")
    if p == "itvedant":
        main()
    else:
        print("Wrong password: ")
        pswd()
pswd()                  