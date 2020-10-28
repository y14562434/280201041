a = float(input("enter the value of a: "))
b = float(input("enter the value of b: ")) 
c = float(input("enter the value of c: "))
D = b**2 - 4*a*c
x1 = (-b -D**0.5)/2*a
x2 = (-b +D**0.5)/2*a

if D>0 :
  root1 = x1
  root2 = x2
  print("your roots are:" , root1 ,"and" , root2)
elif D==0 :
  root =x1=x2
  print("your root is:" , root)  
else :
  print("you do not have any real roots")