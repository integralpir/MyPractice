import random

print('''Аналог шара судьбы... 
Только без шара... 
Если случайность для вас это судьба, то пожалуйста.''')

A = ['Бесспорно','Предрешено','Никаких сомнений','Определённо да','Можешь быть уверен в этом','Мне кажется - да','Вероятнее всего','Хорошие перспективы','Знаки говорят - да','Да, но не совсем','Пока неясно, попробуй снова','Спроси позже','Лучше не рассказывать','Сейчас нельзя предсказать','Сконцентрируйся и спроси опять','Даже не думай','Мой ответ - нет','По моим данным - нет','Перспективы не очень хорошие','Весьма сомнительно']

print('Задайте вопрос.')
print('Задали?')
x = input()
print('Вот ответ на ваш вопрос >>> ', A[random.randint(0,20)])
