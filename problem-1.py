class Calculator:
    def add(self, a, b):
        return a+b
    
    def subtract(self, a, b):
        return a-b
        
    def multiply(self, a, b):
        return a*b

    def divide(self, a, b):
        return a/b

my_cl = Calculator()
                
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
ch=input("Enter operator: ")        
if(ch == "+"):
    print(a, "+", b, "=", my_cl.add(a, b))
elif(ch == "-"):
    print(a, "-", b, "=", my_cl.subtract(a, b))
elif(ch == "*"):
    print(a, "*", b, "=", my_cl.multiply(a, b))
elif(ch == "/"):
    print(a, "/", b, "=", my_cl.divide(a, b))
    
else:
    print("Invalid Input")