a = float(input("num1"))
b = float(input("num2"))
c = float(input("num3"))

if a<=b and a<=c :
  min_number = a
elif b<=a and b<=c :
  min_number = b 
else :
  min_number = c  


print("min value" , min_number)