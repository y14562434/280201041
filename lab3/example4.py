age = int(input("please enter your age: "))
price = 3
discount = 0.5

if age<6 or age>60 :
  price = 0
elif 6<=age<18 :
  price = 3*(1-discount)
else :
  price = 3
print("the ticket price is:" , price)      