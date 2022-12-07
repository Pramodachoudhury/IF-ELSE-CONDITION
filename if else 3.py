#----------------------61-----------------
#WAP to calculate the electricity bill (accept number of unit from user)to the following criteria:
#unit                                    price
#first 100 units                        0
#next 100 units                     rs. 5 per/unit
#after 200 units                    rs. 10 per/unit
u=int(input('enter a unit of a month:'))
if u>0 and u<=100:
    print('the bill is 0')
elif (u>100) and (u<=200):
    amount_charge=(u-100)*5
    print('the bill is :',amount_charge)
elif u>200:
    amount_charge1=(u-200)*10+500
    print('the bill is :',amount_charge1)
else:
    print('the input is out of range')

#---------------------62-----------------
#A company decided to give  bonous to employee according to following criteria:
#       time period of service                          bonous
#       more than 10 years                              10%
#       >=6 and <1=10 years                           8%
#       less than 6 years                                   5%
#ask the user their salary and years of services and print the net bonus amount:?????
"""salary= int(input('enter a salary'))
year=int(input('enter a years'))
if year>10:
    bonous=salary*(10/100)
    print('the net bonous  amount of a salary is :',bonous)
elif (year>=6) and (year<=10):
    bonous1=salary*(8/100)
    print('the net bonous amount of a salary is:',bonous1)
elif year<=6:
    bonous2=salary*(5/100)
    print('the net bonous amount of a salary is :',bonous2)"""
#-------------63------------------------
#accept the number of days from the user and calculate the charge for  library according to following
#till five days: rs.2/day:
#six to ten days: rs.3/day:
#11 to 15 days : rs.4/day:
#after 15 days : rs 5/day:
"""n=int(input('enter a number of days:'))
if n<5:
    charges=(n*2)
    print('the no. of charges is:',charges)
elif(n>=6) and (n<10):
    charges=n*3
    print('the no. of charges ix:',charges)
elif(n>=11) and (n<=15):
    charges=n*4
    print('the no. of charges is:',charges)
elif(n>15):
    charges=n*5
    print('the no. of charges is:',charges)"""

    











    
