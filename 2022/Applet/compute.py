import easygui


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
 
def pow(x, y):
	"""幂"""

	return x ** y

def calc():
	# 用户输入
	choice = easygui.choicebox("Select an operator", "Calculator", ["Add","Sub","Multiply","Divide","Pow","Quit"])
	nums = easygui.multenterbox("["+MODULE+"]"+"输入数字: ", "Calculator", ["Number 1", "Number 2"])
	num1, num2 = int(nums[0]), int(nums[1])
	if choice == "Add":
		print("["+MODULE+"]"+str(num1),"+",str(num2),"=", add(num1,num2))
 
	elif choice == "Sub":
		print("["+MODULE+"]"+str(num1),"-",str(num2),"=", subtract(num1,num2))
 
	elif choice == "Multiply":
		print("["+MODULE+"]"+str(num1),"*",str(num2),"=", multiply(num1,num2))
 
	elif choice == "Divide":
		print("["+MODULE+"]"+str(num1),"/",str(num2),"=", divide(num1,num2))

	elif choice == "Pow":
		print("["+MODULE+"]"+str(num1),"^",str(num2),"=", pow(num1,num2))
	else:
		return 0
