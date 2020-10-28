gpa =float(input("enter your GPA: "))
lecture = int(input("enter the number of your lectures: "))

if gpa< 2.0 :
  if lecture<47:
    print("not enough GPA and not enough number of lectures")
  else : 
    print("not enough GPA")  
else :
  if lecture<47 :
    print("not enough number of lectures")
  else :
    print("graduated!")          