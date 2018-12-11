def Add(x,y,z):
    print(x+y+z)

Add(5,6,7)

class calculator:
    color ='red' # properties
    battery = 2

    def Add(x,y,z): #method
        print("addition ",x+y+z)
    def Subtr(x,y,z): #method
        print("subration ",x-y-z)

print(calculator.color)
print(calculator.battery)
calculator.Add(5,6,7)
calculator.Subtr(5,6,7)
