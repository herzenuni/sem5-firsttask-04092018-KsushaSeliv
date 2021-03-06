# sem5-firsttask-04092018

## Задача 1

Напишите программу, в которой пользователь вводит число от 0 до 9 включительно, а программа выводит название введённого числа, а если второй входной аргумент ```type``` имеет значение ```bin```, ```oct```,```hex```, то функция преобразует это число в бинарную, восьмеричную или шестнадцатеричную форму. Предусмотреть проверку корректности введённого пользователем значения. При реализации должны использоваться декораторы. 
При реализации должны использоваться декораторы (но можно обойтись и без них). 
Предусмотрите обработку исключительных ситуаций. 
Напишите тесты с использованием assert.

```python
#функция c аргументами: введённое число(a) и его тип ((bin, oct, hex)(atype))

def vvedennoechislo(a, atype): 
  
  #далее, проверяем, входит ли число, которое ввёл пользователь в нужный нам промежуток(0-9)
  
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
    
vvedennoechislo(8,'oct')        
vvedennoechislo(7,'bin') 
vvedennoechislo(2,'hex')

#немного тестов
def vvedennoechislo(): 
  assert (7,'bin') == ('Семь', '0b121'), 'Ошибка'
  assert (1,'oct') == ('Один', '0x1'), 'Ошибка'
  assert (2,'hex') == ('Два', '0o2'), 'Ошибка'
  assert (3,'bin') == ('Один', '011'), 'Ошибка'
  assert (2,'oct') == ('Два', '0x2'), 'Ошибка'
  
```
![alt](https://github.com/herzenuni/sem5-firsttask-04092018-KsushaSeliv/blob/master/10.JPG)


## Задача 2

#На основе созданного в рамках лабораторного занятия 1 программного кода напишите фрагмент кода (класс)
#для обработки исключительных ситуаций, которые могут возникнуть в процессе выполнения кода (см. задание ЛР 1), упомянутого выше.

```python
class RangeException(Exception): #создаём класс, наследуя Exeption, для обработки исключения,
#которое возникает в ситуации, когда вводится число не из описанного в условии диапазона(0-9);

#создаём конструктор с входным аргументом
  def __init__(self, text): 
        RangeException.txt = text

try:
    a = int(input('Введите число от 0 до 9 включительно:'))
    if ((a<0)|(a>9)):
      raise RangeException('Число не подходит') #если число не подходит, вылетает исключение
except RangeException: #прописываем наш тип исключения, он просто принтится
    print('Число не подходит')
    a = int(input('Введите число от 0 до 9 включительно:'))

except ValueError:
    print('Число не подходит')
    a = int(input('Введите число от 0 до 9 включительно:'))
atype = input('bin, oct, hex:')


def vvedennoechislo(): 
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
    
vvedennoechislo()        


#немного тестов
def vvedennoechislo(): 
  assert (7,'bin') == ('Семь', '0b121'), 'Ошибка'
  assert (1,'oct') == ('Один', '0x1'), 'Ошибка'
  assert (2,'hex') == ('Два', '0o2'), 'Ошибка'
  assert (3,'bin') == ('Один', '011'), 'Ошибка'
  assert (2,'oct') == ('Два', '0x2'), 'Ошибка'
```
![alt](https://github.com/herzenuni/sem5-firsttask-04092018-KsushaSeliv/blob/master/11.JPG)

## Самостоятельная работа

#Для программы, сделанной в рамках лабораторной работы 1 и 2, реализуйте с использованием механизма
#декораторов (предпочтительно) или без него (в этом случае будет необходимо использовать еще один аргумент) функционал для
#сохранения истории вычислений функции в файл. 
#При записи в файл предусмотреть вероятность возникновения исключительных ситуаций и создать собственный 
#класс или классы для обработки исключительных ситуаций при записи в файл. 

```python
class RangeException(Exception): #создаём класс, наследуя Exeption, для обработки исключения, которое возникает в ситуации, когда вводится число не из описанного в условии диапазона(0-9);

#создаём конструктор с входным аргументом
  def __init__(self, text): 
        RangeException.txt = text

logger = [] 

try:
    a = int(input('Введите число от 0 до 9 включительно:'))
    if ((a<0)|(a>9)):
      raise RangeException('Число не подходит') #если число не подходит, вылетает исключение
except RangeException: #прописываем наш тип исключения, он просто принтится
    print('Число не подходит')
    a = int(input('Введите число от 0 до 9 включительно:'))

except ValueError:
    print('Число не подходит')
    a = int(input('Введите число от 0 до 9 включительно:'))
atype = input('bin, oct, hex:')



def vvedennoechislo(): 
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
    
     


if len(logger) == 1:   
     logger.append("Отсутствие исключений")
try:
      with open('text.txt', 'a') as f:
        f.write(str(logger) + "\n")
        f.write("Число: " + str(a) + " Система счисления: " +str(atype))
except IOError: #Возбуждается, когда операция ввода-вывода (например, при использовании print() или open()) не проходит. 
#Например: «файл не найден», «диск заполнен» и т.п..
      print("Что-то пошло не так")

vvedennoechislo()      

#немного тестов
def vvedennoechislo(): 
  assert (7,'bin') == ('Семь', '0b121'), 'Ошибка'
  assert (1,'oct') == ('Один', '0x1'), 'Ошибка'
  assert (2,'hex') == ('Два', '0o2'), 'Ошибка'
  assert (3,'bin') == ('Один', '011'), 'Ошибка'
  assert (2,'oct') == ('Два', '0x2'), 'Ошибка'
```

![alt](https://github.com/herzenuni/sem5-firsttask-04092018-KsushaSeliv/blob/master/12.JPG)
![alt](https://github.com/herzenuni/sem5-firsttask-04092018-KsushaSeliv/blob/master/13.JPG)
