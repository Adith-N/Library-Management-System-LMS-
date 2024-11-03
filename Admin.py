import mysql.connector as ms
import random as r
def clear():
    for i in range(10):
        print()
o=0
db=ms.connect(host='localhost',user='root',passwd='Ammu2013',database='lms')
print(db)
csr=db.cursor()
rat=[0.0,0.1,0.2,0.3,0.4,1.0,1.1,1.2,1.3,1.4,1.5,2.0,2.1,2.2,2.3,2.4,3.0,
            3.1,3.2,3.3,3.4,4.0,4.1,4.2,4.3,4.4,5.0]
def BookInserter():
    clear()
    a=input("Enter Name Of Book: ")
    genre=input("Enter Genre: ")
    global rat
    try:
        v=r.randrange(0,len(rat))
        sql="insert ignore into Books(Title, genre, rating) values(%s,%s,%s)"
        values=(a,genre,rat[v])
        csr.execute(sql,values)
        db.commit()
    except Exception as x:
        print(x)


def BookRemove():
    clear()
    B=input("Book To Remove: ")
    try:
        print("Do you want to remove book "+B+" from database?")
        cnf2=input("(Y/N)-")
        if cnf2=="Y":
            q="'"+B+"'"
            sql="delete from books where Title="+q
            csr.execute(sql)
            db.commit()
        else:
            pass
    except Exception as pp:
        print(pp)

def adminmenu():
    clear()
    print("Admin Menu")
    print("1) Add Book")
    print("2) Remove Book")
    print("3) Exit")
    cx=int(input("Enter Choice: "))
    if cx==1:
        BookInserter()
        adminmenu()
    elif cx==2:
        BookRemove()
        adminmenu()
    elif cx==3:
        quit()
    else:
        print("Incorrect Choice")
        adminmenu()
            
        
