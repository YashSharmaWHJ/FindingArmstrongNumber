'''a=32
c = a%(10**(len(str(a))-1))
b = (a-c)/(10**(len(str(a))-1))

ArmstrongNumber =False
if (c*c + b*b == a):
    ArmstrongNumber =True

else:
    ArmstrongNumber =False
    print("This number is not an Armstrong Number")

if (ArmstrongNumber==True):
    print("This number is an Armstrong Number")

'''
a=153

sum=0
temp=a
while temp>0:
    x=temp%10
    sum=sum+(x**3)
    temp=temp//10
    print(temp)
if (a==sum):
    print("The number is an armstrong number")
else:
    print("The number is not an armstrong number")
