print("★ Hello, Welcome to my Webpage. For your safety, I need your information")

name = input("★ What is your name?\n")
age = int(input("★ How old are you?\n")) - 1
city = input("★ Where do you live?\n")
is_information_correct = input(f"★ Hi, {name}. You are legal age is {age} years old and live in {city}.\nIf it is correct, Please press Y or if it is not correct, Please press N\n[Y/N]\n")
print("The answer is " + is_information_correct)