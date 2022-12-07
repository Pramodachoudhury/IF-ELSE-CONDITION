#-54--At a particular company, employees are rated at the end of each year. The rating scale
#begins at 0.0, with higher values indicating better performance and resulting in larger
#raises. The value awarded to an employee is either 0.0, 0.4, or 0.6 or more. Values
#between 0.0 and 0.4, and between 0.4 and 0.6 are never used. The meaning associated
#with each rating is shown in the following table. The amount of an employee’s raise is $2400.00 multiplied by their rating.
#Rating          Meaning
#0.0                Unacceptable performance
#0.4                 Acceptable performance
#0.6 or more     Meritorious performance
#Write a program that reads a rating from the user and indicates whether the performance was unacceptable, acceptable or meritorious. The amount of the employee’s
#raise should also be reported. Your program should display an appropriate error message if an invalid rating is entered.
"""r=float(input("enter rating:"))
if r==0.0:
	print("unacceptable performance",r*2400)
elif r==0.4:
	print("acceptable performance",r*2400)
elif r>=0.6:
	print("meritorious performance",r*2400)
else:
	print("invalid rating")"""
#56-Electromagnetic radiation can be classified into one of 7 categories according to its
#frequency, as shown in the table below:
#Name                                Frequency range (Hz)
#Radio whaves                          Less than 3 × 109
#Microwaves                            3 × 109 to less than 3 × 1012
#Infrared light                           3 × 1012 to less than 4.3 × 1014
#Visible light                             4.3 × 1014 to less than 7.5 × 1014
#Ultraviolet light                       7.5 × 1014 to less than 3 × 1017
#X-rays                                      3 × 1017 to less than 3 × 1019
#Gamma rays                              3 × 1019 or more
#Write a program that reads the frequency of the radiation from the user and displays the appropriate name
"""f=float(input('enter the frequency:'))
if f<(3e9):
    print('radio waves')
elif f<=(3e9)and f<(3e12):
    print('microwaves')
elif f<=(3e12)and f<(4.3e14):
    print('infrared light')
elif f<=(4.3e14)and f<(7.5e14):
    print('visible light')
elif f<=(7.5e14)and f<(3e17):
    print('ultraviolet light')
elif f<=(3e17)and f<(3e19):
    print('x-ray')
elif f>=(3e19):
    print('gamma ray')
else:
     print('invalid frequency')"""
#-57--A particular cell phone plan includes 50 minutes of air time and 50 text messages
#for $15.00 a month. Each additional minute of air time costs $0.25, while additional
#text messages cost $0.15 each. All cell phone bills include an additional charge of
#$0.44 to support 911 call centers, and the entire bill (including the 911 charge) is subject to 5 percent sales tax
#Write a program that reads the number of minutes and text messages used in a
#month from the user. Display the base charge, additional minutes charge (if any),
#additional text message charge (if any), the 911 fee, tax and total bill amount. Only
#display the additional minute and text message charges if the user incurred costs in
#these categories. Ensure that all of the charges are displayed using 2 decimal places
"""m=int(input('enter the no. of minutes:'))
t=int(input('enter the no. of text:'))
base_charge=15
call_center_price=0.44
tax=0.05
if m<50 and t<50:
    price=15
    add_min_charge=0
    add_mes_charge=0
elif m>50:
    price1=(t-50)*0.25
    add_min_charge=price1
    add_mes_charge=0
elif t>50:
    price=(m-50)*0.15
    add_min_charge=0
    add_mes_charge=price1
total_price=base_charge+add_min_charge+add_mes_charge+call_center_price
total_tax=total_price*tax
bill=total_price+total_tax
print('the base charge is:',base_charge)
print('the additional min charges:',add_min_charge)
print('the additional message charges:',add_mes_charge)
print('call center charges:',call_center_price)
print('tax amount is:',total_tax)
print('total billis :',bill)"""
#58--Most years have 365 days. However, the time required for the Earth to orbit the Sun
#is actually slightly more than that. As a result, an extra day, February 29, is included
#in some years to correct for this difference. Such years are referred to as leap years.
#The rules for determining whether or not a year is a leap year follow:
#• Any year that is divisible by 400 is a leap year.
#• Of the remaining years, any year that is divisible by 100 is not a leap year.
#• Of the remaining years, any year that is divisible by 4 is a leap year.
#• All other years are not leap years.
#Write a program that reads a year from the user and displays a message indicating
#whether or not it is a leap year.
"""year=int(input('enter a year:'))
if (year%400==0):
    print('TRUE:')
elif (year%100==0):
    print('FALSE ')
elif (year%4==0):
    print('TRUE')
else:
    ('all the years are not a leap years:FALSE')"""
#59--Write a program that reads a date from the user and computes its immediate successor.
#For example, if the user enters values that represent 2013-11-18 then your program
#should display a message indicating that the day immediately after 2013-11-18 is
#2013-11-19. If the user enters values that represent 2013-11-30 then the program
#should indicate that the next day is 2013-12-01. If the user enters values that represent
#2013-12-31 then the program should indicate that the next day is 2014-01-01. The
#date will be entered in numeric form with three separate input statements; one for
#the year, one for the month, and one for the day. Ensure that your program works
#correctly for leap years
"""d=int(input('enter a date:'))
m=int(input('enter a month:'))
y=int(input('enter a year:'))
if d==31 and m==12:
    d=1
    m=1
    y+1
elif d==31:
    d=1
else:
    print(d,m,y,sep='-')"""

    
#60--In a particular jurisdiction, older license plates consist of three uppercase letters
#followed by three numbers. When all of the license plates following that pattern had
#been used, the format was changed to four numbers followed by three uppercase letters.
#Write a program that begins by reading a string of characters from the user. Then
#your program should display a message indicating whether the characters are valid
#for an older style license plate or a newer style license plate. Your program should
#display an appropriate message if the string entered by the user is not valid for either style of license plate.
plate=input('enter a number plate')
if  len (plate) == 6  and \
    plate[0] >= "A"   and  plate[0]    <=  "Z"   and  \
    plate[1] >= "A"   and  plate[1]    <=  "Z"   and  \
    plate[2] >= "A"   and  plate[2]    <=  "Z"   and  \
    plate[3] >= "0"   and  plate[3]    <=  "9"   and  \
    plate[4] >= "0"   and  plate[4]    <=  "9"   and  \
    plate[5] >= "0"   and  plate[5]    <=  "9":
   print ("The    plate   is  a  valid   older   style   plate.")
elif len (plate)  == 7  and  \
    plate[0] >= "0"   and  plate[0]    <=  "9"   and  \
    plate[1] >= "0"   and  plate[1]    <=  "9"   and  \
    plate[2] >= "0"   and  plate[2]    <=  "9"   and  \
    plate[3] >= "0"   and  plate[3]    <=  "9"   and  \
    plate[4] >= "A"   and  plate[4]    <=  "Z"   and  \
    plate[5] >= "A"   and  plate[5]    <=  "Z"   and  \
    plate[6] >= "A"   and  plate[6]    <=  "Z":
   print ("The    plate   is  a  valid   newer   style   plate.")
else :
   print ("The    plate   is  not   valid.")








 








