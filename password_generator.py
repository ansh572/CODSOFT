import random
letters=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'
'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
numbers=['0','1','2','3','4','5','6','7','8','9']
symbols=['!','@','#','$','%','&','(',')','*','+','~','^','-','=','_','{','}','[',']','?','/','|',';',':','"','.','<','>'] 
print("Welcome to password generator")
Required_letters = int(input("How many letters are required in your password?\n"))
Required_symbols = int(input("How many symbols are required in your password?\n"))
Required_numbers = int(input("How many numbers are required in your password\n"))
password_list=[]
for i in range(1,Required_letters+1): #1,2,3,4
    char = random.choice(letters)
    password_list += char
for i in range(1,Required_symbols+1):
    char = random.choice(symbols)
    password_list += char
for i in range(1,Required_numbers+1):
    char = random.choice(numbers)
    password_list += char
print("this will give you exact password as per your input\n",password_list)# this will give you exact password as per your input 
random.shuffle(password_list)# now shuffling your password
print()
print("here the password_list will get shuffled\n",password_list)# here the password_list will get shuffled
password=""
for char in password_list:
    password +=  char
print()
print("FINAL PASSWORD \n",password)