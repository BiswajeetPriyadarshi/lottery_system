import random
num1=random.randint(1,101)
print('=================================================')
print('****welcome lottery system*******')
print('=================================================')
print()
print('1.Start      2.Exit')
x=int(input('Enter no. 1 to start\nEnter no.2 to Exit the Game \n'))
num0=0
if x==1:
  
    while True:
        num=int(input("Guess The no. to win lottery :  "))
        num0 = num0+1
        if num==num1:
            print("Hurray you win the lottery")
        else:
            print("Oops Better Luck Next Time")
        if num0==5:
            break
        
        
elif x==2:
    exit
else:
    print("Please Enter Valid num") 

print("Your lottery NO.     ",num1)   
