
cadbury = (15)
cadburybox = cadbury + 5 
print('You have' ,cadburybox, 'choclates')



CadburyMilk=6
CadburyDark=5
CadburyWhite=8
cadburymilk= ('milk chocolates')
cadburydark= ('dark chocolates')
cadburywhite= ('white chocolates') 
cadburylist= [['milk',5,],['dark',8],['white',3]] 
import pandas
dir(pandas)
cadburydf=pandas.DataFrame(cadburylist,columns=('Type Of Chocolate','Quantity'))
print(cadburydf)

name=input('Please enter your name')
print('Your name is',name)

age= int(input())

print('You are' ,age, 'years old')

chocolate1={'cadburymilk':5}
chocolate2={'cadburydark':8}
chocolate3={'cadburywhite':3}
print('There are' ,chocolate1, ',' ,chocolate2, ',and' ,chocolate3, 'in the box')
S={'Steve':32,'Lia':28, 'Vin':45, 'Katie':38 }
print('These are the name and ages of the people:' ,S,'.')

studentlist= [['Steve',32,'M',],['Lia',28,'F'],['Vin',45,'M'], ['Katie',38,'F']]
import pandas
dir(pandas)

studentdf = pandas.DataFrame(studentlist,columns=('Name','Age','Gender'),rows=('1','2','3'))
print(studentdf)
