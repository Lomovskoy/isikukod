from datetime import datetime, date, time
def check(x):
    while (x.isdigit() != True) or (len(x) != 11):
        x=input('Enter the correct Isikukood: ')
    mas=[0]*11
    for i in range(0,11):
        mas[i]=int(x[i])
    return(mas)
#-------------------------------------------------------------------------------
def gender(y):
    flag = True
    while flag:
        if y[0]%2 == 1 and y[0] <= 8:
            gen ='male'
            print('Your gender: ',gen)
            flag = False
        elif y[0]%2 == 0 and y[0] <= 8:
            gen ='female'
            print('Your gender: ',gen)
            flag = False
        else:
            x=input('Enter the correct Isikukood: ')
            y = check(x)
    return gen
#------------------------------------------------------------------------------
def yearfan(z):
    if z[0] == 1 or z[0] == 2:
        year = [1,8]
        #print('Your date of birth: ',z[5],z[6],' day ',z[3],z[4],' month ',year[0],year[1],z[1],z[2],' year', sep = '')
        print('Your date of birth: {}{} day {}{} month {}{}{}{} year'.format(z[5],z[6],z[3],z[4],year[0],year[1],z[1],z[2]))
    elif z[0] == 3 or z[0] == 4:
        year = [1,9]
        print('Your date of birth: {}{} day {}{} month {}{}{}{} year'.format(z[5],z[6],z[3],z[4],year[0],year[1],z[1],z[2]))
        #print('Your date of birth: ',z[5],z[6],' day ',z[3],z[4],' month ',year[0],year[1],z[1],z[2],' year', sep = '')
    elif z[0] == 5 or z[0] == 6:
        year = [2,0]
        print('Your date of birth: {}{} day {}{} month {}{}{}{} year'.format(z[5],z[6],z[3],z[4],year[0],year[1],z[1],z[2]))
        #print('Your date of birth: ',z[5],z[6],' day ',z[3],z[4],' month ',year[0],year[1],z[1],z[2],' year', sep = '')
    else:
        year = [2,1]
        print('Your date of birth: {}{} day {}{} month {}{}{}{} year'.format(z[5],z[6],z[3],z[4],year[0],year[1],z[1],z[2]))
        #print('Your date of birth: ',z[5],z[6],' day ',z[3],z[4],' month ',year[0],year[1],z[1],z[2],' year', sep = '')
    dat=[int(str(z[5])+str(z[6])),int(str(z[3])+str(z[4])),int(str(year[0])+str(year[1])+str(z[1])+str(z[2]))]
    return dat
#------------------------------------------------------------------------------
def leapYear(g):
    if (g%4 == 0) and (g%100 != 0):
        vis = True
        #print(g)
    else:
        vis = False
    return(vis)
#------------------------------------------------------------------------------
def agefan(t):
    dat = str(datetime.date(datetime.now(tz=None)))
    x = 0
    y = 0
    mas1 = []
    year = [31,28,31,30,31,30,31,31,30,31,30,31]
    #visyear = [31,29,31,30,31,30,31,31,30,31,30,31]
    for i in range(0,10):
        if dat[i].isdigit() == True:
            mas1.append(int(dat[i]))
    mas2 = [int(str(mas1[6])+str(mas1[7])),int(str(mas1[4])+str(mas1[5])),int(str(mas1[0])+str(mas1[1])+str(mas1[2])+str(mas1[3]))]  
    print(t)
    print(mas2)
    if t[0] == mas2[0] and t[1] == mas2[1]:
        print('Happy Birthday!')
    if mas2[1]==2 and mas2[0]==year[1] or mas2[1]>2:
        y = 1
    for i in range(t[2],mas2[2]+y):
        if leapYear(i):
            if t[1]==2 and t[0]==year[1] or t[1]>2:
                x += 1
    #print('Высокосных дней за жизнь',x)
    if mas2[0]>=t[0] and mas2[1]>=t[1]:#если сейчас больше дней чем при рождении и месяц больше или равен
        itog = [mas2[0]-t[0]+x,mas2[1]-t[1],mas2[2]-t[2]]
        if itog[1]<0:
            itog[2] -=1
            itog[1] = (len(year) - abs(itog[1]))
        if itog[0]>year[itog[1]] and itog[1] < 12:
            itog[1] += 1
            itog[0] = year[itog[1]]-(itog[0]-(year[itog[1]+1]))
        elif itog[0]>year[itog[1]] and itog[1] == 12:
            itog[1] = 1
            itog[0] = year[itog[1]-1]-(itog[0]-(year[11]))
            itog[2] += 1
        elif itog[1] == 12:
            itog[1] = 1
            itog[2] += 1
            itog[0] = year[itog[1]-1]-itog[0]
        elif itog[0]>year[itog[1]] and itog[1] > 12:
            itog[1] = itog[1]-12
            if itog[1] == 0:
                itog[1] = 1
            itog[2] += 1
            itog[0] = year[itog[1]-1]-(itog[0]-(year[itog[1]-1]))
    elif mas2[0]>t[0] and mas2[1]<t[1]:#если сейчас больше дней чем при рождении и месяц меньше
        itog = [year[len(year)-t[1]]-t[0]+x,len(year)-t[1],mas2[2]-(t[2]+1)]
        if itog[1]<0:
            itog[2] -=1
            itog[1] = (len(year) - abs(itog[1]))
        if itog[0]>year[itog[1]] and itog[1] < 12:
            itog[1] += 1
            itog[0] = year[itog[1]]-(itog[0]-(year[itog[1]+1]))
        elif itog[0]>year[itog[1]] and itog[1] == 12:
            itog[1] = 1
            itog[0] = year[itog[1]-1]-(itog[0]-(year[11]))
            itog[2] += 1
        elif itog[1] == 12:
            itog[1] = 1
            itog[2] += 1
            itog[0] = year[itog[1]-1]-itog[0]
        elif itog[0]>year[itog[1]] and itog[1] > 12:
            itog[1] = itog[1]-12
            if itog[1] == 0:
                itog[1] = 1
            itog[2] += 1
            itog[0] = year[itog[1]-1]-(itog[0]-(year[itog[1]-1]))
    elif mas2[0]<t[0] and mas2[1]>=t[1]:#если сейчас меньше дней чем при рождении и месяц больше ил равен
        itog = [year[mas2[1]-(t[1]+1)]-t[0]+x,mas2[1]-(t[1]+1),mas2[2]-t[2]]
        if itog[1]<0:
            itog[2] -=1
            itog[1] = (len(year) - abs(itog[1]))
        if itog[0]>year[itog[1]] and itog[1] < 12:
            itog[1] += 1
            itog[0] = year[itog[1]]-(itog[0]-(year[itog[1]+1]))
        elif itog[0]>year[itog[1]] and itog[1] == 12:
            itog[1] = 1
            itog[0] = year[itog[1]-1]-(itog[0]-(year[11]))
            itog[2] += 1
        elif itog[1] == 12:
            itog[1] = 1
            itog[2] += 1
            itog[0] = year[itog[1]-1]-itog[0]
        elif itog[0]>year[itog[1]] and itog[1] > 12:
            itog[1] = itog[1]-12
            if itog[1] == 0:
                itog[1] = 1
            itog[2] += 1
            itog[0] = year[itog[1]-1]-(itog[0]-(year[itog[1]-1]))
    elif mas2[0]<t[0] and mas2[1]<t[1]:#если сейчас меньше дней чем при рождении и месяц меньше
        itog = [year[mas2[1]-(t[1]+2)]-t[0]+x,len(year)-t[1]+1,mas2[2]-(t[2]+1)]
        if itog[1]<0:
            itog[2] -=1
            itog[1] = (len(year) - abs(itog[1]))
        if itog[0]>year[itog[1]] and itog[1] < 12:
            itog[1] += 1
            itog[0] = year[itog[1]]-(itog[0]-(year[itog[1]+1]))
        elif itog[0]>year[itog[1]] and itog[1] == 12:
            itog[1] = 1
            itog[0] = year[itog[1]-1]-(itog[0]-(year[11]))
            itog[2] += 1
        elif itog[1] == 12:
            itog[1] = 1
            itog[2] += 1
            itog[0] = year[itog[1]-1]-itog[0]
        elif itog[0]>year[itog[1]] and itog[1] > 12:
            itog[1] = itog[1]-12
            if itog[1] == 0:
                itog[1] = 1
            itog[2] += 1
            itog[0] = year[itog[1]-1]-(itog[0]-(year[itog[1]-1]))
    print('Your age:',itog[2],'year',itog[1],'month',itog[0],'day')
    return itog
#------------------------------------------------------------------------------
def validity(x):
    weight1 = [1,2,3,4,5,6,7,8,9,1,0]
    weight2 = [3,4,5,6,7,8,9,1,2,3,0]
    summa = 0
    for i in range(len(x)):
        summa += (x[i]*weight1[i])
    summa = summa % 11
    if summa == x[10]:
        print('isikukood is correct')
        return (True)
    summa = 0
    for i in range(len(x)):
        summa += (x[i]*weight2[i])
    summa = summa % 11
    if summa == x[10]:
        print('isikukood is correct')
        return (True)
    if summa == 10:
        summa = 0
    if summa == x[10]:
        print('isikukood is correct')
        return (True)
    else:
        print('isikukood is not correct')
        return (False)
#==============================================================================   
print('='*31,'Isikukood program','='*30)
print('Autor: Lomovskoy Kirill\nGroup: KTVR - 16')
print('*'*80)
vvod = input('Enter your Isikukood: ')
print('-'*80)
IsKood = check(vvod)
IsCorrekt = validity(IsKood)
print('-'*80)
if IsCorrekt:
    Gend = gender(IsKood)
    print('-'*80)
    Year = yearfan(IsKood)
    print('-'*80)
    Age = agefan(Year)
    print('_'*80)


