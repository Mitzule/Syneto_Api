import math

def triangle():
    
    side_1 = int(input("side 1: "))
    side_2 = int(input("side 2: "))
    side_3 = int(input("side 3: "))

    def triangle_perimeter(side_1, side_2, side_3): 
        perimeter = side_1 + side_2 + side_3
        return perimeter
    
    def triangle_area(side_1, side_2, side_3): #using Heron's formula
        s = triangle_perimeter(side_1, side_2, side_3) / 2
        area = (s*(s-side_1)*(s-side_2)*(s-side_3)) ** 0.5 
        return area
    
    print("triangle perimeter:", triangle_perimeter(side_1, side_2, side_3))
    print("triangle area:", round(triangle_area(side_1, side_2, side_3), 2))
    
def square():
    
    side_1 = int(input("side 1: "))
    side_2 = int(input("side 2: "))
    side_3 = int(input("side 3: "))
    side_4 = int(input("side 4: "))
    
    def square_perimeter(side_1, side_2, side_3, side_4):
        perimeter = side_1 + side_2 + side_3 + side_4
        return perimeter
    
    def square_area(side_1, side_2, side_3, side_4):
        area = side_1 * side_2
        return area
    
    print("square perimeter:", square_perimeter(side_1, side_2, side_3, side_4))
    print("square area:", square_area(side_1, side_2, side_3, side_4))
    
def rectangle():
    
    side_1 = int(input("side 1: "))
    side_2 = int(input("side 2: "))
    
    def rectangle_perimeter(side_1, side_2):
        perimeter = (side_1 + side_2) * 2
        return perimeter
    
    def rectangle_area(side_1, side_2):
        area = side_1 * side_2
        return area
    
    print("rectangle perimeter:", rectangle_perimeter(side_1, side_2))
    print("rectangle area:", rectangle_area(side_1, side_2))
    
def circle():
    
    pi = math.pi
    r = int(input("radius: "))
    
    def circle_perimeter(r):
        perimeter = 2 * pi * r
        return perimeter
    
    def circle_area(r):
        area = pi * r ** 2
        return area
    
    print("circle perimeter:", round(circle_perimeter(r), 2))
    print("circle area:", round(circle_area(r), 2))    

def rhombus():
    
    side_1 = int(input("side 1: "))
    side_2 = int(input("side 2: "))
    
    def rhombus_perimeter(side_1, side_2):
        perimeter = (side_1 + side_2) * 2
        return perimeter
    
    def rhombus_area(side_1, side_2):
        area = side_1 * side_2
        return area
    
    print("rhombus perimeter:", rhombus_perimeter(side_1, side_2))
    print("rhombus area:", rhombus_area(side_1, side_2))
    
def parallelogram():
    
    side_1 = int(input("side 1: "))
    side_2 = int(input("side 2: "))
    
    def parallelogram_perimeter(side_1, side_2):
        perimeter = (side_1 + side_2) * 2
        return perimeter
    
    def parallelogram_area(side_1, side_2):
        area = side_1 * side_2
        return area
    
    print("parallelogram perimeter:", parallelogram_perimeter(side_1, side_2))
    print("parallelogram area:", parallelogram_area(side_1, side_2))
    
def trapezoid():
    
    side_1 = int(input("side 1: "))
    side_2 = int(input("side 2: "))
    side_3 = int(input("side 3: "))
    side_4 = int(input("side 4: "))
    
    def trapezoid_perimeter(side_1, side_2, side_3, side_4):
        perimeter = side_1 + side_2 + side_3 + side_4
        return perimeter
    
    def trapezoid_area(side_1, side_2, side_3, side_4):
        area = (side_1 + side_2) / 2 * side_3
        return area
    
    print("trapezoid perimeter:", trapezoid_perimeter(side_1, side_2, side_3, side_4))
    print("trapezoid area:", trapezoid_area(side_1, side_2, side_3, side_4))
    
def pentagon():
    
    side_1 = int(input("side 1: "))

    def pentagon_perimeter(side_1):
        perimeter = side_1 * 5
        return perimeter
    
    def pentagon_area(side_1):
        area = 5 * side_1 ** 2 / (4 * math.tan(math.pi / 5))
        return area
    
    print("pentagon perimeter:", pentagon_perimeter(side_1))
    print("pentagon area:", round(pentagon_area(side_1), 2))

def hexagon():
    
    side_1 = int(input("side 1: "))
    
    def hexagon_perimeter(side_1):
        perimeter = side_1 * 6
        return perimeter
    
    def hexagon_area(side_1):
        area = 3 * side_1 ** 2 * math.sqrt(3) / 2
        return area
    
    print("hexagon perimeter:", hexagon_perimeter(side_1))
    print("hexagon area:", round(hexagon_area(side_1), 2))
    
def decagon():
    
    side_1 = int(input("side 1: "))
    
    def decagon_perimeter(side_1):
        perimeter = side_1 * 10
        return perimeter
    
    def decagon_area(side_1):
        area = 5 * side_1 ** 2 * (5 + 2 * math.sqrt(5)) / 4
        return area
    
    print("decagon perimeter:", decagon_perimeter(side_1))
    print("decagon area:", round(decagon_area(side_1), 2))

while True:
    
    print("##############################")
    print("#       1. triangle          #")
    print("#       2. square            #")
    print("#       3. rectangle         #")
    print("#       4. circle            #")
    print("#       5. rhombus           #")
    print("#       6. parallelogram     #")
    print("#       7. trapezoid         #")
    print("#       8. pentagon          #")
    print("#       9. hexagon           #")
    print("#       10. decagon          #")
    print("#       11. exit             #")
    print("##############################")

    choice = int(input("Choice: "))

    if choice == 1:
        triangle()
    elif choice == 2:
        square()
    elif choice == 3:
        rectangle()
    elif choice == 4:
        circle()
    elif choice == 5:
        rhombus()
    elif choice == 6:
        parallelogram()
    elif choice == 7:
        trapezoid()
    elif choice == 8:
        pentagon()
    elif choice == 9:
        hexagon()
    elif choice == 10:
        decagon()
    elif choice == 11:
        break
    else:
        print("Invalid choice")
        