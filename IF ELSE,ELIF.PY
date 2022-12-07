#32-WAP to print weather the given number is positive or negative?
"""n=int(input("enter a number:"))
if n>0:
    print('its apositive number')
if n<0:
    print('its a negative number')
if n==0:
    print('its a zero number')"""
#33- WAP to print weather its even number or odd number?
"""n=int(input('enter a number:'))
if n%2==0:
    print('its a even number')
if n%2!=0:
    print('its a odd number')"""
#34- WAP to print weather its even number or odd number?
"""n=int(input('enter a number:'))
if n%2==0:
    print('its a even number')
else :
    print('its a odd number')"""
#35-WAP to print weather the given number is positive or negative and zero?
"""n=int(input("enter a number:"))
if n>0:
    print('its apositive number')
elif n<0:
    print('its a negative number')
elif n==0:
    print('its a zero number')"""
#36-WAP to print the grade of a student using IF-ELSE?
"""n=int(input('enter a number'))
if n>90:
    print('the student is excelent')
elif n>=60 and n<=90:
    print('the student is 1st division')
elif n>=35 and n<=60:
    print('the student is 2nd division')
else:
    print('the student is fail')"""
#37-In this exercise you will create a program that reads a letter of the alphabet from the user.
#If the user enters a, e, i, o or u then your program should display a message indicating
#that the entered letter is a vowel. If the user enters y then your program should display a
#message indicating that sometimes y is a vowel, and sometimes y isa consonant. Otherwise
#your program should display a message indicating that the letter is a consonant.
"""a=str(input('enter a Alphabet :'))
if (a=='a'or a=='i' or a=='e' or a=='o' or a=='u'):
    print('its VOWEL')
else :
    print('its CONSOTANT')"""
#38-Write a program that determines the name of a shape from its number of sides. Read
#the number of sides from the user and then report the appropriate name as part of
#a meaningful message. Your program should support shapes with anywhere from 3
#up to (and including) 10 sides. If a number of sides outside of this range is entered
#then your program should display an appropriate error message
"""v=int(input('enter a side:'))
if v==3:
    print('triangle')
elif v==4:
    print('square')
elif v==5:
    print('pentagon')
elif v==6:
    print('hexagon')
elif v==7:
    print('septagon')
elif v==8:
    print('octagon')
elif v==9:
    print('nanogon')
elif v==10:
    print('decagon')
else:
    print('invalid')"""
#39-The length of a month varies from 28 to 31 days. In this exercise you will create a program
#that reads the name of a month from the user as a string. Then your program should display
#the number of days in that month. Display '28 or 29 days' for February so that leap years are addressed
"""month = input ("Enter the name of a month: ")
if month == 'April' or month == 'June' or month == 'September' or month == 'November':
    print('the month of days is :31')
elif month=='january' or month=='march' or month=='may' or month=='july' or name=='august' or name=='octber' or name=='december':
    print('the month of days is :30')
elif month == "February":
    print('the month of dates is : 28 or 29')
else :
    print('the month is int list ')"""
#40-The following table lists the sound level in decibels for several common noises.
#Noise Decibel level (dB)
#Jackhammer 130
#Gas lawnmower 106
#Alarm clock 70
#Write a program that reads a sound level in decibels from the user. If the user
#enters a decibel level that matches one of the noises in the table then your program
#should display a message containing only that noise. If the user enters a number
#of decibels between the noises listed then your program should display a message
#indicating which noises the level is between. Ensure that your program also generates
#reasonable output for a value smaller than the quietest noise in the table, and for a
#value larger than the loudest noise in the table
"""d=float(input('enter anumber of decibels:'))
if d>0 and d<40:
    print('quiter than a quite room')
elif d==40:
    print('the same as quite room')
elif d>40 and d<70:
    print('the noise between quite room and alaram lock')
elif d==70:
    print('the same as alaram clock')
elif d>70 and d<106:
    print('the noise between alaram and gas lawnmower')
elif d==106:
    print('the same as gas lawnmower')
elif d>106 and d<130:
    print('the noise between gas lawnmower and jackhammer')
elif d==130:
    print('the same as jackhammer')
else:
    print(' the too loud')"""
#41--A triangle can be classified based on the lengths of its sides as equilateral, isosceles or scalene.
#All 3 sides of an equilateral triangle have the same length. An isoscelestriangle has two sides that are
#the same length, and a third side that is a differentlength. If all of the sides have different lengths then
#the triangle is scalene. Write a program that reads the lengths of 3 sides of a triangle from the user.
#Display a message indicating the type of the triangle.

"""x=int(input('enter 1st lenght of a triangle:'))
y=int(input('enter 2nd length of a triangle:'))
z=int(input('enter 3rd length of a triangle:'))
if x==y==z :
    print('the triangle is equilateral')
elif x==y or y==z or z==x:
    print('the triangle is isosceles')
else:
    print('the triangle is scalene')"""
#45Canada has three national holidays which fall on the same dates each year.
#Holiday Date
#New year’s day January 1
#Canada day July 1
#Christmas day December 25
#Write a program that reads a month and day from the user. If the month and day
#match one of the holidays listed previously then your program should display the
#holiday’s name. Otherwise your program should indicate that the entered month and
#day do not correspond to a fixed-date holiday.----------------------------------
"""x=str(input('enter a month :'))
y=int(input('enter a day :'))
if x=='January' and y== 1:
    print('the new years holiday')
elif x=='July' and y== 1:
    print('the canada day')
elif x=='December' and y== 25:
    print('the christmass day')
else:
    print('the enter month & day do not correspond to fixed-date holiday')"""
#-46----Write a program that reads a position from the user. Use an if statement to determine
#if the column begins with a black square or a white square. Then use modular arithmetic
#to report the color of the square in that row. For example, if the user enters
#a1 then your program should report that the square is black. If the user enters d5
#then your program should report that the square is white. Your program may assume
#that a valid position will always be entered. It does not need to perform any error checking.

"""r=int(input('enter a row no:'))
c=int(input('enter a column no:')) 
if r%2==0 and c%2==0:
	print("black")
elif r%2!=0 and c%2!=0:
	print("black")
else:
	print("white")"""
  #48--------------------------------------------------------------------------------------     
"""set1=['a','c','e','g']
set2=['b','d','f','h']
r=str(input('enter a row alphabet:'))
c=str(input('enter a column alphabet:'))
if(r in set1) and (c in set1):
    print('the colour is black')
elif(r in set2) and (c in set2):
    prinr('the colour is black')
else:
    print('the colour is white')"""
#(49)-The horoscopes commonly reported in newspapers use the position of the sun at the
#time of one’s birth to try and predict the future. This system of astrology divides the
#year into twelve zodiac signs, as outline in the table below:
#Zodiac sign Date range
#Capricorn December 22 to January 19
#Aquarius January 20 to February 18
#Pisces February 19 to March 20
#Aries March 21 to April 19
#Taurus April 20 to May 20#
#Gemini May 21 to June 20
#Cancer June 21 to July 22
#Leo July 23 to August 22
#Virgo August 23 to September 22
#Libra September 23 to October 22
#Scorpio October 23 to November 21
#Sagittarius November 22 to December 21
#Write a program that asks the user to enter his or her month and day of birth. Then
#your program should report the user’s zodiac sign as part of an appropriate output message.
"""m=input('enter a birth of month:')
d=int(input('enter a birth of day:'))
if (m=='dec' or m=='jan') and (d<=19 or d>=22):
    print('capricon')
elif (m=='jan' or m=='feb') and (d<=18 or d>=20):
    print('aquarius')
elif (m=='feb' or m=='mac') and (d<=19 or d>=20):
    print('pisces')
elif (m=='mac' or m=='april') and (d<=19 or d>=21):
    print('aries')
elif (m=='april' or m=='may') and (d<=20 or d>=20):
    print('taurus')
elif (m=='may' or m=='jun') and (d<=20 or d>=21):
    print('gemini')
elif (m=='jun' or m=='jul') and (d<=22 or d>=21):
    print('cancer')
elif (m=='jul' or m=='aug') and (d<=22 or d>=23):
    print('leo')
elif (m=='aug' or m=='sep') and (d<=22 or d>=23):
    print('vigro')
elif (m=='sep' or m=='oct') and (d<=22 or d>=23):
    print('libra')
elif (m=='oct' or m=='nov') and (d<=21 or d>=23):
    print('scorpio')
elif (m=='nov' or m=='dec') and (d<=21 or d>=22):
    print('sagittarius')"""

#The following table contains earthquake magnitude ranges on the Richter scale and
#their descriptors:
#Magnitude Descriptor
#Less than 2.0 Micro
#2.0 to less than 3.0 Very minor
#3.0 to less than 4.0 Minor
#4.0 to less than 5.0 Light
#5.0 to less than 6.0 Moderate
#6.0 to less than 7.0 Strong
#7.0 to less than 8.0 Major
#8.0 to less than 10.0 Great
#10.0 or more Meteoric
#Write a program that reads a magnitude from the user and displays the appropriate
#descriptor as part of a meaningful message. For example, if the user enters 5.5 then
#your program should indicate that a magnitude 5.5 earthquake is considered to be a moderate earthquake
"""d=float(input('enter a magnitude :'))
if d>0 and d<2.0:
    print('the magnitude is micro')
elif d>2.0 and d<3.0:
    print('the magnitude is very minor')
elif d>3.0 and d<4.0:
    print('the magnitude is minor')
elif d>4.0 and d<5.0:
    print('the magnitude is light')
elif d>5.0 and d<6.0:
    print('the magnitude is modarate')
elif d>6.0 and d<7.0:
    print('the magnitude is strong')
elif d>7.0 and d<8.0:
    print('the magnitude is major')
elif d>8.0 and d<10.0:
    print('the magnitude is great')
elif d>10.0:
    print('the magnitude is meteroic')
else:
    print(' the too loud')"""
#--------------51-----------------------------
"""a=int(input('enter x*x coefficient:'))
b=int(input('enter a x cofficient:'))
c=int(input('enter the constant:'))
d=(b*b)-(4*a*c)
if d>0:
    root1=(-b+(d**0.5))/(2*a)
    root2=(-b-(d**0.5))/(2*a)
    print('the square root of equation is ',root1,root2)
else:
    print('the roots are complex')"""
   













    
          
    








