# THIS IS A PROGRAM FOR CALCULATOR IN PYTHON
print(".......CALCULATOR.......")
# HERE WE TAKE INPUT FROM USER
NUMBER_1 = float(input("enter the first number:"))
NUMBER_2 = float(input("enter the second number:"))
print(" PLEASE PRESS A/a FOR ADDITON (+)\n")
print(" PLEASE PRESS S/s FOR SUBTRACTION (-)\n")
print(" PLEASE PRESS M/m FOR MULTIPLICATON (*)\n")
print(" PLEASE PRESS D/d FOR DIVISION (/)\n")      
your_choice = (input("ENTER YOUR CHOICE FROM A/a S/s M/m D/d : "))
# THIS PART WILL PERFROM CALCULATION
if your_choice == 'A' or your_choice == 'a':
    ADDITION = NUMBER_1+NUMBER_2
    print("\u2705 THE ADDITION OF TWO NUMBERS WILL BE =",ADDITION)
elif your_choice == 'S' or your_choice =='s' :
    SUBTRACTION = NUMBER_1-NUMBER_2
    print("\u2705 THE SUBTRACTION OF TWO NUMBERS WILL BE =",SUBTRACTION)
elif your_choice == 'M' or your_choice =='m':
    MULTIPLICATION = NUMBER_1*NUMBER_2
    print("\u2705 THE MULTIPLICATION OF TWO NUMBERS WILL BE =",MULTIPLICATION)
elif your_choice == 'D' or your_choice =='d':
    if NUMBER_2 == 0:
        print("\u274C ERROR: WE CANNOT DIVIDE ANY NUMBER BY ZERO")
    else:
        DIVISION = NUMBER_1/NUMBER_2
    print("\u2705 THE DIVISION OF TWO NUMBERS WILL BE =",DIVISION)
else:
    print("\u274C INVALID CHOICE.....PLEASE CHOOSE 'A' 'S' 'M' 'D' ")
