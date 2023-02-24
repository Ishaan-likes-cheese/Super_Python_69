import math

'''

a = float(input("Give side a: "))
b = float(input("Give side b: "))

c = math.sqrt(a * a + b * b)
print(c)

'''

side = (input("Give the side you want to solve for(a,b,c):"))

if side != "a":
   print("please select a side (a,b,c)")

elif side != "b":
   print("please select a side (a,b,c)")

elif side != "b":
   print("please select a side (a,b,c)")


if side == "a":
   b = float(input("Give side b:"))
   c = float(input("Give side c:"))
   a = math.sqrt(b*b + c*c)
   print(f"Side a is: {a}")
elif side == "b":
   a = float(input("Give side a:"))
   c = float(input("Give side c:"))
   b = math.sqrt(a*a + c*c)
   print(f"Side b is: {b}")

elif side == "c":
   b = float(input("Give side b:"))
   a = float(input("Give side a:"))
   c = math.sqrt(b*b + a*a)
   print(f"Side a is: {c}")
