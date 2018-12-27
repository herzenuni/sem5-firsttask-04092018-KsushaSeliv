#Для программы, сделанной в рамках лабораторной работы 1 и 2, реализуйте с использованием механизма
#декораторов (предпочтительно) или без него (в этом случае будет необходимо использовать еще один аргумент) функционал для
#сохранения истории вычислений функции в файл. 
#При записи в файл предусмотреть вероятность возникновения исключительных ситуаций и создать собственный 
#класс или классы для обработки исключительных ситуаций при записи в файл. 

class RangeException(Exception):
    def __init__(self, text):
        RangeException.txt = text
        
logger = [] #Модуль Logging позволяет вести журнал диагностики, который регистрирует события, связанные с работой приложений, 
#а также ведение журнала аудита, который регистрирует события операций пользователя для анализа.
#Особенно используется для записи событий в файл.

try:
    a = int(input('Введите число от 0 до 9 включительно:'))
    if ((a < 0) | (a > 9)):
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
        print("Ответ:", bin(a))
    elif atype == 'oct':
        print("Ответ:", oct(a))
    elif atype == 'hex':
        print("Ответ:", hex(a))


vvedennoechislo()


if len(logger) == 1:   
     logger.append("Отсутствие исключений")
try:
      with open('text.txt', 'a') as f:
        f.write(str(logger) + "\n")
        f.write("Число: " + str(a) + " Система счисления: " +str(atype))
except IOError: #Возбуждается, когда операция ввода-вывода (например, при использовании print() или open()) не проходит. 
#Например: «файл не найден», «диск заполнен» и т.п..
      print("Что-то пошло не так")