num1=[1,2,3]
num2=[4,5,6]
num3=(num1+num2)
print(num3)
for x in num2:
  num1.append(x)
print(num1)  
num1.extend(num2)
print(num1)