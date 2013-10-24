Yi Zhou (EID:yz4439)


1.
# sphere.py
# A program that computes the volume and surface area of a sphere.

import math

def main():
    print("This program calculates the volume and surface area of a sphere")
    r = eval(input("Please enter the radius of the sphere: "))
    V=4/3*math.pi*r*r*r
    A=4*math.pi*r*r
    print()
    print("The volume and surface area of the sphere are", V, "and", A, "respectively")

main()

2.
# Pizzacost.py
# A program that computes the cost per square inch of a circular pizza.


import math

def main():
    print ("This program calculates the cost per square inch of a circular pizza")
    r = eval(input("The radius of the pizza is: "))
    TotalCost = eval(input("The cost of the pizza is: "))
    A = math.pi*r*r
    B = TotalCost/A
    print()
    print("The cost per square inch of the circular pizza is", B)

main()

3.

    # Molecularweight.py
    # A program that computes the molecular weight of a hydrocarbon.

    def main():
	 print("This program determines the molecular weight of a hydrocarbon")
	 print("Please enter the number of hydrogen, carbon, and oxygen atoms")
	 H = eval(input("H: "))
	 C = eval(input("C: "))
	 O = eval(input("O: "))
	 Weight=1.0079*H+12.011*C+15.9994*O
         print()
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

    x1,y1,x2,y2= eval(input("Please enter the value of (x1,y1,x2,y2) with comma in between:"))
    
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
	for factor in range(n,0,-1):
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
		fact = fact + factor*factor*factor
	print("The sum of the cubes of the first", n, "natural numbers", "is", fact)

    main()

13. 
    
    # SumNumbers.py
    # Program to sum a series of numbers entered by the user.
###Your indentation is a mess here.


    def main():
        print ("This program sums a series of numbers entered by you")
	n = eval(input("Please enter how many numbers you want to sum: "))
	number = eval(input("Please enter the first number: "))  ###How might you have written your code to eliminate this and the next line?
	sum = number
	for i in range (1, n):
		number = eval(input("Please enter the next number: "))
		sum = sum + number
	print ()
	print ("The sum of these numbers is ", sum)
	
    main()

14. 
    # AverageNumbers.py
    # Program to calculate the average of a series of numbers.

    def main():
	print ("This program calculates the average of a series of numbers enterd by you")
	n = eval(input("Please enter how many numbers you have: "))
	number = eval(input("Please enter the first number: "))
	sum = number
	for i in range (1, n):
		number = eval(input("Please enter the next number: "))
		sum = sum + number
	average = sum/float(n)  ###You didn't need to convert n to a float.  Do you know why?
	print ()
	print ("The average of these numbers is ", average)

    main()


15. 
    # Pivalue.py
    # Program that approximates the value of pi.

    import math

    def main():
	print (" This program approximates the value of pi by summing n terms of 4*(-1)**(n+1)/(2n-1) and evaluate how different it is from math.pi")
	n = eval(input("please enter the value of n: "))
	pi=0
	for m in range (1,n+1,1):
		pi=pi+(-1)**(m+1)*4/(2*m-1)
		difference = pi - math.pi
	print ()
        print(" The approximate value of pi is", pi, "and its difference from math.pi is", difference)

    main()


16.

    # Fibonaccinumber.py
    # Program that determines the nth Fibonacci number of a classical Fibonacci sequence.
   
    def main():
	print ("This program determines the nth Fibonacci number of a classical Fibonacci sequence")
	n = eval(input("please enter the value of n higher than 3: "))
	a,b=1,1
	for i in range (3, n+1):
		c=a+b
		a=b
		b=c
	print()
	print (" The", n, "th Fibonacci number in a classical Fibonacci sequence is ", c)
    
    main()

17.

    # GuessRoot.py
    # Program that guesses the square root of a number.

    import math

    def main():
	print ("This program guesses the square root of a number x")
	x = eval(input("please enter the value of x higher than 0: "))
	n = eval(input("please enter the times of guesses: "))
	guess = x/2
	for i in range (2, n+1):
		guess = (guess + x/guess)/2
	difference = guess - math.sqrt(x)

	print ()
	print ("The approximate square root of", x, "obtained after", n, "times of guesses is", guess, "and its difference from math.sqrt is", difference)

   main()