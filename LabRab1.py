##Напишите программу, в которой пользователь вводит число от 0 до 9 включительно,
##а программа выводит название введённого числа, а если второй входной аргумент type имеет значение bin, oct,hex,
##то функция преобразует это число в бинарную, восьмеричную или шестнадцатеричную форму.
##Предусмотреть проверку корректности введённого пользователем значения. При реализации должны использоваться декораторы. 
##При реализации должны использоваться декораторы (но можно обойтись и без них). 
##Предусмотрите обработку исключительных ситуаций. Напишите тесты с использованием assert



def vvedennoechislo(a, atype):
  if (a==0):
    print("Ноль")
  elif (a==1):
    print("Один")
  elif (a==2):
    print("Два")
  elif (a==3):
    print("Три")
  elif (a==4):
    print("Четыре")
  elif (a==5):
    print("Пять")         
  elif (a==6):
    print("Шесть")
  elif (a==7):
    print("Семь")
  elif (a==8):
    print("Восемь")
  elif (a==9):
    print("Девять")
  else:
    print("Вы ввели не то число")


  if atype == 'bin':
        print(bin(a))
  elif atype == 'oct':
        print(oct(a))
  elif atype == 'hex':
        print(hex(a))
    
vvedennoechislo(2,'oct')        

##def vvedennoechislo():
##assert vvedennoechislo(6,'oct') == ('Шесть','0o6')
##assert vvedennoechislo(5,'oct') == ('Пять','0o5')
##assert vvedennoechislo(1,'hex') == ('Один','0x1')


![Иллюстрация к проекту](https://github.com/herzenuni/sem5-firsttask-04092018-KsushaSeliv/blob/master/Lab1.JPG
