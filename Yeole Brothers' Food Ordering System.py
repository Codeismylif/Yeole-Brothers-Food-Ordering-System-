

import pandas as pd


# ------------------ Food Menu System --------------------


def main():
    
    totalamount = 0
    
    totalamounta = 0
    
    totalamountb = 0
    
    totalamountc = 0
    
    
    while True:
        
        print(" Please choose what you want to have : \n")
        
        print(" 1. STARTERS \n")
        
        print(" 2. MAIN COURSE \n")
        
        print(" 3. DESSERTS \n")
        
        print(" 4. EXIT/ BILL AMOUNT \n")
        
        
        b = input(" Enter the no. : ")
        
        print("-"*50,"\n")


        if b == '1':                                                                       
            
            print(" STARTERS \n")

            starters = { 'Item' : ['Paneer Platter',
                                   'Mushroom Tikka',
                                   'Chicken Chilly',
                                   'Chicken 65',
                                   'Hara Bara Kebab'],
                        'Amount' : [200, 180, 230, 250, 190] }
            
            starter_df = pd.DataFrame(starters)
            
            print("-"*50)

            print(starter_df)
            
            print("-"*50, "\n")
            
            print(" Please enter the name of the dish: \n")
            
            itema = input(" ")
            
            print("-"*50, "\n")
            
            print(" How many ? \n")
            
            noofitemsa = int(input(" "))
            
            print("-"*50, "\n")
            
            
            for ia, ja in zip(starters['Item'],starters['Amount']):
                

                if itema == ia:
                    
                    totalamounta += ja * noofitemsa
                    
                    print (" Item : ", itema)
                    
                    print (" Amount: ₹", totalamounta, "/-")
                    
                    print(" With 18% GST : ₹",\
                           totalamounta + totalamounta*0.18,\
                            "/-", "\n")


        elif b == '2':
            
            print(" MAIN COURSE \n")

            main_course = {'Item': ['Paneer Tikka',
                                    'Mushroom Kadhai',
                                    'Butter Chicken',
                                    'Chicken Tikka',
                                    'Mix Veg'],
                        'Amount': [250, 230, 280, 250, 150]}
            
            main_course_df = pd.DataFrame(main_course)

            print("-"*50)
            
            print(main_course_df)
            
            print("-"*50, "\n")
            
            print(" Please enter the name of the dish : \n") 
            
            itemb = input(" ")
            
            print("-"*50, "\n")
            
            print(" How many ? \n")
            
            noofitemsb = int(input(" "))
            
            print("-"*50, "\n")


            for ib, jb in zip(main_course['Item'],main_course['Amount']):
                
                
                if itemb == ib:
                    
                    totalamountb += jb * noofitemsb
                    
                    print(" Item : ", itemb)
                    
                    print(" Amount : ₹", totalamountb, "/-")
                    
                    print(" With 18% GST : ₹",\
                            totalamountb + totalamountb*0.18,\
                            "/-", "\n")


        elif b == '3':
            
            print(" DESSERTS \n")

            desserts = {'Item': ['Kulfi',
                                 'Ice Cream',
                                 'Ice Cream Cone',
                                 'Faluda',
                                 'Gulab Jamun'],
                           'Amount': [195, 185, 235, 150, 100]}

            desserts_df = pd.DataFrame(desserts)

            print("-"*50)
            
            print(desserts_df)
            
            print("-"*50, "\n")
            
            print(" Please enter the name of the dish : \n")
            
            itemc = input(" ")
            
            print("-"*50, "\n")
            
            print(" How many ? \n")
            
            noofitemsc = int(input(" "))
            
            print("-"*50, "\n")


            for ic, jc in zip(desserts['Item'], desserts['Amount']):
                
                
                if itemc == ic:
                    
                    totalamountc += jc * noofitemsc
                    
                    print (" Item : ", itemc)
                    
                    print (" Amount : ₹", totalamountc, "/-")
                    
                    print(" With 18% GST : ₹",\
                            totalamountc + totalamountc*0.18,\
                            "/-", "\n")
                    
                    
        else:
            
            break
        
    print("-"*50, "\n")

    totalamount = totalamounta + totalamountb + totalamountc
    
    totalamountf = (totalamounta + totalamounta*0.18) + \
                   (totalamountb + totalamountb*0.18) + \
                   (totalamountc + totalamountc*0.18)
    
    print(" TOTAL AMOUNT : ₹", totalamount, "/-", "\n")

    print(" TOTAL AMOUNT WITH 18% GST: ₹", totalamountf, "/-", "\n")
    
    print("-"*50, "\n")
    
    print("-------------------- THANK YOU ------------------- \n")
    
    print("-------------------- CREATED BY ------------------ \n")
    
    print("    Romanch D. Yeole            Pinak K. Yeole \n")
    
    print("    12th E                      12th E \n")
    
    print("    15                          13 \n")
    

# ------------------ Introduction & User Credentials --------------------


print("-"*50, "\n")

print(" Welcome to YEOLE BROTHERS' FOOD ORDERING SYSTEM \n")

print("-"*50, "\n")


df = pd.read_csv(r"C:\Users\Roman\Desktop\FOS.csv")


dict1 = df.to_dict()

print(" Do you want to : \n")

print(" 1. REGISTER \n")

print(" 2. LOGIN \n")


a = input(" Enter the no. : ")

print("-"*50, "\n")

       
# -------------------- REGISTER --------------------


if a == '1':
    
    print("-------------------- REGISTER -------------------- \n")
    
    new_username = input(" Please enter your name : ") 
    
    print("-"*50, "\n")
    
    new_password = input(" Please enter a new password : ")
    
    print("-"*50, "\n")
    
    confirmpassword = input(" Please re-enter your password : ")
    
    print("-"*50, "\n")
    

    if new_password == confirmpassword:
        
        row = pd.Series([new_username,new_password],
                         index=df.columns)
        
        df = df.append(row,ignore_index=True)
        
        df.to_csv(r"C:\Users\Roman\Desktop\FOS.csv",
                  mode='w',
                  index=False,
                  header=True)
        
        print(" User Added Successfully ")
        
        print("-"*50, "\n")
        
        print(" Run the code again and Login to continue ")
        
        print("-"*50, "\n")
        
        
    else:
        
        print(" Password doesn't Match ")
        
        print("-"*50, "\n")
        
        
# --------------------- LOGIN ----------------------

elif a == '2':

    print("--------------------- LOGIN ---------------------- \n")

    login_username = input(" Please Enter username : ")

    print("-"*50, "\n")
    
    login_password = input(" Please Enter password : ")

    print("-"*50, "\n")

    userNameFound = False


    for i in dict1 ['username'].keys():


        if dict1 ['username'][i] == login_username:

            userNameFound = True


            if dict1 ['password'][i] == login_password:

                print(" Success ")

                print("-"*50, "\n")

                main()


            else:
            
                print(" Invalid Password ")

                print("-"*50, "\n")


    if not userNameFound:

        print(" Invalid Username ")

        print("-"*50, "\n")