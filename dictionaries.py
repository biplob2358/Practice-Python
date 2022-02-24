car={
    "brand":"Ford",
    "model":"Mustang",
    "year":1997,
    "year":2000 #changeable

}
print(car)
print(car["brand"])
print(len(car))
print(type(car))
x=car.keys()
print(x)
y=car.values()
print(y)
z=car.items()
print(z)
car["color"]="Red"
print(car)