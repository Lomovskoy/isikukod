import datetime
 
def year(z):
    z = str(z)
    if len(z) == 1:
        if int(z) == 1:
            return (u' год')
        if 1 < int(z) < 5:
            return (u' года')
        if 4 < int(z) < 21 or int(z) == 0:
            return (u' лет')
    if len(z) > 1:
        buff = int(z[-2:])
        if 0 <= buff <= 20:
            return (u' лет')
        elif int(str(buff)[1]) == 1:
            return (u' год')
        elif 1 < int(str(buff)[1]) < 5:
            return (u' года')
        elif int(str(buff)[1]) > 4:
            return (u' лет')
 
print(u'Введите свой день рождения (дд. мм. гггг)')
x = raw_input()
while ':' in x or '-' in x or ',' in x or ';' in x or '/' in x or ' ' in x:
    x = x.replace(':','.')
    x = x.replace(',','.')
    x = x.replace(';','.')
    x = x.replace('/','.')
    x = x.replace(' ','.')
 
x = (x.split('.'))
 
age_day = str((datetime.date.today()) - (datetime.date(int(x[2]),int(x[1]),int(x[0]))))
if age_day == '0:00:00':
    print(u'Поздравляем с прибытием в этот мир!')
else:
    age_day = int(age_day[:age_day.find('d')-1])
    if age_day >= 0:
        print (u'Вам '+(str(int(age_day/365.25)))+year(int(age_day/365.25)))
    else:
        print(u'Вы еще не родились')
 
print(u'Для выхода нажмите Enter')
raw_input()
