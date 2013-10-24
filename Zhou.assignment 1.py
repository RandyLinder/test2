Yi Zhou (EID:yz4439)


1.
# sphere.py
# A program that computes the volume and surface area of a sphere.

import math

def main():
    print("This program calculates the volume and surface area of a sphere")
    r = eval(input("Please enter the radius of the sphere: "))
    V=4/3*math.pi*r*r*r  ###It would be better to use a more informative variable names than single characters.
	                     ###Better to use exponentiation for powers, e.g., r**3
    A=4*math.pi*r*r		###To save typing you could assign math.pi to a variable.
    print("The volume and surface area of the sphere are", V, "and", A, "respectively")

main()



2.
# Pizzacost.py
# A program that computes  the cost per square inch of a circular pizza.


import math

def main():
    print("This program calculates the cost per square inch of a circular pizza")
    r = eval(input("The radius of the pizza is: "))  ###Need to prompt them for the radius in inches
    TotalCost= eval(input("The cost of the pizza is: "))  ###What might you do if they input $13.00
    A=math.pi*r*r
    B=TotalCost/A
    print("The cost per square inch of the circular pizza is", B)

main()

3.   ###If you try to run this it will fail because the indentation is wrong.
     ###The same problem is evident on some of your other programs.

    # Molecularweight.py
    # A program that computes the molecular weight of a hydrocarbon.

    def main():
	 print("This program determines the molecular weight of a hydrocarbon")
	 print()  ###How else might you have printed a blank line?
	 print("Please enter the number of hydrogen, carbon, and oxygen atoms")  ###How might you have done this using simultaneous assignment?
	 H = eval(input("H: "))
	 C = eval(input("C: "))
	 O = eval(input("O: "))
	 Weight=1.0079*H+12.011*C+15.9994*O  ###Use white space to make this equation more easily read.
	                                     ###This is a problem elsewhere too.
	 print ("The molecular weight of the hydrocarbon is", Weight)
    
    main()

4.
    # lightning.py 
    # A program that determines the distance to a lightning strike.

    def main():
	print ("This program determines the distance to a lightning strike")
	Time = eval(input("The time elapsed between the flash and the sound of thunder in senconds is: "))
	distance = 1100*Time/5280
	print ()
	print ("The distance to the lightning strike is", distance, "miles")
    main()

5.

    # CoffeeCost.py 
    # A program that determines the cost of a coffee order from The Konditorei coffee shop.

    def main():
	print ("This program determines the cost of a coffee order from The Konditorei coffee shop")
	Amount = eval(input("The amount of coffee ordered in pound is: "))
	Cost = 10.50*Amount+0.86*Amount+1.50
	print ()
	print ("The cost of this order is $", Cost)
    
    main()

6.
# slop.py 
# A program that determines the the slop of a line through two (non-vertical) points.

def main():
    print("This program determines the slop of a line through two (non-vertical) points: (x1,y1) and (x2,y2)")
    print()

    x1,y1,x2,y2= eval(input("Please enter the value of (x1,y1,x2,y2) with comma in between:"))   ###These instuctions might be confusing to a user.
																								 ###How might you write this so it would be clearer?
    
    k=(y2-y1)/(x2-x1)

    print()
    print("The slope of the line through the two points is", k )

main()

7. 
# distance.py 
# A program that determines the distance between two (non-vertical) points.

import math

def main():
    print("This program determines the distance between two (non-vertical) points: (x1,y1) and (x2,y2)")
    print()

    x1,y1,x2,y2= eval(input("Please enter the value of (x1,y1,x2,y2) with comma in between:"))
    
    distance=math.sqrt ((x2-x1)**2+(y2-y1)**2)

    print()
    print("The distance between the two points is", distance )

main()

8.
    # epact.py 
    # A program that determines the Gregorian epact.

    def main():
	print ("This program determines the Gregorian epact")
	year = eval(input("The 4-digit year is: "))
	C = year // 100
	epact=(8 + (C//4)-C + ((8*C + 13)//25) + 11*(year%19))%30
	print ()
	print ("The Gregorian epact for this year is ", epact)
    
    main()

9.
# TriangleArea.py 
# A program that determines the area of a triangle.

import math

def main():
    print("This program determines the area of a triangle with three sides a, b, and c")
    print()

    a,b,c= eval(input("Please enter the value of (a,b,c) with comma in between:"))
    
    s=(a+b+c)/2

    A=math.sqrt (s*(s-a)*(s-b)*(s-c))

    print()

    print("The area of the triangle is", A)

main()

10.
# LadderLength.py 
# A program that determines the length of a ladder required to reach a given height when leaned against a house.

import math

def main():
    print("This program determines the length of a ladder required to reach a given height when leaned against a house")
    print()

    height = eval(input("The height of the house is: "))
    degrees = eval(input("The angle of the ladder in degree is: "))
    
    angle = math.pi*degrees/180

    length = height/math.sin (angle)

    print()

    print("The length of the ladder required to reach the house is ", length)

main()

11.
    # SumNatureNumbers.py
    # Program to compute the sum of the first n natural numbers.

    def main():
	print("This program find the sum of the first n natural numbers")
	print()
	n = eval(input("Please enter the value of n: "))
	fact = 0
	for factor in range(n,0,-1):   ###How else might you have used range() to iterate your for loop?
		fact = fact + factor
	print("The sum of the first", n, "natural numbers", "is", fact)

    main()

12.

    # SumCubesNatureNumbers.py
    # Program to compute the sum of the cubes of the first n natural numbers.

    def main():
	print("This program find the sum of the cubes of the first n natural numbers")
	print()
	n = eval(input("Please enter the value of n: "))
	fact = 0
	for factor in range(n,0,-1):
		fact = fact + factor*factor*factor  ###Definitely want to use exponentiation here.
	print("The sum of the cubes of the first", n, "natural numbers", "is", fact)

    main()

13. 