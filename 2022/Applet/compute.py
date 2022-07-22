MODULE = "calc"
 
# 定义函数
def add(x, y):
   """相加"""
 
   return x + y
 
def subtract(x, y):
   """相减"""
 
   return x - y
 
def multiply(x, y):
   """相乘"""
 
   return x * y
 
def divide(x, y):
   """相除"""
 
   return x / y
 
def run():
    # 用户输入
    print("["+MODULE+"]"+"选择运算：")
    print("["+MODULE+"]"+"1、相加")
    print("["+MODULE+"]"+"2、相减")
    print("["+MODULE+"]"+"3、相乘")
    print("["+MODULE+"]"+"4、相除")
 
    choice = input("["+MODULE+"]"+"输入你的选择(1/2/3/4):")
 
    num1 = int(input("["+MODULE+"]"+"输入第一个数字: "))
    num2 = int(input("["+MODULE+"]"+"输入第二个数字: "))
 
    if choice == '1':
       print("["+MODULE+"]"+num1,"+",num2,"=", add(num1,num2))
 
    elif choice == '2':
       print("["+MODULE+"]"+num1,"-",num2,"=", subtract(num1,num2))
 
    elif choice == '3':
       print("["+MODULE+"]"+num1,"*",num2,"=", multiply(num1,num2))
 
    elif choice == '4':
       print("["+MODULE+"]"+num1,"/",num2,"=", divide(num1,num2))
    else:
       print("["+MODULE+"]"+"非法输入")
