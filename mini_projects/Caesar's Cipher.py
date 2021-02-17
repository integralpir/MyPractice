print('Программа шифровки / дешифровки текста по методу Цезаря')
#k = int(input('Введите шаг сдвига для шифровки ( >0 ) или дешифровки ( <0 ) '))
en_alphabet = [chr(i) for i in range(65,91)] + [chr(j) for j in range(97,123)]
ru_alphabet = [chr(i) for i in range(1040,1104)]
def cezar(text):
    if text[0][0] in en_alphabet:
        alphabet = en_alphabet; moch = 26
    else:
        alphabet = ru_alphabet; moch = 32
    A = []
    for i in range(len(text)):
        k = 0
        result = ''
        for z in range(len(text[i])):
            if text[i][z].isalpha():
                k += 1
        for j in range(len(text[i])):
            if text[i][j].isalpha():
                if text[i][j].isupper():
                    result += (alphabet[(alphabet.index(text[i][j]) + k) % moch])
                else:
                    result += (alphabet[(alphabet.index(text[i][j]) + k) % moch + moch])
            else:
                result += text[i][j]
        A.append(result)
    print(*A)
txt = input('Введите текст ').split()
cezar(txt)