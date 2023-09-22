age = int (input ("Сколько вам лет"))

if age % 100 == 11 :
      print (age,  "лет")
elif age % 10 == 1:
     print (age,  "год")
elif age > 10 and age <15:
      print (age,  "лет")
elif age % 10 >4:
    print (age, "лет")
elif age % 10 == 0:
      print (age, "лет")
else:
      print (age,  "года")
