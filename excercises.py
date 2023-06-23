# string = "%s %s is 20 years old"
# name = "Trust"
# print(string%(name,"Dolamo"))
# nums = [5,5,6,6,7] 
# try:
#    print(sum(nums))
 
# except:
#    print('Cannot print the sum! Your variables are not numbers.')
# name = input("Enter your name")
# age = int(input("Enter your age"))
# house_num = int(input("Enter your House Number"))
# name = "TRUST".lower()
# reversed_name = name[::-1]
# print(name)
# print(reversed_name)
word = input("Enter word: ").lower()
reversed_word = word[::-1]
if word == reversed_word:
  print("The word is a Palindrome")
else:
  print("The word is not a Palindrome")
