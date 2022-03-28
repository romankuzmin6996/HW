from math import *
a = float(input("Ievadi a locekli: "))
b = float(input("Ievadi b locekli: "))
c = float(input("Ievadi c locekli: "))
Diskr = b**2 - 4*a*c
if Diskr<0:
  print("nav saknes, jo Diskrim. < 0")
elif Diskr>0:
  x1= (-b+sqrt(Diskr))/2*a
  x2= (-b-sqrt(Diskr))/2*a
  print("2 saknes, jo Diskr.>0")
  print("X1:", x1, "X2", x2)
elif Diskr==0:
  x1= (-b+sqrt(Diskr))/2*a
  print("1 sakne, jo Diskrim. = 0")
  print("X:", x1)