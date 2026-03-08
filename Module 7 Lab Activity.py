import math

#Process to compute the area of a circle
def areaOfCircle(r):
    return math.pi * (r ** 2)


radius = float(input("Enter the radius of the circle: "))
area = areaOfCircle(radius)

print("The area of the circle is:", area)

#Martin Sanchez
#March 7 2026
#Problem1AreaOfCircle.py
#Main program: ask user for radius and compute area


def in_range(n):
    # range(1,10) includes numbers 1 through 9
    return n in range(1, 10)

#Ask for a number
num = int(input("Enter a number: "))

#Check result
if in_range(num):
    print(f"{num} is in the range 1 to 9")
else:
    print(f"{num} is NOT in the range 1 to 9")


#Martin Sanchez
#March 7 2026
#Problem2CheckRange.py    
#Program checks whether a number is in a given range 1-10


def multiply_list(numbers):
    result = 1
    for num in numbers:
        result *= num
    return result

#Given list
nums = [5, 2, 7, -1]

#Print the result
product = multiply_list(nums)
print("The product of the list is:", product)

#Martin Sanchez
#March 7 2026
#Problem3MulitplyList.py
#Program multiplya all the numbers in a list [5, 2, 7, -1]


def sort_list(numbers):
    sorted_list = []
    
    for num in numbers:
#If sorted_list is empty, just append
        if not sorted_list:
            sorted_list.append(num)
        else:
#Find the correct position to insert num
            inserted = False
            for i in range(len(sorted_list)):
                if num < sorted_list[i]:
                    sorted_list.insert(i, num)
                    inserted = True
                    break
#If num is the largest, append at the end
            if not inserted:
                sorted_list.append(num)
    
    return sorted_list

# Given list
nums = [1, 3, 3, 3, 6, 2, 3, 5]

# Call the function
result = sort_list(nums)
print(result)

#Martin Sanchez
#March 7 2026
#Problem4Unique.py
#Program takes a list of numbers and returns a new list. Use list [1, 3, 3, 3, 6, 2, 3, 5]



import turtle

def drawSquare(t, sz):
    """Get turtle t to draw a square of side sz."""
    for _ in range(4):
        t.forward(sz)
        t.left(90)

# Setup
wm = turtle.Screen()
alex = turtle.Turtle()
alex.color("blue")
alex.speed(0)

# Draw concentric squares
size = 200          # starting size
step = 20           # how much each square shrinks

for _ in range(10):  # number of squares
    drawSquare(alex, size)
    alex.penup()
    alex.forward(step / 2)
    alex.left(90)
    alex.forward(step / 2)
    alex.right(90)
    alex.pendown()
    size -= step

wm.exitonclick()



#Martin Sanchez
#March 7 2026
#Problem5Squares.py
#Program produces the image of squares.


class car:

    def __init__(self, model, year, color, type, manufacturer):
        self.model = model
        self.year = year
        self.color = color
        self.type = type
        self.manufacturer = manufacturer

    def get_model(self):
        return self.model

    def get_year(self):
        return self.year

    def get_color(self):
        return self.color

    def get_type(self):
        return self.type

    def get_manufacturer(self):
        return self.manufacturer

    def fullspecs(self):
        return (
            self.model + ' ' +
            str(self.year) + ' ' +
            self.color + ' ' +
            self.type + ' ' +
            self.manufacturer
        )

car1 = car("Sports", 2012, "Blue", "Coupe", "Ford")
car2 = car("Sedan", 2020, "Black", "Compact", "Honda")

print(car1.get_color())
print(car1.get_model())
print(car2.get_color())
print(car1.get_type())
print(car1.get_manufacturer())
print(car1.fullspecs())
print(car2.fullspecs())


#Martin Sanchez
#March 7 2026
#Problem6ClassCar.py
#Program adds two additional attributes of ‘type’ and ‘manufacturer’









