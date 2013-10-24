# Import library
import math

#Question 1
def VolAndAreaOfSphere():
    rad = eval(input("Enter the radius of your sphere: "))
    #The choice of three digits after the decimal is arbitrary
    print("The volume of your sphere is ", round(4*(rad**3)*math.pi/3,3), " units")
    print("The surface area of your sphere is ", round(4*math.pi*(rad**2),3)," units")
    
VolAndAreaOfSphere()

#Question 2
def CostByAreaOfPizza():
    r = eval(input("Enter the diameter of your pizza: "))/2
    c = eval(input("Enter the cost of your pizza: "))
    print("The cost per unit area is $", round(math.pi*(r**2)/c,2))

CostByAreaOfPizza()

#Question 3
def MolMassOfHydrocarbon():
    h = eval(input("Enter the number of hydrogen atoms: "))
    c = eval(input("Enter the number of carbon atoms: "))
    o = eval(input("Enter the number of oxygen atoms: "))
    #Match significant figures
    print("The molecular mass of your hydrocarbon is", round(((h*1.0079)+(c*12.011)+(o*15.9994)),4), "amu")

MolMassOfHydrocarbon()

#Question 4
def TimeElapsed():
    t = eval(input("Enter the delay between lightning and thunder in seconds: "))
    #Ignore the effect of the time it takes for light to travel, on the order of microseconds
    print("The distance of the lightning is", round(t*1100/5280,1),"miles or", round(t*1100), "feet")

TimeElapsed()

#Question5
def CostOfCoffee():
    w = eval(input("Enter the weight of coffee you require, in pounds: "))
    #Calculate shipping
    ship_price = 1.5 + (w*0.86)
    #Coffee itself
    coffee_price = 10.5*w
    #Total
    price = round(ship_price + coffee_price,2)
    print("The cost of your order is $",price)

CostOfCoffee()

#Question 6
def GetSlope():
    #Easiest to get the input this way, and practical as well
    x1 = eval(input("Enter the x-coordinate of the first point: "))
    y1 = eval(input("Enter the y-coordinate of the first point: "))
    x2 = eval(input("Enter the x-coordinate of the second point: "))
    y2 = eval(input("Enter the x-coordinate of the second point: "))
    #Might as well do this
    if(x1 == x2):
        print("The slope cannot be computed")
    else:
        print("The slope is", round(((y2-y1)/(x2-x1)),2))

GetSlope()

#Question 7
def GetDistance():
    #Easiest to get the input this way, and practical as well
    x1 = eval(input("Enter the x-coordinate of the first point: "))
    y1 = eval(input("Enter the y-coordinate of the first point: "))
    x2 = eval(input("Enter the x-coordinate of the second point: "))
    y2 = eval(input("Enter the x-coordinate of the second point: "))
    #Calculate sum of squares
    s_o_s = ((x2-x1)**2) +((y2-y1)**2)
    #Get square root
    distance = s_o_s**(1/2)
    print("The distance between the points is", round(distance,2),"units")

GetDistance()

#Question 8
def GetEpact():
    year = eval(input("Enter 4 digit year: "))
    C = year//100
    epact = (8 + (C//4) - C + ((8*C+13)//25) + (11*(year%19)))%30
    print("The Gregorian epact is", epact, "days")

GetEpact()

#Question 9
def GetTriangleArea():
    a = eval(input("Enter the length of one side of your triangle: "))
    b = eval(input("Enter the length of another side of your triangle: "))
    c = eval(input("Enter the length of the third side of your triangle: "))
    #calculate semiperimeter
    s = (a+b+c)/2
    #apply Heron's formula
    area = ((s)*(s-a)*(s-b)*(s-c))**(1/2)
    print("The area of your triangle is", round(area,2), "square units")

GetTriangleArea()

#Question 10
def GetLadderLength():
    angle = eval(input("Enter the angle in degrees: "))
    rad_angle = angle*math.pi/180
    height = eval(input("Enter the height you need: "))
    lad_length = height/(math.sin(rad_angle))
    print("The length of the ladder required is", math.ceil(lad_length), "units")

GetLadderLength()

#Question 11
def GetSum():
    n = eval(input("Enter the number of numbers, starting from 1, that you want summed: "))
    #Could also do this with a for-loop, but that would need more memory to store and update sums for each step I think.
    s = ((n)*(n+1))//2
    print("The sum is", s)

GetSum()

#Question 12
def GetSumOfCubes():
    n = eval(input("Enter the number of numbers, starting from 1, for which you want the sum of cubes: "))
    #Again, could also use for-loop
    s = (((n)*(n+1))//2)**2
    print("The sum is", s)

GetSumOfCubes()

#Question 13
def GetSumOfSeries():
    n = eval(input("Enter the number of numbers that you want summed: "))
    s = eval(input("Enter the first number: "))
    for i in range(n-1):
        number = eval(input("Enter the next number: "))
        s = s + number
    print("The sum is", s)

GetSumOfSeries()

#Question 14
def GetAverage():
    #This is basically the above program plus an extra step at the end
    n = eval(input("Enter the number of numbers that you want averaged: "))
    s = eval(input("Enter the first number: "))
    for i in range(n-1):
        number = eval(input("Enter the next number: "))
        s = s + number
    print("The average is", round(s/n,2))

GetAverage()

#Question 15
def GetPi():
    #Again, a slight modification to 13
    n = eval(input("Enter the number of terms in the series you want evaluated: "))
    s = 0
    for i in range(0,n):
        number = (4/((2*i)+1))*((-1)**i)
        s = s + number
        #Can test the program by asking it to print s and/or number here
    print("The approximated value of pi obtained is", round(s,6))
    print("The difference from the actual value is", math.pi-s)
    print("The accuracy is", abs(round(((math.pi-s)*100)/math.pi,2)), "%")

GetPi()

#Question 16
def GetNthFibonacci():
    #Again, very similar
    n = eval(input("Enter the term of the Fibonacci sequence you want: " ))
    current_term = 1
    prev_term = 1
    #There is probably a more elegant solution but this is serviceable
    if(n==1):
        print("The term is 1")
    elif(n==2):
        print("The term is 1")
    else:    
        for i in range(2,n):
            s = prev_term + current_term
            prev_term = current_term
            current_term = s
        print("The term is", s)

GetNthFibonacci()

#Question 17
def GetSqrt():
        x = eval(input("Enter the number you want to find the square root of: "))
        n = eval(input("Enter the number of interations you want: "))
        guess = x/2
        for i in range(n):
            guess = (guess + (x/guess))/2
        print("The estimated square root is", round(guess,6))
        print("The actual square root is", round(math.sqrt(x),6))
        print("The error is", abs(round(((guess-math.sqrt(x))*100)/math.sqrt(x),2)), "%")

GetSqrt()
