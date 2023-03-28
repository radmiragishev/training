import random
y = random.randint(0, 101)

def is_valid(x) :
    if x.isdigit() == True and int(x) in range(1, 101) :
        return True 
    return False
   
print('Добро пожаловать в игру "Угадай число"')
count = 1
while True :
    y = int(y)
    x = input('Введите число от 1 до 100:')
    is_valid(x)
    if is_valid(x) is False :
        print('Вы ввели не число или число вне диапазона')
        print('Давайте попробуем еще раз')
        continue
    if is_valid(x) is True :
        x = int(x)    
        if x > y :
            print('Я загадал число меньше, попробуйте еще раз')
            count += 1
            continue
        if x < y :
            print('Я загадал число больше, попробуйте еще раз')
            count += 1
            continue
        if x == y :
            print('Супер, вы угадали число за', count, 'раз!')
            if input('Сыграем еще раз? Введите "Да" - если согласны или "Нет": ').lower() in ['Да','да','lf', 'IF','ДА', 'дА'] :
                print('Я загадал новое число, поехали!')
                y = random.randint(0, 101)
                count = 1
            else :
                print('До встречи!')
                break
