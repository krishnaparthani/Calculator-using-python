x=input("please give the first value \n")
y=input("please give the second value\n")
op=input("please give the operator\n")
if (op=="+") :
    print(int(x)+int(y))
elif (op=="-") :
    print(int(x)-int(y))
elif (op=="*") :
    print(int(x)*int(y))
elif (op=="/") :
    print(int(x)/int(y))
elif (op=="%") :
    print(int(x)%int(y))
else:
    print("invalid input")