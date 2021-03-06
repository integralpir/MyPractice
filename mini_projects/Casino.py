import random

print('Добро пожаловать! Желаете ознакомиться с правилами игры?')
a = input('''>>> 1 - Да.
>>> 2 - Нет.
>>> ''')
print()
if a == '1':
    print('''Добро пожаловать в наше казино!
Вашему вниманию предлагается игра "Числовая угадайка".
Её правила очень просты. Вам необходимо угадать случайное число от 1 до 100!
У вас будет 10 попыток.
Чем меньше попыток вы потратите, тем больше увеличится ваша ставка.
Если же вы не угадаете число, то ставка сгорает.
Всё просто, я загадываю, ты отгадываешь!''')
print()
print('''Итак, начнём! Сколько фишек вы желаете приобрести?
1 фишка = 100 $''')
print()
n = int(input('Хочу фишек на такую сумму: '))
print()
print('Ваша сдача: ', n % 100)
player_wallet = n // 100

def game(bid, wallet):
    wallet -= bid
    f = random.randint(0,1)
    i = 10
    while i > 0:
        n = int(input('Введите число: '))
        if n == f:
            print('Вы угадали число!')
            print('Ваша ставка увеличивается в', i, 'раз!!!')
            wallet += bid * i
            break
        elif f > n:
            print('Введенное число меньше, чем искомое.')
            i -= 1
            print('У вас осталось', i, 'попыток.')
        elif f < n:
            print('Введенное число больше, чем искомое.')
            i -= 1
            print('У вас осталось', i, 'попыток.')

    else:
        print('У вас кончились попытки, вы проиграли.')
        wallet -= bid

    return wallet

while True:
    print('Ваш баланс составляет:', player_wallet)
    print()
    if player_wallet <= 0:
        print('К сожалению, ваш баланс не позволяет вам продолжить игру. Спасибо за игру!')
        break
    player_bid = int(input('Делайте вашу ставку >>> '))
    player_wallet = game(player_bid, player_wallet)
    print('Желаете продожить игру?')
    answer = int(input('''>>> 1 - Да.
>>> 2 - Нет.
>>> '''))
    if answer == 1:
        print('Отлично! Продолжаем!')
        continue
    else:
        print('Спасибо за игру!')
        break