import mysql.connector as m
import time as t
import lib as l
pc=[]
t1=['The Godfather','The Da Vinci Code', 'Hunger Games']
try:
    con=m.connect(user='root',host='localhost',password='Ammu2013',database='lms')
    cur=con.cursor()
except Exception as e:
    print(e)
def clear():
    for i in range(10):
        print()
def u():
    print("[**Note that this is a one time process after each login]")
    global user
    user=input("Enter Username: ")
#Main Menu
def mainmenu():
    global cur
    o=0
    clear()
    c=1
    while c!=7:
        print('\t  +---------------------------------------------------------------------+')
        t.sleep(0.3)
        print('\t  |                    AMRITA VIDYALAYAM LIBRARY MANAGER                |')
        t.sleep(0.2)
        print('\t  |                                                                     |')
        t.sleep(0.2)
        print('\t  |                         1) BORROW A BOOK                            |')
        t.sleep(0.2)
        print('\t  |                         2) RETURN A BOOK                            |')
        t.sleep(0.2)
        print('\t  |                         3) LIBRARY TODAY                            |')
        t.sleep(0.2)
        print('\t  |                         4) SUPPORT                                  |')
        t.sleep(0.2)
        print('\t  |                         5) EXIT                                     |')
        t.sleep(0.3)
        print('\t  +---------------------------------------------------------------------+')
        c=7
    t.sleep(1)
    ch=str(input("Enter Choice (1?,2?,3?,4?,5?,6?): "))

    while o==0:
        if ch=='1':
            clear()
            o=1
            g1 = [
    'Romance',
    'MysteryThriller',
    'ScienceFictionFantasy',
    'SelfHelp'
]
            g2 = [
    'YoungAdultYA',
    'NonFiction',
    'HistoricalFiction',
]
            g3 = [
    'Horror',
    'FantasyRomance',
    'LiteraryFiction'
]
            print('\t  +---------------------------------------------------------------------+')
            print('\t                              BORROW AN E BOOK                           ')
            print('\t                                   Genres:                               ')
            cur.execute('select genre from books group by genre')
            result=cur.fetchall()
            for i in result:
                print("                                   ",i, sep=' ')
                t.sleep(0.08)
            print('\t  +---------------------------------------------------------------------+')
            t.sleep(0.2)
            print("[#To Exit Type 'Exit']")
            print()
            u=input("Specify Your Genre: ")
            if u == "Exit":
                f.close()
                mainmenu()
            cur.execute("select * from books where genre=%s",(u,))
            result = cur.fetchall()
            for i in result:
                print(i)
                print()
            try:
                table="CREATE TABLE IF NOT EXISTS "+user+"(title varchar(50) primary key, genre varchar(50) not null)"
                cur.execute(table)
                title=input("Title Of Book You Want To Borrow: ")
                c=str(input("Confirm Checkout (Alloted Time 1 Week) (Y/N)?: "))
                c=c.upper()
                if c=='Y' or c=='YES':
                    sql="Insert into "+user+" values('{}','{}')".format(title, u)
                    cur.execute(sql)
                    con.commit()
                    cur.execute("select * from "+user)
                    result = cur.fetchall()
                    clear()
                    print("\t                                    CART")
                    for i in result:
                        print('\t  +---------------------------------------------------------------------+')
                        t.sleep(0.05)
                        print("\t                         ",i)
                        t.sleep(0.05)
                        print('\t  +---------------------------------------------------------------------+')
                    t.sleep(1)
                    mainmenu()
                else:
                    print("Checkout Cancelled")
                    t.sleep(1)
                    mainmenu()
            except Exception as e:
                print(e)
                mainmenu()
                    
            
        elif ch=='2':
            o=1
            table="CREATE TABLE IF NOT EXISTS "+user+"(title varchar(50) primary key, genre varchar(50) not null)"
            cur.execute(table)
            clear()
            print('\t  +---------------------------------------------------------------------+')
            print('\t                              RETURN AN E BOOK                           ')
            print("\t                                    CART")
            cur.execute("select * from "+user)
            result = cur.fetchall()
            for i in result:
                print('\t  +---------------------------------------------------------------------+')
                t.sleep(0.05)
                print("\t  ",i)
                t.sleep(0.05)
                print('\t  +---------------------------------------------------------------------+')
            t.sleep(1)
            print("[#To Exit Type 'Exit']")
            print()
            b=input("Return Cart?: ")
            if b == "Exit":
                quit()
            b=b.upper()
            if b=='Y' or b=='YES':
                b=int(input("If Extra Time Taken Specify (Days): "))
                global pc
                pc+=[b*20]
                c=input("Confirm Return (Y/N)?: ")
                cur.execute("drop table "+user)
                print("Pending Charges =",pc)
                t.sleep(1)
                clear()
                mainmenu()
            else:
                print("Return Cancelled")
                t.sleep(0.5)
                clear()
                
                mainmenu()
        elif ch=='3':
            o=1
            liba()
            
        elif ch=='4':
            o=1
            clear()
            print('\t  +------------------------------------------------------------------------+')
            t.sleep(0.2)
            print('\t  |                              ONLINE SUPPORT                            |')
            t.sleep(0.2)
            print('\t  |                                                                        |')
            t.sleep(0.2)
            print('\t  |                         1)Youtube  - Support Link?                     |')
            t.sleep(0.2)
            print('\t  |                         2)Discord  - Support Link?                     |')
            t.sleep(0.2)
            print('\t  |                         3)Facebook - Support Link?                     |')
            t.sleep(0.2)
            print('\t  |                         4)Whatsapp - Support Link?                     |')
            t.sleep(0.2)
            print('\t  |                         5)EXIT?                                        |')
            t.sleep(0.2)
            print('\t  |                                                                        |')
            t.sleep(0.2)
            print('\t  +------------------------------------------------------------------------+')
            t.sleep(1)
            while True:
                ch=str(input("Enter Choice (1?,2?,3?,4?,5?): "))
                if ch=='1':
                    clear()
                    print('\t  +---------------------------------------------------------------------+')
                    print('\t  |                        https://www.youtube.com                      |')
                    print('\t  +---------------------------------------------------------------------+')
                    t.sleep(3)
                    mainmenu()
                if ch=='2':
                    clear()
                    print('\t  +---------------------------------------------------------------------+')
                    print('\t  |                     https://discord.gg/qVUmTZNsTJ                   |')
                    print('\t  +---------------------------------------------------------------------+')
                    t.sleep(3)
                    mainmenu()
                if ch=='3':
                    clear()
                    print('\t  +---------------------------------------------------------------------+')
                    print('\t  |                        https://www.facebook.com                     |')
                    print('\t  +---------------------------------------------------------------------+')
                    t.sleep(3)
                    mainmenu()
                if ch=='4':
                    clear()
                    print('\t  +---------------------------------------------------------------------+')
                    print('\t  |                        https://www.whatsapp.com                     |')
                    print('\t  +---------------------------------------------------------------------+')
                    t.sleep(3)
                    mainmenu()
                if ch=='5':
                    print("\t\t\t Hope Your Problem Was Solved")
                    t.sleep(1)
                    exit()
            else:
                print("\t\t\t Incorrect Input")
                mainmenu()
            
        elif ch=='5':
            o=1
            p=input("Are you sure you want to exit? (Y/N): ")
            p=p.upper()
            if p=='Y' or p=='YES':
                quit()
        else:
            print("Incorrect Choice |RETYPE|")
            ch=int(input("Enter Choice (1?,2?,3?,4?,5?,6?): "))

def liba():
            clear()
            print('\t  +------------------------------------------------------------------------+')
            t.sleep(0.2)
            print('\t  |                              LIBRARY TODAY                             |')
            t.sleep(0.2)
            print('\t  |                                                                        |')
            t.sleep(0.2)
            print('\t  |                         1)NEWS TODAY - FRESH OUT THE OVEN              |')
            t.sleep(0.2)
            print('\t  |                         2)FROM THE CREATORS DESK                       |')
            t.sleep(0.2)
            print('\t  |                         3)MOST POPULAR BOOKS                           |')
            t.sleep(0.2)
            print('\t  |                         4)MAIN MENU?                                   |')
            t.sleep(0.2)
            print('\t  |                                                                        |')
            t.sleep(0.2)
            print('\t  +------------------------------------------------------------------------+')
            while True:
                t.sleep(0.7)
                print()
                print()
                print()
                ch=str(input("Enter Choice (1?,2?,3?,4?,5?): "))
                if ch=='1':
                    print('Presenting the top headlines today from our news partner "BBC"')
                    print()
                    print()
                    print()
                    l.NewsFromBBC()
                elif ch=='2':
                    clear()
                    f=open('cd.txt','r')
                    st=f.readlines()
                    for i in st:
                        print(i)
                        t.sleep(1.1)
                elif ch=='3':
                    print('TOP BOOKS TODAY: ',t1)
                elif ch=='4':
                    mainmenu()
                else:
                    print('INCORRECT CHOICE |PLEASE RETRY|')
                    mainmenu()
'''=====TEMP FIELD====='''
user='Keyston'
