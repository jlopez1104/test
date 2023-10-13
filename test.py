def rectangle():
        width = float(input("please enter in width of rectangle: "))
        length = float(input("please enter in height of rectangle: "))
        AofRectangle = width*length
        print("the area of the rectangle is: ",AofRectangle,)
def multi():
    mult = int(input("please enter number you wish to multiply: "))
    for i in range (1,13):
      print (mult,"times",i, "=",mult*i,)
while True:
    print("Menu:")
    print("what would you like to solve?")
    print("1) Area of Rectangle")
    print("2) Times Table")
    print("3) Exit")
    choice = input("please enter input (1/2/3): ")
    if choice == "1":
        rectangle()
    elif choice == "2":
        multi()
    elif choice == "3":
        print("thank you for using program!")
        break
    else:
        print("please enter a correct number")