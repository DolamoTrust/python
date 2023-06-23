
def welcome():
   name = input("Enter your 1st-name: ")
   surname = input("enter your Surname: ")
   print("WELCOME:",name,surname)
   return name

def age_confirmer():
    num = int(input("enter your age: "))
    if num >= 18:
     print("You meet age requirements!")
     call_apscalcualtor()
    elif num < 18:
        print("Unfortunately you dont meet age requirements!")
    else :
        print("you have to enter age")

def aps_calculator():
   
   maths = int(input("Insert your maths level /7: "))
   L_science = int(input("Insert your life sciences level /7:"))
   P_science = int(input("Insert your pysical sciences level /7: "))
   Geography = int(input("Insert your geography level /7: "))
   home_language = int(input("Insert your level home language /7: "))
   add_language = int(input("Insert your level additional language /7:"))  
   total_aps = maths + L_science + P_science + Geography + home_language + add_language
   print("Your final APS is:" ,total_aps)

   if home_language >= 4 and total_aps >=23 :
      print("Bachelor pass")
   elif home_language >= 4 and total_aps >=15 and total_aps <23:
      print("Diploma pass")
   elif home_language >=4 and total_aps <15:
      print("Higher Certificate")       
   elif home_language <3:
      print("You can apply to rewrite")  


def call_apscalcualtor():

   n = input("would you like to calculate your aps if yes and enter: ")
   if n== "yes":
      aps_calculator()
   else:
      print("You may exit")

     
welcome()
age_confirmer()
# to be continued

