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
