name=["Biplob","Gourob","Masum","Sajib","Habib"]
print(name)
print(len(name))
print(type(name))
print(name[1])
print(name[-1])
print(name[1:4])
name[2]="Raju"
print(name)
name.append("Saju")
print(name)
name.insert(1,"Sagor")
print(name)

num1=[1,2,3,4,5]
num2=[6,7,8,9,10]
num1.extend(num2)
print(num1)
num1.remove(2)
print(num1)

name.sort()
print(name)

name.sort(reverse=True)
print(name)