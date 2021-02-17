temp = int(input())
if temp < -25:
    print('жутко холодно')
elif temp >= -25 and temp < 0:
    print('холодно')
elif temp >= 0 and temp < 10:
    print('прохладно')
elif temp >= 10 and temp < 25:
    print('тепло')
elif temp >= 25:
    print('жара')