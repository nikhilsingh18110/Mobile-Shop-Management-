import os
import platform
import mysql.connector as sql
import datetime as dt

#==========================Mobile Shop===========================

print('_____________________________________WELCOME TO MOBILE SHOP__\
________________________')
mydb=sql.connect(host='localhost', user='root', passwd='root')

#=========================Stock Modification==============================

def smod():
    mydb=sql.connect(host='localhost', user='root', passwd='root', database='mobile_shop1')
    print("\t1.To Change Mobile Name\n\t2.To Change Unit Price\n\t3.Quit")
    print()
    modc=int(input("\tEnter Your Choice : "))
    if modc==1:
        name=input("\t\tEnter Current Name : ")
        mname=input("\t\tEnter New Name : ")
        cursor=mydb.cursor()
        sq="""update mobile set name=%s where name=%s"""
        val=(mname, name)
        cursor.execute(sq, val)
        mydb.commit()
        print("\n\n")
        print("\t\tOne Record Modified")
        print("\n\n")
        sdetail()
    elif modc==2:
        up=int(input("\t\tEnter Current Unit Price : "))
        mup=int(input("\t\tEnter New Unit Price : "))
        cursor=mydb.cursor()
        sq="""update mobile set unit_price=%s where unit_price=%s"""
        val=(up, mup)
        cursor.execute(sq, val)
        mydb.commit()
        print("\n\n")
        print("\t\tOne Record Modified")
        print("\n\n")
        sdetail()
    else:
        print("\n\n")
        main_menu()
    
#=========================Customer Modification==========================

def cmod():
    mydb=sql.connect(host='localhost', user='root', passwd='root', database='mobile_shop')
    print("\t\1.Change Customer Name")
    bn=input("\t\tEnter Customer Bill Number : ")
    name=input("\t\tEnter Name : ")
    cursor=mydb.cursor()
    sq="""update user set Cname=%s where bill_no=%s"""
    val=(name, bn)
    cursor.execute(sq, val)
    mydb.commit()
    print("\n\n")
    print("\tOne Record Modified")
    print("\n\n")
    cdetail()
    

#=============================Buy Product============================    
    
def customer():
    mydb=sql.connect(host='localhost', user='root', passwd='root', database='mobile_shop')
    name=input('\t\tPlease Enter Your Name : ')
    print('\n\t\tThank you for visting Our store')
    print('\t\t---Select Mobile Brand which you want to Buy----')
    print()

    #===========Selecting Of Brand=============
    
    b=input('\t\tEnter Brand Name : ')
    
    
    
    val=b.lower()
    mycursor=mydb.cursor()
    sq="""select * from mobile"""
    mycursor.execute(sq)
            
    result=mycursor.fetchall()
    
    for (Item_code,Model_No,Brand,Name,Unit_price,Quantity) in result:
        if Brand.lower()==val:

            #==========Buying Of Mobile if Brand Is Available==============

            cursor=mydb.cursor()
            sm="""select * from mobile where brand=%s"""
            cursor.execute(sm, (val,))
            result1=cursor.fetchall()
            print("\t\t", "="*80)
            print()
            print("\t\tItem Code\t    Model Number\t    \tBrand\t\t    Name\t\t    Unit Price\t    Quantity\t")
            print("\t\t", "_"*80)
            for (Ic,Mn,Br,Na,Up,Qu) in result1:
                print("\t\t", Ic, "\t\t    ", Mn, "\t\t    ", Br,  " \t    ", Na, " \t\t    ",\
                  Up, "\t\t    ", Qu)
            print()
            print("\t\t", "="*80)    
                    
            print("\t", "_"*80)
            print()
            print('     Do You want to select from above Mobiles   (Y/N)')
            ch=input('Enter Your Choice :')
            if ch=='Y' or ch=='y':

                print('Which Model you Want')
                ch1=input('Enter Model Name : ')
                ch1=ch1.lower()
                
                #  ========Checking Availability In Stocks============
                cursor=mydb.cursor()
                sql001="""select * from mobile where name=%s"""
                cursor.execute(sql001, (ch1,))
                Icode=0
                Q=0
                myresult=cursor.fetchall()
                for (Item_code,Model_No,Brand,Name,Unit_price,Quantity) in myresult:
                    Q=Quantity
                    Icode=Item_code 

                if Q==0:
                    print("\t\tSorry Your Select Phone is Not Available Now\n")
                    prin("\t\tPlease Share Your Number To Get Info When this Phone is in Stock")
                    number=int("\t\tEnter Your Number Here : ")
                    sql011="""delete from mobile where name=%s"""
                    cursor.execute(sql011, (ch1,))
                    mydb.commit()

                    #==============Reducing Item Code due Lack of Stock================
                    
                    sql012="""update mobile set item_code=item_code-1 where item_code>%s"""
                    cursor.execute(sql012, (Icode,))
                    mydb.commit()


                    # ================= Buying of Mobile if It is Available================

                    
                else:    
                    ch2=(ch1,)
                    sq0='select * from mobile where name=%s'
                    cursor=mydb.cursor()
                    cursor.execute(sq0,ch2)
                    result=cursor.fetchall()
                    for (Item_code,Model_No,Brand,Name,Unit_price,Quantity) in result:
                        print('Price of Selected Phone : ', Unit_price)
        
                    print()
                    print()
                    print()
                    print('Do you want to Buy (Y/N)')
                    ch2=input('Enter your Choice : ')
            
                    if ch2=='y' or ch2=='Y':

                        #===========Selecting Payment Method==============
                         
                            print()
                            print()
                            print('Select Payment Mode')
                            print('    1.Cash\n    2.Credit Card\n    3.Debit card')
                            ch3=int(input('Enter your choice Number :'))
                            print()
                            print()
                            if ch3==1:
                                print('Thank you,  Please make Payment')
                            elif ch3==2 or ch3==3:
                                print('Please Enter your Card Details')
                                cn=int(input('Enter your Card Nmber :'))
                                cvv=int(input('Enter CVV :'))
                            print('Thank you for buying Phone\n Please Visit Again')
                
                            sq01="""insert into user (Cname, Mobile_name, Bill_Amount, Bill_no, D_O_P, Warranty)\
                                  values(%s, %s, %s, %s, %s, %s)"""

                            bn=1000   
                            cursor=mydb.cursor()
                            cursor.execute("select * from user")
                            result=cursor.fetchall()
                            for (Cname, mname, bamt, id, dop, warnty) in result:
                                bn=id
                            
                            #=========Creating Bill Number==========
                          
                            nbn=bn+1
                            print("\t Your Bill Number : ", nbn)

                            #==========Selecting Buying Date And Warranty Date======
                        
                            x = dt.date.today()
                            y = dt.date.today()+dt.timedelta(days=365)
                    

                            val=(name, ch1, Unit_price, nbn, x, y)
                            mycursor=mydb.cursor()
                  
                         
                            mycursor.execute(sq01, val)
                            mydb.commit()

                            # =========== Reducing Mobile Quantity In Stock Table===========

                            sq1="""update mobile set quantity=quantity-1 where brand=%s and name=%s"""
                            val1=(b, ch1)
                            mycursor=mydb.cursor()
                
                
                            mycursor.execute(sq1, val1)
                            mydb.commit()

                            print()
                            main_menu()

                        

              
        else:
            print()
            print("\t\t", "_"*80)
            print()
            print("\t\t\tSorry We Don't Have That Brand\n")
             
            print("\t\t\tDo You Want To Select Brands : (Y/N)")   
              
            print()
            ab=input("\t\tEnter Your Choice : ")
            if ab=="Y" or ab=="y":
                print()
                print("_"*120)
                print()
                customer()
            else:
                print()
                print("\t\tSorry For This Inconviniance\n")
                print("\t\tThank You For Visiting This Please Visit Again")

                

                    
    
        
    
        
    
    
                
#====================================Owner Login=======================
def login():
    count=1
    mydb=sql.connect(host='localhost', user='root', passwd='root', database='mobile_shop')
    while(count<=3):
        user=input('\tEnter Login ID :')
        passwd=input("\tEntrer the Password : ")
        if user=='IPMS001' and passwd=='12345' :
            print()
        
            print('\n\t------Now You Can Access Your Account-------')
            print()
            print()
            print()
            print('\t\t1.Customer Details\n\t\t    2.Stock Details')
            print()
            och=int(input('\tEnter your Choice Number :'))
            if och==1:
                print()
                cdetail()
            elif och==2:
                print()
                sdetail()
            else:
                print("\n\n")
                print("\t____________________INVALID CHOICE_______________")
                print()
                main_menu()
            break    
        else:
             count=count+1
        
             print("\n\n")
            

        if count==4:
            print("\t_________________You Entered Wrong UserID or Password Maximum Time____\
                        ____________")
            print("\n\n\n")
            main_menu()
            
            
            
        
#===================================Main Menu=======================
def main_menu():
     mydb=sql.connect(host='localhost', user='root', passwd='root', database='mobile_shop')
     print('   \t\t1.SHOP OWNER \t   2.CUSTOMER\t    3.Quit')
     print()
     c=int(input('\t\t   Enter your Choice Number :'))
     if c==1:
         login()
     elif c==2:
         customer()
     elif c==3:
         quit()
     else:
         print("\t______________________Invalid Choice________________")
         quit()
#===================================Create Tables=========================
def create_table():
    try:
        mydb=sql.connect(host='localhost', user='root', passwd='root', database='mobile_shop')
        cursor=mydb.cursor()
        cursor.execute("create table mobile(Item_code int primary key, Model_No varchar(20),\
                                      Brand varchar(20), Name varchar(20), Unit_price int, Quantity int)")
        cursor.execute("create table user(Cname varchar(20), Mobile_name varchar(20), Bill_amount int, \
                                   Bill_No int primary key, D_O_P date, Warranty date)")
        mydb.close()
        main_menu()
    except:
        print('.................................  Please Continue')
        print()
        print("_"*80)
        print()
        main_menu()
#===================================Create Database============================
def create_database():
    mydb=sql.connect(host='localhost', user='root', passwd='root')
    try:
        cursor=mydb.cursor()
        cursor.execute("create database mobile_shop")
        mydb.close()
    except:
        create_table()

#=========================Delete  Stocks Details=========================
        
def delete():
    mydb=sql.connect(host='localhost', user='root', passwd='root', database='mobile_shop')
    print("\n\t 1.Delete By Item Code\n\t 2.Delete By Mobile Name\n\t 3.Back To Stock Detail")
    print("\n\n")
    och1=int(input('\t\tEnter Your Choice Number : '))
    if och1==1:

       #========Deleting Stocks By Item Code=========================
        
        moc=input("\n\t\tEnter Item Code : ")
        cursor=mydb.cursor()
        sq="""delete from mobile where Item_code=%s"""
        sq1="""select * from mobile where Item_code=%s"""
        cursor.execute(sq1, (moc,))
        result=cursor.fetchall()
        print("\t\t", "="*80)
        print()
        print("\t\tItem Code\t    Model Number\t    Brand\t\t    Name\t\t    Unit Price\t    Quantity\t")
        print("\t\t ", "_"*80)
        for (Item_code,Model_No,Brand,Name,Unit_price,Quantity) in result:
                    
                    
            print("\t\t", Item_code, "\t\t    ", Model_No, "\t\t    ", Brand,  " \t    ", Name, " \t\t    ", \
                       Unit_price, "\t\t    ", Quantity)
            print()
        print("\t\t", "="*80)    
                    
        print("\t", "_"*80)
        print()
        print("\t\tThis Record Will be Delete\n\t\t\
                     Do You Want to Delete : (Y/N)")
        j=input("\n\t\tEnter Your Choice : ")
        if j=='y' or j=="Y":
            
            cursor=mydb.cursor()
        
            cursor.execute(sq, (moc,))
            mydb.commit()
            print("\n\t\t1 Record Deleted")
            print('\n\n')
            print("\tDo You Want To Delete Other Recocrd : (Y?N)")
            print()
            w=input("\t\tEnter Your Choice : ")
            if w=='y' or w=='Y':
                print()
                delete()
            elif w=='n' or w=='N':
                print()
                
                print('\t1.Main Menu\t 2.Stock Detail')
                d=int(input("\t\tEnter Choice Number : "))
                if d==1:
                    main_menu()
                elif d==2:
                    sdetail()
                else:
                    main_menu()
        elif j=='n' or j=='N':
            print("\tDo you Want to Delete Another Record : (Y/N)")
            t=input("\t\tEntre Your Choice : ")
            if t=='y' or t=='Y':
                print()
                delete()
            elif t=='n' or t=='N':
                print()
                sdetail()
            else:
                main_menu()
            
    elif och1==2:

           #===========Deleting Stock By Mobile Name===========
        
            moc=input("\tEnter Mobile Name : ")
            cursor=mydb.cursor()
            sq="""delete from mobile where name=%s"""
            sq1="""select * from mobile where name=%s"""
            cursor.execute(sq1, (moc,))
            result=cursor.fetchall()
            print("\t\t", "="*80)
            print()
            print("                    Item Code\t    Model Number\t    Brand\t\t    Name\t\t    Unit Price\t    Quantity\t")
            print("\t\t", "_"*80)
            for (Item_code,Model_No,Brand,Name,Unit_price,Quantity) in result:
                    
                    
                print("                     ", Item_code, "\t\t    ", Model_No, "\t\t    ", Brand,  " \t    ", Name, " \t\t    ", \
                                    Unit_price, "\t\t    ", Quantity)
                print()
            print("\t\t", "="*80)    
                    
            print("\t", "_"*80)
            print()
            print("\tThis Record Will be Delete\n\t\
                     Do You Want to Delete : (Y/N)")
            j=input("Enter Your Choice : ")
            if j=='y' or j=="Y":
            
                cursor=mydb.cursor()
        
                cursor.execute(sq, (moc,))
                mydb.commit()
                print("\t1 Record Deleted")
                print('\n\n\n\n')
                print("\tDo You Want To Delete Other Record : (Y/N)")
                print()
                w=input("\t\tEnter Your Choice : ")
                if w=='y' or w=='Y':
                    print()
                    delete()
                elif w=='n' or w=='N':
                    print()
                    
                
                    print('\t\t1.Main Menu\n\t\t 2.Stock Detail')
                    d=int(input("\t\tEnter Choice Number : "))
                    if d==1:
                        main_menu()
                    elif d==2:
                        sdetail()
                    else:
                        main_menu()
            elif j=='n' or j=='N':
                print("\tDo you Want to Delete Another Record : (Y/N)")
                t=input("\t\tEntre Your Choice : ")
                if t=='y' or t=='Y':
                    print()
                    delete()
                elif t=='n' or t=='N':
                    print()
                    print('\t1.Main Menu\n 2.Stock Detail')
                    d=int(input("\tEnter Choice Number"))
                    if d==1:
                        main_menu()
                    else:
                        sdetail() 
                else:
                    main_menu()
                    
    elif och1==3:

         #=========Back to Stock Details==============
        
        print()
        print("\t\t==================================================")
        print()
        sdetail()
    else:
                print('\n\t\t _____________________Invalid Choice_________________')
                delete()
        
        
        
#======================================Customer Details===========================

def cdetail():
    mydb=sql.connect(host='localhost', user='root', passwd='root', database='mobile_shop')
    print('\t    1.Display All Records\n\t    2.Display By Bill No.\n\t    3.Display By Customer Name.\n\t    4.Modify\n\t    5.Quit')
    a=int(input('\tEnter your Choice No. : '))
    if a==1:
   
        #=========Display All Customer's Record=============
        
        cursor=mydb.cursor()
        cursor.execute("select * from user")
        result=cursor.fetchall()
        print("\t\t", "="*55)
        print()
        print("\tCustomer Name\tMobile Name\tBill Amount\tBill Number\tDate of Purchase\tWarranty")
        print("\t\t", "_"*55)
        print()
        for (Cname,Mobile_name,Bill_amount,Bill_no,D_O_P,Warranty) in result:
            print("\t",Cname,"\t\t",Mobile_name,"\t",Bill_amount,"\t\t",Bill_no,"\t\t",D_O_P,"\t",Warranty)
            print()
        print("\t\t", "="*55)
        print('\n \n\t\t ___________TOP OF APPLICATION____________________\n')
        cdetail()
    elif  a==2:


        #========Display Customer's Record By Bill No.=========     
        
        billno=input("\tEnter Bill No. : ")
        cursor=mydb.cursor()
        sq="""select * from user where Bill_no=%s"""
        cursor.execute(sq, (billno,))
        result=cursor.fetchall()
        print("\t\t", "="*55)
        print()
        print("\tCustomer Name\tMobile Name\tBill Amount\tBill Number\tDate of Purchase\tWarranty")
        print("\t\t", "_"*55)
        for (Cname,Mobile_name,Bill_amount,Bill_no,D_O_P,Warranty) in result:
            print("\t",Cname,"\t\t",Mobile_name,"\t",Bill_amount,"\t\t",Bill_no,"\t\t",D_O_P,"\t",Warranty)
        print("\t\t","="*55)
        print('\n \n\t\t ___________TOP OF APPLICATION____________________\n')
        cdetail()
    elif a==3:

         #======Display Customer's Record By Name===============
        
        cname=input("\tEnter Customer Name : ")
        cursor=mydb.cursor()
        sq="""select * from user where Cname=%s"""
        cursor.execute(sq, (cname,))
        result=cursor.fetchall()
        print("\t\t","="*55)
        print()
        print("\tCustomer Name\tMobile Name\tBill Amount\tBill Number\tDate of Purchase\tWarranty")
        print("\t\t", "_"*55)
        for (Cname,Mobile_name,Bill_amount,Bill_no,D_O_P,Warranty) in result:
            print("\t",Cname,"\t\t",Mobile_name,"\t",Bill_amount,"\t\t",Bill_no,"\t\t",D_O_P,"\t",Warranty)
        print("\t\t", "="*55)        
        print('\n \n\t\t ___________TOP OF APPLICATION____________________\n')
        cdetail()
    elif a==4:

             #===Modification in Customer Table======================= 
             
            print('\n\n')
            cmod()
    elif a==5:
        print("\n\n")
        main_menu()
    else:
        print("\n\n")
        print("\t____________Invalid Choice___________")
        print('\n \n \t\t___________TOP OF APPLICATION____________________\n')
        main_menu()
#=================================Stock Detail============================                     
def sdetail():
    mydb=sql.connect(host='localhost', user='root', passwd='root', database='mobile_shop')    
    print("\n\t 1.Display Stock\n\t 2.Add Stock\n\t 3.Delete stock\n\t 4.Modify\n\t 5.Quit")
    a=int(input("\tEnter your Choice Number : "))
    if a==1:

         #==============Display stock Details===============
        
        cursor=mydb.cursor()
        cursor.execute("select * from mobile")
        result=cursor.fetchall()
        print("\t\t","="*100)
        print()
        print("\t\tItem Code\t    Model Number\t    Brand\t\t    Name\t\t    Unit Price\t    Quantity\t")
        print("\t\t","_"*100)
        for (Item_code,Model_No,Brand,Name,Unit_price,Quantity) in result:
                    
                    
                    print("                     ", Item_code, "\t\t    ", Model_No, "\t\t    ", Brand,  " \t    ", Name,\
                          " \t\t    ", Unit_price, "\t\t    ", Quantity)
                    print()
        print("\t\t","="*100)    
                    
        print("\t", "_"*65)    
        print("\n\t\t\tPROCEED FORWARD")
        print()
        print('\t\t1.Main Menu\t 2.Stock Detail')
        print()
        d=int(input("\t\tEnter Choice Number : "))
        print()
        print("_"*100)
        if d==1:
            main_menu()
        else:
            sdetail()
    elif a==2:

         #==========Adding Stocks===========   
         
        cursor=mydb.cursor()
        Sid=1000
        sq="SELECT * FROM mobile"
        cursor.execute(sq)
        result = cursor.fetchall()
        for (id,Model_No,Brand,Name,Unit_price,Quantity) in result:
            Sid=id
         
         
        newid=Sid+1
                     
                
        mobn=input('\tEnter Model Number : ')
        brand=input('\tEnter Brand : ')
        name=input('\tEnter Mobile Name : ')
        unitp=int(input('\tEnter Unit Price : '))
        qun=int(input('\tEnter Quantity : '))
        mycursor=mydb.cursor()
        sq1="""insert into mobile (Item_code, Model_No, Brand, Name, unit_price, Quantity) \
                        values(%s, %s, %s, %s, %s, %s)"""
        val=(newid, mobn, brand, name, unitp, qun)
        mycursor.execute(sq1, val)
        mydb.commit()
        print()
        print("\t\tRecord Add succesfully")
        print()
        print('\n\n')
        print('\t1.Main Menu\n\t 2.Stock Detail')
        d=int(input("\n\tEnter Choice Number"))
        if d==1:
            main_menu()
        else:
            sdetail()
    elif a==3:

            #=============Deleting of Records in Stocks==========
            delete()


    elif   a==4:
                print("\n\n")
                smod()
    else:
        print('\n\t\t ____________________Invalid Choice_______________')
        main_menu()


create_database()
                   

                     

                 

                     
            
