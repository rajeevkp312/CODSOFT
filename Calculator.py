print("Simple Calculator")
x=float(input("Enter the 1st number \n"))
y=float(input("Enter the 2nd number \n"))
print('Choose the arithmetic operation \n 1.Addition \n 2.Subtraction \n 3.Multiplication \n 4.Division')
choice=int(input("Choose any option from 1 to 4\n"))
if choice==1:
    print(x+y)
elif choice==2: 
    print(x-y)
elif choice==3:
    print(x*y)
elif choice==4:
    print(x/y)
else:
    print("invalid option choosen")     
             
