#На основе созданного в рамках лабораторного занятия 1 программного кода напишите фрагмент кода (класс)
#для обработки исключительных ситуаций, которые могут возникнуть в процессе выполнения кода (см. задание ЛР 1), упомянутого выше.

#Например один из вариантов:

#1) напишите класс для обработки исключений RangeException, для обработки исключения, которое возникает в ситуации,
#когда вводится число не из описанного в условии диапазона;
#2) напишите класс для обработки исключений ConvertTypeException, для обработки исключения,
#которое возникает в ситуации, когда пользователь выбрал тип не из списка обозначенного в условии задачи.






class RangeException(Exception):
  def __init__(self,text):
        RangeException.txt = text


try:
    a = int(input('Введите число от 0 до 9 включительно:'))
    if ((a<0) | (a>9)):
      raise RangeException('Число не подходит')
      
except RangeException:
    print('Число не подходит')
    a = int(input('Введите число от 0 до 9 включительно:'))

except ValueError:
    print('Число не подходит')
    a = int(input('Введите число от 0 до 9 включительно:'))

atype = input('bin, oct, hex:')



def vvedennoechislo():
  
    if (a == 0):
      print("Ноль")
    elif (a == 1):
      print("Один")
    elif (a == 2):
      print("Два")
    elif (a == 3):
      print("Три")
    elif (a == 4):
      print("Четыре")
    elif (a == 5):
      print("Пять")
    elif (a == 6):
      print("Шесть")
    elif (a == 7):
      print("Семь")
    elif (a == 8):
      print("Восемь")
    elif (a == 9):
      print("Девять")
    else:
      print("Начните сначала")


    if atype == 'bin':
      print("Ответ: ", bin(a))
    elif atype == 'oct':
      print("Ответ: ", oct(a))
    elif atype == 'hex':
      print("Ответ: ", hex(a))
      
vvedennoechislo()

#def vvedennoechislo():
#assert vvedennoechislo(6,'oct') == ('Шесть','0o6')
#assert vvedennoechislo(5,'oct') == ('Пять','0o5')
#assert vvedennoechislo(1,'hex') == ('Один','0x1')

