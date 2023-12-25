a = int(input("enter first number\n:::"))
b = int(input("enter second number\n:::"))
c = input("enter the operator you want\n[+,h,×,÷]:::")
if(c == "+"):
    d = a + b
    print("the answer is = ",d)
elif(c == "-"):
    d = a - b
    print("the answer is = ",d)
elif(c == "×"):
    d = a * b
    print("the answer id = ",d)
elif(c == "÷"):
    d = a / b
    print("the answer is = ",d)
else:
    print("please choose a valid operator")

