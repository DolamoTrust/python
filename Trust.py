
def welcome():
   name = input("Enter your 1st-name: ")
   middle_name = input("Enter your middle name: ")
   surname = input("enter your Surname: ")
    
   print("WELCOME ",name,middle_name,surname )
   return name + middle_name + surname
def age_confirmer(name):
    username = name
    print(username)
    # num = int(input("enter your age: "))
    # if num >= 18:
    #  print("You meet age requirements!")
    # elif num < 18:
    #     print("Unfortunately you dont meet age requirements!")
    # else :
    #     print("you have to enter age")

def testmark_checker():
   
   test1 = int(input("Insert your test1 mark /50: "))
   test2 = int(input("Insert your test2 mark /50:"))
   test3 = int(input("Insert your test3 mark /50: "))
   test4 = int(input("Insert your test4 mark /50: "))  
   total_test = test1 + test2 + test3 + test4
   total_testmark = total_test / 200
   total_percentage = total_testmark * 100
   print("Your final mark is: " ,total_percentage)

   if total_percentage >= 50:
      print("you have met the pass mark")
      print("You may proceed to the Submit your mark to you end year report")
   else:
         print("you have not met the pass mark")
         print('You can retake the exams')   

age_confirmer(welcome)       
welcome()
testmark_checker()
